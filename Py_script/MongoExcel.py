# -*-coding:utf-8 -*-
# 2018/03/24


import xlwt,pymongo,sys,getopt,time

class show_process:
    def __init__(self,max_steps):
        self.max_steps = max_steps
        self.max_arrow = 60
        # self.i = i
    def show_pro(self,i):
        if i >= 0:
            num_arrow = int(i*self.max_arrow/self.max_steps)
            num_line = self.max_arrow - num_arrow
            percent = i*100/self.max_steps
            pro_bar = "Process:["+">"*num_arrow + "-"*num_line + "]" + "  %.2f"%percent + "%" + "\r"
            sys.stdout.write(pro_bar)
            sys.stdout.flush()



def set_style(name,height,bold=False):
    style = xlwt.XFStyle()

    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.colour_index = 2
    font.height = height

    style.font = font
    return style

def argv_parser(key_array,para):
    options,args = getopt.getopt(sys.argv[1:],"i:p:d:c:n:o:f:h")
    # print(options)
    # print(args)
    for name,value in options:
        if name == "-h":
            print ('''
 -i ip for hostserver
 -p port for hostserver
 -d chose db
 -c chose collection
 -n number for serach
 -o output file
 -f show key that you need
                    ''')
            sys.exit()                
        if name == "-f":
            key_array = value.split(",")
            continue
        para[name] = value
    return key_array,para

def craw_title(sheet,*key):
    # print (key)
    for k,i in zip(key,range(len(key))):
        sheet.write(0,i,k,set_style("Times New Roman",300,True))

def craw_row(j,data,*key):
    for k,i in zip(key,range(len(key))):
        if not isinstance(data[k],str) and not isinstance(data[k],int):
            sheet1.write(j,i,str(data[k]))
            continue
        sheet1.write(j,i,data[k])

if __name__ == "__main__":
    para = {}
    key_array = []
    array,para = argv_parser(key_array,para)

    # print (array)
    # print (para)

    conn = pymongo.MongoClient(para["-i"],int(para["-p"]))
    db = conn[para["-d"]]
    coll = db[para["-c"]] 
    # array = ["66","77","88","99"]

    f =xlwt.Workbook()
    sheet1 = f.add_sheet("shrrt1",cell_overwrite_ok = True)
    craw_title(sheet1,*array)
    
    process_bar = show_process(int(para["-n"])-1)

    for  data,i,n in zip(coll.find(),range(coll.find().count()),range(int(para["-n"]))):
        process_bar.show_pro(n)
        craw_row(i+1,data,*array)
    f.save(para["-o"])


 