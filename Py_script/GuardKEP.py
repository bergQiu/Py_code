# coding:utf-8
# 2018/02/07
# demo mqtt ,消息隊列mq測試,守護KepServer進程

import paho.mqtt.client as mqtt
import time,threading,datetime,os

class myThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect("10.10.0.96",1883,60)
        client.loop_forever()

    #連接成功回調函數
    def on_connect(self,client,userdata,flags,rc):
        print("connected with result code  " + str(rc))
        client.subscribe("testforKEP")
    #消息推送回調函數
    def on_message(self,client,userdata,msg):
        global time_
        time_ = time.time()
        print(msg.topic + ":"+str(msg.payload))

def judgeTime(time_):
    if time.time() - time_ >10:
        print(str(datetime.datetime.now())[:len(str(datetime.datetime.now()))-7]+"  KEPServerEXV6 is shut down")
        return True
    # else:
    #     return False

def control():
    os.system("net stop KEPServerEXV6 ")
    time.sleep(5)
    os.system("net start KEPServerEXV6")

if __name__ == "__main__":
    # global time_
    time_ = time.time()
    mq = myThread()
    mq.setDaemon(True)
    mq.start()
    while True:
        while judgeTime(time_):
            control()
            time_ = time.time()
            break
        time.sleep(2)
    