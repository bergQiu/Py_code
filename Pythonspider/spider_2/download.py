
import urllib,requests,os
from lxml import etree

# def show_scedule(blocknum,blocksize,totalsize):
#     per = 100 *  blocknum * blocksize / totalsize
#     if per > 100:
#         per = 100
#     print ("当前下载进度：",per)


# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
# url = "http://ivsky.com/tupian/ziranfengguang/"
# headers = {"User_Agent":user_agent}
#
# res = requests.get(url,headers = headers)
# html = etree.HTML(res.text)
# img_url = html.xpath('.//img/@src')
# print (img_url)
# # i = 0
# for url in img_url:
#     real =  r"img"+str(i)+r".jpg"
urllib.request.urlretrieve("http://img.ivsky.com/img/tupian/li/201710/31/yueliang-003.jpg",r"1.jpg")
#     i+=1

