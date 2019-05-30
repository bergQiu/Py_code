# coding:utf-8
# 2018/01/03
# Mssql test

import pymssql

conn = pymssql.connect(host ="minerva",user = "sa",password = "00",database = "Berg_DB")

cur = conn.cursor()

name = "berg.qiu"
password = "960876"
enable = False

if cur :
    try:
        print("connect successful!")
        sqlStr = "select * from login where name_ = '" + name + "' and password_ = '" +password + "'"
        # sqlStr = "select * from berg_test "
        # sqlStr +="where name='"+ name +"'"
        # print(sqlStr)
        cur.execute(sqlStr)
        # result = cur.fetchall()
        result = cur.fetchone()
        print (result[1])
        print(result[0])
        # print("%s  %s"%(result[1],result[2]))
        if result:
            if name == result[1] and  pwd == str(result[2]):
                print (result[1])
                print(result[2])
                enable = True  
        if enable:
            print("A")
        else:
            print("B")
        print(type(result))
        for i,(id,name,age,sex) in enumerate(result):
            print('第 '+str(i+1)+' 行记录->>> '+ str(id) +':'+ str(name)+ ':' + str(age) + ":" + str(sex) )

    except:
        print("There are some problems here")

cur.close()