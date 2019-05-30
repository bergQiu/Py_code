# coding:utf-8
# 2018/09/08
# 單文件分析

from __future__ import division
import sys,os,re


# file_name = r'C:\Users\Berg.Qiu\Desktop\pytest\tz_code_px.txt'


def analysis(file_name):
    i,j = 0,0
    no = []
    r = re.compile(r'P\d+')
    with open(file_name,'r') as fs:
        for f in fs.readlines():
            j += 1
            if "Not scanned" in f:
                i += 1
                if r.search(f):
                    no.append(r.search(f).group())
            if "Total" in f:
                print("Already analyzed")
                print(no)
                fs.close()
                sys.exit()
        str_ = "Total {0}, missing brush {1}, leak rate {2} %\n".format(j-1,i,round(i*100/j,2))
    with open(file_name,'a') as q:
        q.writelines(str_)
        q.writelines(str(no))
        # f = fs.readline()
        # print (f)

if __name__=='__main__':
    file = sys.argv[1]
    file_name = os.path.join(os.getcwd(),file)
    print(file_name)
    analysis(file_name)
    print("Operation completed")

