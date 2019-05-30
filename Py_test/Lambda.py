# coding:utf-8
# 2018/04/13
# Lambda test

data = {}
data["NUM"] = True
f = data["NUM"]
t = lambda f:f if f else ""
print(t(data["NUM"]))
