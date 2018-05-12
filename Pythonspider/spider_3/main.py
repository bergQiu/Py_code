# -*- coding: utf-8 -*-
import requests,chardet,json,csv,re,time
from bs4 import  BeautifulSoup

url = "https://3344xg.com/"
user_agnet ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"

'''首页
html = requests.get(url,headers = {"User-Agent":user_agnet})

html.encoding = "utf-8"
#str(html,encoding='utf-8')
#with open("html.html","w",encoding="utf-8") as f:
#   f.write(html.text)
#print(html.text)
soup = BeautifulSoup(html.text,"lxml")
'''




''''自拍前十页
url = "https://3344xg.com/tupianqu/zipai/"
content = []

for i in range(10):
    if  i:
        url_ = url + "index_" + str(i+1)+".html"
    else:
        url_ = url

    html = requests.get(url)
    html.encoding = "utf-8"
    # with open("zipai.html","w",encoding="utf-8") as f:
    #    f.write(html.text)
    soup = BeautifulSoup(html.text,"lxml")

    for each in soup.find(class_="news_list").find_all("a"):
        each_url = "https://3344xg.com/" + each["href"]
        each_title = each["title"]
        content.append({"url":each_url,"title":each_title})

with open("zipai.json","w",encoding="utf-8") as f:
    json.dump(content,fp = f,ensure_ascii = False, indent = 4)
print("complete")
print (time.clock()+" s")

'''

''''mulu
menu_list  = soup.find_all(class_ = "menu")
type = ["图片区","小说区","电影区"]
content = []
for each in menu_list:
    dt = each.find("dt")
    name = dt.string
    if name in type:
        a = each.select("dd a")
        for a in a:
            url_ ="https://3344xg.com"+ a["href"]
            str_ =a.string
            content.append({"type":name,"name":str_,"url":url_})
print(content)
headers = ["type","name","url"]
with open("csv_1.csv","w",encoding="utf-8") as s:
    f_csv = csv.DictWriter(s,headers)
    f_csv.writeheader()
    f_csv.writerows(content)
'''

''''home_list  推荐
home = soup.find(class_ = "home_list")
home_url_list = []

for each in home.find_all(href = True):
    url_ = "https://3344xg.com" + each.get("href")
    name_ = each.string
    home_url_list.append({"url":url_,"name":name_})

with open("json_1.json","w",encoding="utf-8") as fp:
    json.dump(home_url_list,fp = fp,indent = 4,ensure_ascii= False)
print("doenload success")
'''

