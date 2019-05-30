# -*- coding: utf-8 -*-
#！/usr/bin/python2
# 2017/10/24
# 漏水檢測

import time,datetime,json,thread,subprocess
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import fun


#######################################

fs=open("/home/pi/Desktop/leak_detect/config.json")
d1=fs.read()
d2=json.loads(d1)
broker=str(d2['MQTT']['broker'])
port=d2['MQTT']['port']
LS_topic=str(d2['MQTT']['LS_topic'])
HEART_topic=str(d2['MQTT']['HEART_topic'])
#SID=d2['MQTT']['SID']
#print broker,port,LS_topic,HEART_topic,SID
#print type(broker)
fs.close()

#########################################

GPIO.setmode(GPIO.BCM)

pins=[4,22,27,17,5,6,26,25,24,23]
prev=[0,0,0,0,0,0,0,0,0,0]
data={}

def  pin_init():
    for pin in pins:
        GPIO.setup(pin,GPIO.IN)

def data_init():
    for pin in pins:
        data[pin]={'value':0,'time':0}
    
def heartbeat():
    MQ_1=mqtt.Client()
    MQ_1.connect(broker,port)
    SID={'SID':'S170830'}
    while True:
        MQ_1.publish(HEART_topic,json.dumps(SID))
        #print SID
        time.sleep(1)

def check_py():
    global count
    ps=subprocess.check_output('ps -ef | grep -i python',shell=True)
    count=ps.count('getvalue.py')
    return
####################################################
        
if __name__=='__main__':
    
    sun=0
    _str="Leak.py"
    sun=fun.checkPy(_str)
    if sun>=2:
        exit()
    else:
        pin_init()
        data_init() 
        try:
            thread.start_new_thread(heartbeat,())
        except:
            print "Error:unable to start thread"
        #send_data({'change':0,'data':'I am alive'})  
        change=1
        MQ=mqtt.Client()
        MQ.connect(broker,port)
        while True:
            for pin in pins:
                curr=GPIO.input(pin)
                x=pins.index(pin)
                if prev[x]!=curr:
                    prev[x]=curr
                    data[pin]={'value':curr,'UpdateTime':str(datetime.datetime.now())}
                    change=change+1
            MQ.publish(LS_topic,json.dumps({'change':change,'data':data}))
            if change!=0:
                print data
            change=0
            time.sleep(1)
        
  

      
       
            


            
            
