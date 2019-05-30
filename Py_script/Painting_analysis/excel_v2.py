# coding:utf-8
# 2018/09/26
# 多文件分析統計繪表

from __future__ import division
import sys,os,re,xlwt,xlrd,time,datetime
from xlwt import Workbook
from xlutils.copy import copy 


def set_style(name,height,bold=False):
    style = xlwt.XFStyle()

    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height

    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER

    style.alignment = alignment
    style.font = font 

    return style

def set_style_yellow(name,height,bold=False):
    style = set_style("Arial",220,True)

    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 5
    style.pattern = pattern

    return style

def analysis():
    d = {}
    for filename in os.listdir(os.getcwd()):
        file_name = os.path.join(os.getcwd(),filename)
        if not re.search(r'.txt',file_name):
            continue
        i,j = 0,0
        no = []
        n = re.compile(r'\D+')
        # wa = re.search(r'[A-Za-z]+',file_name.split("\\")[-1]).group()
        wa = file_name.split("\\")[-1][:4]
        try:
            d[wa]
        except:
            d[wa] = {}
        name = n.search(file_name.split("\\")[-1]).group()[:-1]
        r = re.compile(r'P\d+')
        with open(file_name,'r') as fs:
            for f in fs.readlines():
                if "Not scanned" in f:
                    i += 1
                    if r.search(f):
                        no.append(r.search(f).group())
                if "%" in f:
                    # print(f)
                    # print(j)
                    break
                    # sys.exit()
                j += 1  
            str_ = "Total {0}, missing brush {1}, leak rate {2} %\n".format(j-2,i,round(i*100/(j-2),2))
        # with open(file_name,'a') as q:
        #     q.writelines(str_)
        #     q.writelines(str(no))
        d[wa][name] = {
            "Total":j-2,
            "Miss":i,
            "Rate":round(i*100/(j-2),2),
            "Array":no
        }
    # print(d)
    return d

def get_excel(data):
    csh,cwb,filename = create_excel(data)
    n = 0
    for d in data:
        for key in data[d]:
            csh.write_merge(2,2,n,n+3, ("共計條碼" + str(data[d][key]['Total'])).decode('utf-8'),set_style("Arial",220,True))
            break
        for key in data[d]:
            # print(data[d][key])
            csh.write_merge(1,1,n,n+1,("線別：" + key).decode('utf-8'),set_style("Times New Roman",220,True))
            csh.write_merge(3,3,n,n+1, ("成功率" + str(100 - data[d][key]['Rate']) + "%" ).decode('utf-8'),set_style("Arial",220,True))
            csh.write_merge(4,4,n,n+1, ("漏刷數量"+ str(data[d][key]['Miss'])).decode('utf-8'),set_style("Arial",220,True))
            s = 5
            for code in data[d][key]['Array']:
                csh.write(s,n,label = code)
                s += 1
                # print(code)
            n += 2
    print("OK")
    cwb.save(filename)
    return 

def create_excel(data):
    filename = get_date_file() + "_test.xls"
    if not os.path.exists(filename):
        wb = Workbook()
        sh = wb.add_sheet('s001',cell_overwrite_ok=True)
        wb.save(filename)
        print("[" + get_date() +" ] " + filename + "Create successful")
    workbook = xlrd.open_workbook(filename,formatting_info=True)
    cwb = copy(workbook)
    csh = cwb.get_sheet(0)

    csh.write_merge(0,0,0,2*len(data),get_date() ,set_style("Arial",220,True))
    return csh,cwb,filename

def get_excel_v2(data):
    csh,cwb,filename = create_excel(data)    
    n = 0
    for d in data:
        temp_sum = []
        temp_all = {}
        for key in data[d]:
            if re.search(r"up",key):
                temp_all["up"] = data[d][key]["Array"]
            if re.search(r"down",key):
                temp_all["down"] = data[d][key]["Array"]
            temp_sum += data[d][key]["Array"]

        for key in data[d]:
            csh.write_merge(2,2,n,n+3, ("共計條碼" + str(data[d][key]['Total'])).decode('utf-8'),set_style("Arial",220,True))
            break
        l = {}
        for key in data[d]:
            if(n/2%2 == 0):
                l[key.split("_")[-1]] = 0
            if(n/2%2 == 1):
                l[key.split("_")[-1]] = 1
            csh.write_merge(1,1,n,n+1,("線別：" + key).decode('utf-8'),set_style("Times New Roman",220,True))
            csh.write_merge(3,3,n,n+1, ("成功率" + str(100 - data[d][key]['Rate'] ) + "%" ).decode('utf-8'),set_style("Arial",220,True))
            csh.write_merge(4,4,n,n+1, ("漏刷數量"+ str(data[d][key]['Miss'])).decode('utf-8'),set_style("Arial",220,True))
            n += 2
        # print(l)
        s = 5
        t = n - 4 
        temp = list(set(temp_sum))
        temp.sort()
        for code in temp:
            if temp_sum.count(code) == 2 :
                # print(code)
                csh.write_merge(s,s,t,t, code,set_style_yellow("Arial",220,True))
                csh.write_merge(s,s,t+2,t+2, code,set_style_yellow("Arial",220,True))
                s += 1
            elif code in temp_all["down"]:
                if l["down"] == 0:
                    csh.write_merge(s,s,t,t, code,set_style("Arial",220,True))
                else:
                    csh.write_merge(s,s,t+2,t+2, code,set_style("Arial",220,True))
                s += 1
            elif code in temp_all["up"]:
                if l["up"] == 1:
                    csh.write_merge(s,s,t+2,t+2, code,set_style("Arial",220,True))
                else:
                    csh.write_merge(s,s,t,t, code,set_style("Arial",220,True))
                s += 1
            else:
                pass
    # print("OK")
    cwb.save(filename)
    return

def get_date():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

def get_date_file():
    return time.strftime("%m%d_%H%M",time.localtime())

if __name__=='__main__':
    # print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    data = analysis()
    # print(len(sys.argv))
    try:
        get_excel_v2(data) if (len(sys.argv) >= 2) and sys.argv[1] == "-v" else get_excel(data)
    except:
        get_excel(data)

    print("complete")

