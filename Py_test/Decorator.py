# coding:utf-8
# # 2018/05/08
# 測試裝飾器用法
# 閉包滿足的兩個條件：1、函數內部定義函數;2、包含對外部作用域而非全局作用域的引用
# 裝飾器：外部函數傳入被裝飾函數名，內部函數返回裝飾函數名
# 裝飾器特點：1、不修改被裝飾函數的調用方法;2、不修改被裝飾函數的源代碼


def outer(func):
    def inner():
        print("do something befor")
        func()
        print("do something after")
    return inner

@outer
def test():
    print("do something now")
# 不帶參數
# test()

def outer1(func):
    def inner(*args,**kwargs):
        print(kwargs)
        print("do something befor")
        func(*args,**kwargs)
        print("do something after")
    return inner

@outer1
def test1(*args,**kwargs):
    print(args)
    print("do %s something %s now"%(kwargs['a'],kwargs['b']))

# 帶參數
# test1("OOO",a="aaa",b="bbb")

def outer2(func):
    def inner(*args,**kwargs):
        print("do something befor")
        res = func(*args,**kwargs)
        print("do something after")
        return res
    return inner

@outer1
def test2(*args,**kwargs):
    print("do %s something %s now"%(kwargs['a'],kwargs['b']))
    return 1
# 有返回值
# test2("OOO",a="aaa",b="bbb")