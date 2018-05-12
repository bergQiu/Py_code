# coding:utf-8
import requests

class HtmlDownload(object):

    def Download(self,url):
        if url is None:
            return
        user_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
        headers = {"User-Agent":user_Agent}
        html = requests.get(url,headers = headers)
        # print(html.text)
        return html.text
