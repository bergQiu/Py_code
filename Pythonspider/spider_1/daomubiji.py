from bs4 import  BeautifulSoup
import requests,json,csv

url = "http://www.seputu.com"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
headers = { "User_Agent" : user_agent }
res = requests.get(url,headers = headers)

#file = open("result.html",'w',encoding='utf-8')
#file.write(res.text)

soup = BeautifulSoup(res.text,'lxml')
content = []
content1 = []
for each_mulu in soup.find_all(class_ = 'mulu'):
    h2 = each_mulu.find('h2')
    if h2 != None:
        h2_title = h2.string
        list = []
        for a in each_mulu.find(class_ = 'box').find_all('a'):
            href = a.get('href')
            a_title = a.string
            list.append({'href':href,'box_title':a_title})
            content1.append([h2_title,a_title,href])
        content.append({'title':h2_title,'content':list})

#with open('content.json','w',encoding='utf-8') as f:
#    json.dump(content,fp = f,indent = 4,ensure_ascii=False)
hader = ["title","a_title","href"]
with open("content.csv","w",encoding='utf-8') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(hader)
    f_csv.writerows(content1)

#with open('content.json',encoding='utf-8') as fp:
#   print (fp.read())
#print (res.text)