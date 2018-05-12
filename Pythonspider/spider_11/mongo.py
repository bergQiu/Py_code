# -*- coding:utf-8 -*-

import pymongo,json,os,csv

conn = pymongo.MongoClient("127.0.0.1",27017)
db = conn.Berg_test
coll = db.test1


path = os.getcwd()
filename = path + "\\test1.json"
if not os.path.exists(filename):
    os.mkdir(filename)

array = []
headers = ["id_","name_"]
for data,i in zip(coll.find(),range(coll.find().count())):
    if data.get("name"):
        data_ = {}
        data_["id_"] = i
        data_["name_"] = data["name"]*5
        array.append(data_)
print("here")
print(array)
with open("data1.csv","w") as f:
    f_csv = csv.DictWriter(f,headers)
    f_csv.writeheader()
    f_csv.writerows(array)

print("OK")