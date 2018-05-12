# coding:utf-8
import requests
class htmlDownload(object):

    def download(self,url):
        if url is None:
            return
        user_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
        headers = {"User-Agent":user_Agent}
        res = requests.get(url, headers = headers)
        if  res.status_code == 200:
            res.encoding = "utf-8"
            # print (res.text)
            return res.text
        return  None
