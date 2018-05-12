#! python3
# coding: utf-8

import time
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

print ('Connect on 127.0.0.1 ...')
worker = QueueManager(address = ('127.0.0.1',8003),authkey = b'qiye')
worker.connect()

task = worker.get_task_queue()
result = worker.get_result_queue()

print(type(result))

while (not task.empty()):
    imager_url =  task.get(True,timeout = 5)
    print ('run task download %s ...'%imager_url)
    #print (type(imager_url))
    time.sleep(1)
    result.put('%s ------>> successful '%imager_url)

print('worker exit...')







