# coding:utf-8
import lxml,re,time
from bs4 import BeautifulSoup


class HtmlParse(object):

    def __init__(self):
        self.province = ["重庆","天津","北京","上海","香港","澳门","黑龙江","吉林","辽宁","河北","河南","湖南","湖北","陕西","山西","浙江","江苏","安徽","广东","福建","甘肃","贵州","云南","山东","青海", "四川","江西","台湾","广西","宁夏","西藏","内蒙古","新疆"]
        self.province_data = []
    def get_all_url(self,html):
        soup = BeautifulSoup(html,"lxml")
        all_url = []
        for a in soup.find(class_ = "allNameBar").find_all("a",href = re.compile(r".+/aca/371/.+")):
            name = a.text
            url = a.get("href")
            all_url.append({"name":name,"url":url})
        return all_url

    def get_province(self,html):
        soup = BeautifulSoup(html,"html.parser")
        name = soup.find(class_ ="contentBar").find("h1").string
        text = soup.find(class_ = "contentTest").get_text()
        str = ""
        for t in text:
            str += t
        a = re.compile(r"([年|月|日|.|,|。][出生|生于].{5})|([,|。].+省.+人)")
        prov_str = re.search(a,str)
        for addr in self.province:
            if addr in prov_str.group():
                data = {"name":name,"province":addr}
                return data
        print(prov_str.group())
        # print(str)
        showStr = prov_str.group() + "(是何省份）："
        addr_ = input(showStr)
        data = {"name": name, "province": addr_}
        return data
        time.sleep(1)
