# -*- coding:utf-8 -*-

'''
    遞歸測試
'''

def f(x,y):
    if x>0 and y>0:
        return f(x-1,y) + f(x,y-1)
    else:
        return x+y

if __name__ == "__main__":
    # print f(2,1)
    i = '1.0'
    print(float(i))
    print(type(float(i)))