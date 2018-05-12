# coding:utf-8
# taskmanager
# import queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support,Process,Queue
from URLManager import  UrlManager
from DataOutput import Dataoutput
import time


class nodeManager(object):
    def __init__(self,url_q,result_q,store_q,conn_q):
        self.url_q = url_q
        self.store_q = store_q
        self.conn_q = conn_q
        self.result_q = result_q
        pass

    def get_task(self):
        return self.url_q

    def get_result(self):
        return self.result_q

    def start_Manager(self):#分布式管理器
        BaseManager.register("get_task_queue",callable= self.get_task)
        BaseManager.register("get_result_queue",callable= self.get_result)
        manager =BaseManager(address=("127.0.0.1",8001),authkey =  b"baike")
        return manager

    def url_manager_proc(self,url_q,conn_q,root_url):
        url_manager = UrlManager()
        url_manager.add_new_url(root_url)
        while True:
            while url_manager.has_new_url():
                new_url = url_manager.get_new_url()
                print("url "+ new_url)
                url_q.put(new_url)
                # print("old_url=",url_manager.old_url_size())
                if url_manager.old_url_size()>2000:
                    url_q.put("end")
                    print("控制节点发起结束通知!")
                    url_manager.save_progress("new_urls.txt",url_manager.new_urls)
                    url_manager.save_progress("old_urls.txt",url_manager.old_urls)
                    return
            try:
                if not conn_q.empty():
                    urls = conn_q.get()
                    # print(urls)
                    url_manager.add_new_urls(urls)
            except BaseException:
                time.sleep(0.1)

    def result_solve_proc(self,result_q,conn_q,store_q):
        while True:
            try:
                if not result_q.empty():
                    content = result_q.get(True)
                    print("result "+ content)
                    if content["new_urls"] == "end":
                        print("结果分析进程接收到通知然后结束！")
                        store_q.put("end")
                        return
                    conn_q.put(content["new_urls"])
                    store_q.put(content["data"])
                else:
                    # print("result_q is empty")
                    time.sleep(0.1)
            except BaseException:
                time.sleep(0.1)

    def store_proc(self,store_q):
        output = Dataoutput()
        while True:
            if not store_q.empty():
                data = store_q.get()
                # print(data)
                if data == "end":
                    print("储存进程接收到通知然后结束！")
                    # output.store_data()
                    return
                output.store_data(data)
            else:
                # print("store_q is empty")
                time.sleep(0.1)

if __name__ == "__main__":
    # 初始化4个队列
    url_q = Queue(10)
    store_q = Queue(10)
    conn_q = Queue(10)
    result_q = Queue(10)
    node  =  nodeManager(url_q,result_q,store_q,conn_q)
    manager = node.start_Manager()
    url_manager_proc = Process(target = node.url_manager_proc,args = (url_q,conn_q,"http://baike.baidu.com/view/284853.htm",))
    result_solve_proc = Process(target = node.result_solve_proc,args = (result_q,conn_q,store_q,))
    store_proc = Process(target = node.store_proc,args = (store_q,))
    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()
    manager.get_server().serve_forever()








