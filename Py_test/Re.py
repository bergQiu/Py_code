# coding:utf-8
# 2018/01/09
# 正則表達式測試

import re

Str = r"<html><body><h1>hello world<h1></body></html>"

key = r"chuxiuhong@hit.edu.cn"

s ="""
GET /?username=usernam&passworld=passworld&message=message HTTP/1.1
Host: 10.9.235.101:8012
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8
"""
testcode = "abcdefg"


result = re.findall(r"(?<=x)[a-z]+@[a-z]+(?=.)",key)
test = re.findall(r"(?<=<h1>).+(?=<h1>)",Str)
result1 = re.findall(r'(?<=/\?).+(?= )',s)
info = re.findall(r"(?<=User-Agent:).+",s)

code = re.findall(r"efg$",testcode)
ip = re.findall(r"[12]\d{0,2}",s)

print code
print ip
print test
print result1
print info
