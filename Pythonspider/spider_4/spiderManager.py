# coding:utf-8
from htmlDownload import htmlDownload
from htmlParser import htmlParser
from dataOutput import dataOutput
from urlManager import urlManager
import time

class spiderMan(object):
    def __init__(self):
        self.manager = urlManager()
        self.downloader = htmlDownload()
        self.parser = htmlParser()
        self.Output = dataOutput()

    def crawl(self,root_url):
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.old_urls_size() < 5):
            try:
                url = self.manager.get_new_url()
                html = self.downloader.download(url)
                new_url,new_data = self.parser.parser(url,html)
                self.manager.add_new_urls(new_url)
                # print(self.manager.new_urls)
                print("已抓取%s个链接"%self.manager.old_urls_size())
                self.Output.store_data(new_data)
                time.sleep(0.2)
            except:
                print("craw failed")
        print(self.Output.datas)
        # self.Output.output_html()
        self.Output.output_json()

if __name__ == "__main__":
    spiderMan =spiderMan()
    spiderMan.crawl("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB")