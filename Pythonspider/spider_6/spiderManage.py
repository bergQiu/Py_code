# coding:utf-8
from htmlDownload import  htmldownload
from htmlParse import  htmlparse
from storeData import storedata
import time,re,threading,os

class spiderthread_(threading.Thread):
    def __init__(self,name,oldurl,url):
        threading.Thread.__init__(self,name = name)
        self.download = htmldownload()
        self.parse = htmlparse()
        self.store = storedata()
        self.oldurl = oldurl
        self.url_ = url
        pass

    def run(self):
        print(self.name + "is start download,url is " + self.url_)
        i = 2
        while True:
            try:
                html = self.download.down(self.url_)
                some = self.parse.get_all_url(self.oldurl,html)
                r = re.compile(r"(?<=/)\d.*(?=-*\d*\.)")
                url_t = str(re.search(r, self.url_ ).group()[0] + "-" + str(i))
                self.url_ = re.sub(r, url_t, self.url_)
                i += 1
                print(self.url_ + " Began to parse")
            except:
                break
                pass
        # print(self.parse.content)
        data = {"name": self.name, "data": self.parse.content}
        path = os.getcwd()
        path_ = path + "\\" + "result\\"
        if not os.path.exists(path_):
            os.mkdir(path_)
        self.store.outpujson(data,path_)
        # print(data.get("name") + " successful")




class spidermanager(object):
    def __init__(self):
        self.htmldown = htmldownload()
        self.parse = htmlparse()
        self.store = storedata()
        pass

    def crawl(self,url):
        html = self.htmldown.down(url)
        table = self.parse.get_table(url,html)
        print(table)
        for t in table:
            spiderthread_(name= t.get("name"),oldurl= "http://www.720td.com", url= t.get("url")).start()
        print()



if __name__ == "__main__":
    spider = spidermanager()
    spider.crawl("http://www.720td.com")
    # he = {"name":"666","data":"777"}
    # table = [{'name': '校园女神', 'url': 'http://www.720td.com/aalt/1.html'},
    #  {'name': '国产自拍', 'url': 'http://www.720td.com/aalt/2.html'}]
    # #  {'name': '空姐嫩模', 'url': 'http://www.720td.com/aalt/3.html'},
    # #  {'name': '职场偷情', 'url': 'http://www.720td.com/aalt/4.html'}]
    #  # {'name': '车震野合', 'url': 'http://www.720td.com/aalt/5.html'},
    #  # {'name': '熟女人妻', 'url': 'http://www.720td.com/aalt/6.html'},
    #  # {'name': '自慰群交', 'url': 'http://www.720td.com/aalt/7.html'},
    #  # {'name': '名人明星', 'url': 'http://www.720td.com/aalt/8.html'}]
    # for t in table:
    #     print (t.get("url"))
    #     spiderthread_(name= t.get("name"),oldurl= "http://www.720td.com", url= t.get("url")).start()
    #     time.sleep(5)
    # spider.store.outpujson(he)