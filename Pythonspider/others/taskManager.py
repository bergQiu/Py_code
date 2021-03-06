#! python3
# coding: utf-8

import queue,time
from multiprocessing.managers import BaseManager
from multiprocessing import  freeze_support

task_num = 10
task_queue = queue.Queue(task_num)
reslut_queue = queue.Queue(task_num)

def get_task():
    return task_queue
def get_result():
    return reslut_queue

class QueueManager(BaseManager):
    pass

def win_run():
    QueueManager.register('get_task_queue',callable = get_task)
    QueueManager.register('get_result_queue', callable = get_result)
    manager = QueueManager(address=('127.0.0.1',8003), authkey = b'qiye')
    manager.start()

    try:
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        for url in ['image_' + str(i) for i in range(10)]:
            print ('put task %s ...' % url)
            task.put(url)
        print ('try get result...')
        for i in range(10):
            print( 'result is %s' % result.get(timeout = 100))
    except:
        print('manager error')
    finally:
        manager.shutdown()


if __name__ == '__main__':
    freeze_support()
    win_run()







