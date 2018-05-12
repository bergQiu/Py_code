# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem

class Spider10ScrapyPipeline(object):
    def __init__(self):
        self.file = open('papers.json', 'wb')

    def process_item(self, item, spider):
        if item['title']:
            line =json.dumps(dict(item),ensure_ascii = False)+ "\n"
            print("666")
            self.file.write(line.encode("utf-8"))
            return item
        else:
            raise DropItem("missing title in %s"% item)
