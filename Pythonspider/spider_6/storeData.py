# conding:utf-8

import json,os,time

class storedata(object):
    def __init__(self):
        pass

    def outpujson(self,data,path):
        filename = path + data.get("name") + "(" + str(len(data.get("data")))+ ")" + ".json"
        data_ = data.get("data")
        print(filename)
        with open(filename,"w",encoding="utf-8") as f:
            json.dump(data_,fp=f,indent=4,ensure_ascii=False)
        print(data.get("name")+ "Saved successfully")
        print(time.clock())

