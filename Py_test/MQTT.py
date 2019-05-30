# coding:utf-8
# 2017/11/23
# MQTT消息隊列測試

import paho.mqtt.client as mqtt
import time,datetime
import json
import threading

class mqThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        self.doRun = True
        print(self.name + " start\n")
        while self.doRun:
            try:
                print(datetime.datetime.now().isoformat())
                client.connect("10.9.232.7", 1883)
            except:
                print(datetime.datetime.now().isoformat())
                print("connect fail")
                pass
            time.sleep(3*60)
                

    def stop(self):
        self.doRun = False
        print(self.name + " stop\n")

class heartThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        self.doRun = True
        print(self.name + " start\n")
        while self.doRun:
            try:
                client.publish("topic_test",json.dumps(SID))
                time.sleep(1)
            except:
                print("send heart fail")
                
    def stop(self):
        self.doRun = False
        print(self.name + " stop\n")


def on_connect(client, userdate, flags, rc):
    print("connect to server" + str(userdata))

def on_message(client, userdata, msg):
    print("receive msg: " + str(msg.payload))

client = mqtt.Client(client_id="smsCat", clean_session=True)
client.on_connect = on_connect
client.on_message = on_message

client.reconnect_delay_set(1,20)

SID = {"SID":"S0002"}

try:
    threadMQ = mqThread(1,"Thread-MQ",1)
except:
    print("open MQ thread fail")
threadMQ.start()

try:
    threadHeart = heartThread(1,"Thread-Heart",1)
except:
    print("open Heart thread fail")
threadHeart.start()

