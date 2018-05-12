# coding:utf-8
import codecs
import time
import json
class Dataoutput(object):
    def __init__(self):
        self.filepath = 'baike_%s.json'%(time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime()))


    def store_data(self,data):
        with open(self.filepath,"w",encoding="utf-8") as f:
            json.dump(data,fp=f,ensure_ascii=False,indent=4)
