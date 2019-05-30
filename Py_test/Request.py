#_*_ coding :utf_8 _*_
# 2017/08/03
# request test

import time,requests,json


t=5

def read():
    file=open("/sys/class/thermal/thermal_zone0/temp")
    temp=float(file.read())/1000
    file.close()
    return temp

def write(temp):
    file_1=open("/home/pi/Desktop/trmp",'a')
    file_1.write('\n'+'temp:'+str(temp))
    file_1.close()
    print 'temp:' ,temp ,'  write is ok'
    
def post(temp):
    api_url="http://127.0.0.1:1880/temp"
    api_headers={}
    payload={'value':temp}
    req=requests.post(api_url,api_headers,data=payload)

if __name__=='__main__':
    
    while(t):
        print 'all ready'
        temp=read()
        print 'read is ok'
        post(temp)
        print 'post is ok'
        write(temp)
        t-=1
        time.sleep(3)
        
