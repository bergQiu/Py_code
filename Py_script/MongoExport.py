#coding:utf-8
# 2019/03/15
# Python  修改MongoExport,按條件導出

import pymongo,time,xlwt,xlrd,getopt,sys,os,json    
from xlwt import Workbook
from xlutils.copy import copy

def get_parameter():
    opts,args = getopt.getopt(sys.argv[1:],"h:d:c:q:f:o:",["help"])
    para = {}
    for op,value in opts:
        if op == "--help":
            show_message()
            sys.exit()
        if op == "-h":
            para['host'] = value
        elif op == "-d":
            para['database'] = value
        elif op == "-c":
            para['collection'] = value
        elif op == "-q":
            para['query'] =value.replace("'",'"')
        elif op == "-f":
            para['keys'] = value
        elif op == "-o":
            para['files'] = value
    return para

def excel(data,cmd):
    filename = cmd['files']
    if not os.path.exists(filename):
        wb = Workbook()
        sh = wb.add_sheet('s001',cell_overwrite_ok=True)
        wb.save(filename)
    workbook = xlrd.open_workbook(filename,formatting_info=False)
    cwb = copy(workbook)
    csh = cwb.get_sheet(0)
    keys = cmd['keys'].split(',')
    for key in range(len(keys)):
        csh.write(0,key,label = keys[key])
    n = 1
    for d in data:
        for key in range(len(keys)):
            try:
                csh.write(n,key,label = d[keys[key]])
            except:
                pass
        n = n + 1
    cwb.save(filename)
    print(  filename + " was created successfully,Total export :"  + str(n-1) )
    return 
        
def show_message():
    print(
        '''
CMD Parameter Description
    -h  db hostname and port
    -d  database name
    -c  collection name
    -q  query for find ----- eg : <-q {'name':'test'}>
    -f  Keyword What you need
    -o  output filename , Complete route
    --help cat help info
cmd eg : python Mongoexport.py -h 10.10.*.*:27017 -d database -c collection -q {'name':'test'} -f "Desc,Energy"- o c:\t9.xls   
        '''
    )

if __name__ == "__main__":
    cmd = get_parameter()
    try:
        conn = pymongo.MongoClient('mongodb://' + cmd['host'] + '/')
        db = conn[cmd['database']]
        coll = db[cmd['collection']]
    except:
        print("connect DB error,please check you paramter")

    data = coll.find(json.loads(cmd['query']))
    excel(data,cmd)
