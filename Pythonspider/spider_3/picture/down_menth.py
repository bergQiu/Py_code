# -*- coding: utf-8 -*-
import requests,time,os
from bs4 import  BeautifulSoup

def get_html(url):
    html = requests.get(url)
    html.encoding = "utf-8"
    return html.text

def get_page(page_num,url):
    url_ = url +"index_" + str( int(page_num) + 1) +".html"
    return get_html(url_)

def get_topic(html):
    topic_url = []
    soup = BeautifulSoup(html,"lxml")
    for each in soup.find(class_ = "news_list").find_all("a"):
        url_ = "https://3344xg.com/"  + each["href"]
        topic_url.append(url_)
    return topic_url

def download_picture_url(topic_url):
    all_url_down = []
    for each in topic_url:
        html = get_html(each)
        # print(html)
        soup = BeautifulSoup(html,"lxml")
        name = soup.find(class_ = "tit1").string
        img_url = []
        for img in soup.find(class_ = "news").find_all("img"):
            img_url.append(img["src"])
        all_url_down.append({"name":name,"url":img_url})
    return all_url_down

def download_piture(down_url,path):
    for each in down_url:
        url = each["url"]
        name = each["name"]
        i = 0
        file_path = path  + "\\"+ name
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        for url in url:
            path_ = file_path + "\\" + r"img" + str(i) + r".jpg"
            store_picture(url,path_)
            i+=1

def store_picture(url,path_):
    res = requests.get(url)
    with open(path_,"wb") as f:
        f.write(res.content)
        print (path_)


if __name__ == "__main__":
    url = "https://3344xg.com/tupianqu/zipai/"
    path = os.getcwd()
    print ("Welcome to spider download !")
    num_page = input("Please enter the number of download pages：")
    # num_page = 1
    try:
        print("Try to download")
        html = get_page(num_page, url)
        print("Home Download Success, Downloading Theme HTML...")
        topic = get_topic(html)
        print ("Theme HTML download is complete, the image URL is being downloaded...")
        picture_url = download_picture_url(topic)
        print("Image URL download completed,Downloading picture...")
        download_piture(picture_url,path)
        print("Picture download completed")
        time.clock()
    except:
        print ("Download failed")
        pass