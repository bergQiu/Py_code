# coding:utf-8
# 2018/10/26
# 批量更新Mongo資料庫IP設定from excel

import xlrd,pymongo
from xlutils.copy import copy

def readEcel():
    wb = xlrd.open_workbook('C:\Users\Berg.Qiu\Desktop\ipconfig.xlsx')
    table = wb.sheet_by_name(u'Sheet1')
    rows = table.nrows
    ipconfig = {}
    for i in range(rows):
        if table.cell_value(i,1):
            Buil = table.cell_value(i,1)
            ip = table.cell_value(i,19)
            ipconfig[Buil] = ip
    return ipconfig

def updateDB(data):
    myclient = pymongo.MongoClient("mongodb://10.10.0.96:27017")
    berg =  myclient['test_Berg']
    coll = berg['tpmis_pressure_config'] 
    for i in data:
        coll.update_one(
            {'Building':i},
            {'$set':{'IP':data[i]}}
            )

if __name__ == '__main__':
    config = readEcel()
    # updateDB(config)
    print("OK")