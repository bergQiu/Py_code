# coding:utf-8
from HtmlDownload import htmlDownload
from HtmlParser import  htmlParser
from multiprocessing.managers import BaseManager

class spiderWork(object):
    def __init__(self):
        BaseManager.register("get_task_queue")
        BaseManager.register("get_result_queue")
        server_addr = "127.0.0.1"
        self.m = BaseManager(address=(server_addr,8001),authkey=b"baike")
        self.m.connect()
        self.task = self.m.get_task_queue()
        self.result = self.m.get_result_queue()
        self.downloader = htmlDownload()
        self.parser = htmlParser()
        print ("Init finish")

    def crawl(self):
        while True:
            # try:
            if not self.task.empty():
                url = self.task.get()
                print(url)
                if url == "end":
                    print("控制节点通知爬虫节点停止工作")
                    self.result.put({"new_urls":"end","data":"end"})
                    return
                print("爬虫正在解析%s"%url.encode("utf-8"))
                content = self.downloader.download(url)
                new_urls,data = self.parser.parse(url,content)
                print({"new_urls":new_urls,"data":data})
                self.result.put({"new_urls":new_urls,"data":data})
            # except:
            #     print("链接工作节点失败")
            #     return
        # except Exception,e:
        #     print (e)
        #     return

if __name__ == "__main__":
    spider = spiderWork()
    spider.crawl()