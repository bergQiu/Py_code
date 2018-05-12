# coding:utf-8

import lxml
from bs4 import  BeautifulSoup
from htmlDownload import  htmldownload
import time

class htmlparse(object):
    def __init__(self):
        self.htmldown = htmldownload()
        self.table_url = []
        self.content = []

    def get_table(self,oldurl,html):
        soup = BeautifulSoup(html, "lxml")
        table = soup.find("p",class_ = "p2").find_all("a",href = True)
        for a in table:
            url_ = oldurl + a.get("href")
            name = a.get_text()
            self.table_url.append({"name":name,"url":url_})
        return self.table_url

    def get_all_url(self,url_,html):
        soup = BeautifulSoup(html,"lxml")
        content = soup.find(class_ = "pic_box").find_all("a",href = True)
        content_ = []
        for a in content:
            name = a.find("p").get_text()
            url = url_ + a.get("href")
            self.content.append({"name":name,"url":url})
        # return self.content






