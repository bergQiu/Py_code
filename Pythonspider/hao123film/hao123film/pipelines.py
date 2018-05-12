# -*- coding: utf-8 -*-
import json,pymongo,urllib
from scrapy.exceptions import DropItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class Hao123FilmPipeline(object):
    def __init__(self):
        self.file = open("result.json","wb")
        self.conn = pymongo.MongoClient("127.0.0.1", 27017)
        self.db = self.conn.Berg_test
        self.coll = self.db.hao123

    def process_item(self, item, spider):
        if item['name']:
            path = os.getcwd()
            if not os.path.exists(path+'\\image'):
                os.mkdir(path+'\\image')
            # 下载图片
            urllib.request.urlretrieve(url=item['image_url'],filename=path + '\\image\\'+ item['name'] + '.jpg')
            return item
        else:
            raise DropItem("Missing title in %s"%item)


