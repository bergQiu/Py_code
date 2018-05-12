# coding:utf-8
import requests

class htmlDownload(object):
    def __init__(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
        self.headers = {"User-Agent": user_agent}

    def download(self,url):
        if url is None:
            return
        res = requests.get(url,headers = self.headers)
        if res.status_code ==200:
            res.encoding = "utf-8"
            return  res.text
        return None

