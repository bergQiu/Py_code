# coding:utf-8
import json

class StoreData(object):

    def __init__(self):
        self.result = {}
        pass

    def analysis(self,array):
        for data in array:
            if data["province"] not in self.result:
                self.result[data["province"]] = 1
            else:
                self.result[data["province"]] += 1
        return self.result

    def store(self,array,nameStr):
        if array is None:
            return
        try:
            with open(nameStr,"w",encoding= "utf-8") as f:
                json.dump(array,fp=f,indent=4,ensure_ascii=False)
                print(nameStr + " is OK")
        except:
            print("here are some error")
