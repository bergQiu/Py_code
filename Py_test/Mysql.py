# -*-conding:utf-8-*-
# 2018/05/29
# mysql connect test

import pymysql

if __name__ == "__main__":
    # passwd = 'YWRtaW5fNDQwNw'
    db = pymysql.connect(host = '10.10.1.182', port = 4408, user = 'root', passwd = 'YWRtaW5fNDQwNw', db = 'test', charset="utf8") 
    cursor = db.cursor()
    sql_str = "select * from test" 
    cursor.execute(sql_str)
    data = cursor.fetchone()
    print data  

