#coding:utf-8
 
import sys,os,copy,datetime,re,xlwt,xlrd,time
from xlutils.copy import copy as xl_copy

def analysis(filename):
    array = []
    reg = re.compile(r'[\[\]\' ]')
    with open(os.path.join(os.getcwd(),filename),"r") as fs:
        for line in fs.readlines()[:4]:
            # print(line)
            if line[-1] == "\n":
                line = line[:-1]
            # print(reg.sub("",line))
            a = []
            for code in reg.sub("",line).split(","):
                a.append(code)
            b = copy.deepcopy(a)
            array.append(b)
            del a[:]
    return array



def result(val,num,arr):
    if num == -1:
        return True
    if val in arr[num]:
        return result(val,num-1,arr)
    else:
        return False


def mixed(filename,arr):
    c = []
    for val in arr[len(arr)-1]:
        # if val == 'P0152':
        #     pass
            # print("start")
        if result(val,len(arr)-2,arr):
            # print(val)
            c.append(val)

    with open(os.path.join(os.getcwd(),filename),"a+") as fs:
        fs.writelines("\n" + str(datetime.datetime.now()) + " :Mixed Result")
        fs.write("\n" + str(c))

    return c

def union(filename,arr):
    d = []
    for val in arr:
        for v in val:
            if v not in d:
                # print (v)
                d.append(v)

    with open(os.path.join(os.getcwd(),filename),"a+") as fs:
        fs.writelines("\n" + str(datetime.datetime.now()) + " :Union Result")
        fs.write("\n" + str(d))    
    return d 


def time_now():
    return time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time()))

def excel(arr):  
    filename = time_now() + ".xls"
    filename_c = filename
    try:
        if not os.path.exists(filename):
            wb = xlwt.Workbook()
            sh = wb.add_sheet('s001',cell_overwrite_ok=True)
            sh.write(0,0,'code')
            wb.save(filename)
        workbook = xlrd.open_workbook(filename,formatting_info=True)
        cwb = xl_copy(workbook)
        csh = cwb.get_sheet(0)
        # sheet1 = workbook.sheet_by_name('s001')
        s = 1
        for code in arr:
            # print(code)
            csh.write(s,0,label = code)
            s += 1
        cwb.save(filename_c)
    except:
        pass


if __name__ == "__main__":
    arr = analysis(sys.argv[1])
    try:
        array = union(sys.argv[1],arr) if sys.argv[2] == "-u" else 0
    except:
        array = mixed(sys.argv[1],arr)
    excel(array)
    print("OK")
    
    



