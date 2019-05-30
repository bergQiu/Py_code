#-*- coding:utf-8 -*-
# 2018/03/13
# Mongo CRUD\Aggregate test

import pymongo,time
import random,re,datetime
from pyecharts import Line


conn = pymongo.MongoClient("10.10.0.96",27017)
db = conn.test_Berg
# collection = db.tpmis_temp_humi_config
# collection_ = db.tpmis_temp_humi_erp
# collection__ = db["__tpmis_temp_humi_config"]
coll = db.tpmis_control_KEP
# coll = db.tpmis_temp_humi_shorthistory

# t = datetime.datetime.now() - datetime.timedelta(days = 2)
# t1 = datetime.datetime.now()
# print("Start: %s"%t)
# print("End: %s"%t1)
# print("****************")





# print ("A")
# data = []
# random = []
# print (collection.find().count())
# Repo = "88B31"
# Location = "01"
# pipeline = [
#          {'$match':{'Repo':Repo,'Location':re.compile(r'.+' + Location)}},
#          {'$unwind':'$Data'}
#     ]
# ************************************
# print(datetime.datetime(2018,4,28))
# print(datetime.datetime(2018,4,29))
if __name__ == "__main__":
    old_start ="2018-04-21 08:34:42"
    old_end = "2018-05-24 00:21:42"
    user = "Berg_3"
    print datetime.datetime.strptime(old_start,'%Y-%m-%d %H:%M:%S')- datetime.timedelta(hours  = 8 )
    print datetime.datetime.strptime(old_end,'%Y-%m-%d %H:%M:%S')- datetime.timedelta(hours  = 8 )
    for data in coll.find({
                "User":user,
                "Start":{"$gt":datetime.datetime.strptime(old_start.encode('utf-8'),'%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours =8,seconds =1),
                                "$lt":datetime.datetime.strptime(old_start.encode('utf-8'),'%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours =8) + datetime.timedelta(seconds =1)},
                "End":{"$gt":datetime.datetime.strptime(old_end.encode('utf-8'),'%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours =8,seconds =1),
                                "$lt":datetime.datetime.strptime(old_end.encode('utf-8'),'%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours =8,) + datetime.timedelta(seconds =1)}
                }):
        print (data)
# ************************************************************
    # for data in coll.find():
    #     start = data['Start'] + datetime.timedelta(hours =8)
    #     data['Start'] = start.strftime("%Y %m %d %H:%M:%S")
    #     end = data['End'] + datetime.timedelta(hours =8)
    #     data['End'] = end.strftime("%Y %m %d %H:%M:%S")
    #     print data['End']


# ******************************************************
    # pipeline = [
    #     {"$match":{
    #         # 'Location':"MOXA_001_01",
    #         "Start":{"$gt":datetime.datetime.now() - datetime.timedelta(hours = 8 , days  = 2)},
    #         "End":{"$lt":datetime.datetime.now()}
    #         # "Start":{"$gt":t1},
    #         # "End":{"$lt":t}
    #         }},
            
    #      {"$unwind":"$Data"},
    #     #  {"$match":{
    #     #     'Data.Update':{'$gt':t1},
    #     #     # 'End':{'$lt':t}
    #     #  }}
    #      {"$match":{'Data.Temp':0}},
    #     # {'$match':{'Data.Update':{'$gt':datetime.datetime.now() - datetime.timedelta(hours  = 8 , days  = 1)}}}
    #      {"$group":{"_id":"$Location","count":{"$sum":1}}}
    # ]
    # result = {
    # }
    # for each in coll.aggregate(pipeline):
    #     # print (each["Data"]["Update"])
    #     # result[each["_id"]] = each["count"]
    #     print ("%s :---- %s "%(each['_id'],each['count']))  

    # print(result)
# ********************************************

    # Repo = "88B31"
    # Location = "01"
    # pipeline = [
    #      {'$match':{'Repo':Repo,'Location':re.compile(r'.+' + Location)}},
    #      {'$unwind':'$Data'}
    # ]
    # h_data = []
    # t_data = []
    # R_h_data = []
    # R_t_data = []
    # time = []
    # for each in coll.aggregate(pipeline):
    #     h_data.append(float(each['Data']['Humi']))
    #     t_data.append(float(each['Data']['Temp']))
    #     R_h_data.append(float(each['Data']['HumiRef']))
    #     R_t_data.append(float(each['Data']['TempRef']))
        # time.append(each['Data']['Update'])
        # s = each['Data']['Update'] + datetime.timedelta(hours = 8)
        # text = s.strftime("%Y-%m-%d %H:%M:%S")
        # print (text)
        # print(each)

    # result = {
    #     "Temp":t_data,
    #     "Humi":h_data,
    #     "Time":time
    # }

    # line = Line("request.POST")
    # line.add("Temp",time,t_data,is_stack = True,is_label_show = True)
    # line.add("Humi",time,h_data,is_stack = True,is_label_show = True)
    # line.add("RefTemp",time,R_t_data,is_stack = True,is_label_show = True)
    # line.add("RefHumi",time,R_h_data,is_stack = True,is_label_show = True)

    # context = line.render_embed()
    # js = line.get_js_dependencies()
    # print(js)
    # line.render()
    # print(context)
# print (re.compile(r''+Location+''))

# for i in range(collection__.find().count()):

#     db.tpmis_temp_humi_config.insert({
#         "WA":collection__.find()[i]["WA"],
#         "Repo":collection__.find()[i]["Repo"],
#         "Building":collection__.find()[i]["Building"],
#         "Floor":collection__.find()[i]["Floor"],
#         "Reference":collection__.find()[i]["Reference"],
#         "Location":collection__.find()[i]["Location"],
#         "Spec":{
#             "0":[0,80],
#             "1":[80,85],
#             "2":[85,90],
#             "3":[90,200]
#         }

#     })
# print ("Update Successful!")

    # if not isinstance(collection.find()[i]["Repo"],str)://判斷類型
    #     collection.update({"_id":collection.find()[i]["_id"]},
    #     {"$set":{"Repo":str(collection.find()[i]["Repo"])}}
    #     )

    # hisData = collection.find()[i]
    # erpData = collection_.find()[i]
    # WA = erpData["WA"]
    # Repo = erpData["Repo"]
    # Building = erpData["Building"]
    # Floor = erpData["Floor"]
    # Location = "MOXA_001_" + str(i+1)

    # newLocation = collection.find()[i]["Location"][:9] + "0" +collection.find()[i]["Location"][-1]
    # print (newLocation)

    # print (MOXA)
    # collection.update(
    #     {"_id":collection.find()[i]["_id"]},
    #     {"$set":{
    #         "MID":hisData["MID"],
    #         "WA":WA,
    #         "Repo":Repo,
    #         "Building":Building,
    #         "Floor":Floor,
    #         "Location":Location,
    #         "TempMax":hisData["TempMax"],
    #         "TempMin":hisData["TempMin"],
    #         "HumiMax":hisData["HumiMax"],
    #         "HumiMin":hisData["HumiMin"],
    #         "CompCnt":hisData["CompCnt"],
    #         "Reference":False,
    #         }}
    # )

    # collection.update(
    #     {"_id":collection.find()[i]["_id"]},
    #     {"$set":{
    #         "Location":newLocation
    #     }}
    # )

    # collection.update(
    #     {"_id":collection.find()[i]["_id"]},
    #     {"$unset":{
    #             "Temp_max":"",
    #             "Temp_min":"",
    #             "Humi_max":"",
    #             "Humi_min":"",
    #     }}
    # )

