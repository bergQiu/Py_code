#!python2
#coding:utf-8
import itchat
from collections import Counter
from  pprint import pprint 
itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)[0:]

provinces=[]  # #获取 所有好友的省份信息
for friend in friends:
    provinces.append(friend['Province'])

province_d=Counter(provinces)  ##利用自带的Counter,统计省份出现的次数

pro_list =[ i.strip()  for i in  open("pro_list.txt").readlines()]
fh=open("pro_no.txt",'w')
for pro in pro_list:
    pro = pro.decode('utf8')
    num=  province_d[pro] if pro in province_d.keys() else 0
    fh.write(str(num)+"\n")

