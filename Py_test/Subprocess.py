# coding:utf-8
# 2017/10/24
# subprocess test

import subprocess,time,os
'''
t=5
#subprocess.Popen('python /home/pi/Desktop/test00.py',shell=True)
os.system('python /home/pi/Desktop/test00.py')
#execfile('/home/pi/Desktop/test00.py')
'''

'''
while t:
    p=subprocess.check_output('ps -ef | grep -i python',shell=True)
    c=p.count('test00.py')
    print c
    t-=1
    time.sleep(1)
    '''
if __name__=='__main__':
    #subprocess.Popen('python /home/pi/Desktop/leak_detect/main.py',shell=True)
    order=subprocess.check_output('ps -ef | grep -i python',shell=True)
    count_1=order.count('sub.by')
    if count_1==3:
        exit()
    else:
        #os.system('python /home/pi/Desktop/leak_detect/main.py')       
        while True:
            time.sleep(1)
            order=subprocess.check_output('ps -ef | grep -i python',shell=True)
            count=order.count("test00.py")
            #print count
            if count==0:
                #p=subprocess.Popen('python /home/pi/Desktop/leak_detect/main.py',shell=True)
                os.system('python /home/pi/Desktop/test00.py')
                print 'test_sub is startting'
         
            



           
            
