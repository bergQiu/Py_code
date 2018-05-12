# -*- coding: utf-8 -*-
import requests,chardet,json,csv,re,time,urllib
from bs4 import  BeautifulSoup


# def get_html(url):
#     html = requests.get(url)
#     html.encoding = "utf-8"
#     return html.text
#
# def get_page(page_num,url):
#     url_ = url +"index_" + str(page_num+1) +".html"
#     return get_html(url_)
#
# def get_topic(html,url):
#     topic_url = []
#     soup = BeautifulSoup(html,"lxml")
#     for each in soup.find(class_ = "new list").find_all("a"):
#         url_ = "https://3344xg.com/"  + each["href"]
#         topic_url.append(url_)
#     print(topic_url)
#     return topic_url
#
# def download(topic_url):
#     all_url = []
#     for each in topic_url:
#         html = get_html(each)
#         soup = BeautifulSoup(html,"lxml")
#         img_url = []
#         for img in soup.find(class_ = "news").find_all("img"):
#             img_url.append(img["src"])
#
#         all_url.append({"topic":img_url})
#     return all_url

if __name__ == "__main__":
    url = "https://3344xg.com/tupianqu/zipai/"
    print ("Welcome to spider download !")
    num_page = input("请输入下载页数：")

    html = get_page(num_page,url)
    print ("首页下载成功，正在下载主题HTML")



'''
num = 0
all_img = []
path = r"C:\Users\QZL\Desktop\Python spider\spider_3\picture\image"
#user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
url = "https://3344xg.com/tupianqu/zipai/"
content = []
page_num = input("请输入下载的页数：")
for i in range(int(k)):
    if  i:
        url_ = url + "index_" + str(i+1)+".html"
    else:
        url_ = url
    html = requests.get(url)
    html.encoding = "utf-8"
    #print(html.text)
    with open("html1.html","w",encoding="utf-8") as f:
       f.write(html.text)
    soup = BeautifulSoup(html.text,"lxml")

    for each in soup.find(class_="news_list").find_all("a"):
        each_url = "https://3344xg.com/" + each["href"]
        each_title = each["title"]
        content.append({"url":each_url,"title":each_title})
for each in content:
    url_a = each["url"]
    # url_a = content[0]["url"]
    html = requests.get(url_a)
    html.encoding = "utf-8"
    with open("html2.html","w",encoding="utf-8") as f:
       f.write(html.text)
    soup = BeautifulSoup(html.text,"lxml")
    img_url = []
    for img in soup.find(class_ = "news").find_all("img"):
        real =r"img" + str(i) + r".jpg"
        url = img["src"]
        img_url.append(url)
    #print (img_url)
    for url in img_url:
        real = path + "\\"+ r"img"+str(i)+r".jpg"
        #print(real)
        i+=1
        all_img.append({"url":url})
        print(i)
print (all_img)
        print (1i,url)
        urllib.request.urlretrieve("http://cache4.onlyimg.com/pics/2018012614/227114.jpg",real)

        res = requests.get(url)
        with open(real,'wb') as f:
            f.write(res.content)

print(len(content))
print(content)
with open("zipai.json","w",encoding="utf-8") as f:
    json.dump(content,fp = f,ensure_ascii = False, indent = 4)
'''