# coding:utf-8
import  time
from htmlDownload import  HtmlDownload
from htmlParse import  HtmlParse
from urlManager import UrlManager
from storedata import StoreData

class SpiderManager(object):
    def __init__(self):
        self.htmldownload = HtmlDownload()
        self.parse = HtmlParse()
        self.urlmanage = UrlManager()
        self.storedata = StoreData()

        self.province = []

    def crawl(self,url):
        html = self.htmldownload.Download(url)
        urls = self.parse.get_all_url(html)
        self.urlmanage.add_urls(urls)
        i = 0
        while self.urlmanage.has_url():
            url = self.urlmanage.get_url()
            html =self.htmldownload.Download(url)
            data = self.parse.get_province(html)
            self.province.append(data)
            i += 1
            print(i)
        # print(self.province)
        self.storedata.store(self.province,"中国科学院院士信息.json")
        result = self.storedata.analysis(self.province)
        self.storedata.store(result, "省份统计结果.json")

if __name__ == "__main__":
    # url = "www.720tb.com"
    spiderManager = SpiderManager()
    spiderManager.crawl("http://www.casad.cas.cn/chnl/371/index.html")
