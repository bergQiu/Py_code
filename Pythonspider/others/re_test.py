# coding:utf-8
import re,lxml,time


result_ = {}
# result = [{'name': '郭华东', 'province': '江苏'}, {'name': '宋振骐', 'province': '湖北'}, {'name': '陈大可', 'province': '湖南'}, {'name': '房建成', 'province': '山东'}, {'name': '莫毅明', 'province': '香港'}, {'name': '刘永坦', 'province': '江苏'}, {'name': '殷鸿福', 'province': '浙江'}, {'name': '常印佛', 'province': '江苏'}, {'name': '朱森元', 'province': '江苏'}, {'name': '张宏福', 'province': '陕西'}]
# str = "半导体材料物理学家。河南省镇平人。1962年毕业于南开大学物理系。中国科学院半导体所研究员。1995年当选为中国科学院院士。有机化学家 "
# Str = r" 1948年12月11日生于湖北汉口，籍贯河南淇县。1971年毕业于台湾新竹清华大学化学系。1975年获美国纽约州立大学石溪分校博士学位。清华大学化学系教授，生命有机磷化学及化学生物学教育部重点实验"
# pattern = re.compile(r'([,|。].+省.+人)|([年|月|日|.|,|。][出生|生于].{5})')
# #result = re.match(pattern, Str)
# result = re.search(pattern, Str)
# # result = re.split(pattern, Str)
# print (result.group())
# #print (result.group())
#
result =[{'name': '刘明', 'province': '江西'}, {'name': '郑耀宗', 'province': '香港'}, {'name': '戴汝为', 'province': '云南'}, {'name': '沈其韩', 'province': '江苏'}, {'name': '丁国瑜', 'province': '河北'}, {'name': '杨焕明', 'province': '浙江'}, {'name': '陈晓非', 'province': '辽宁'}, {'name': '金展鹏', 'province': '广西'}, {'name': '安立佳', 'province': '吉林'}, {'name': '冯士筰', 'province': '天津'}, {'name': '徐叙瑢', 'province': '山东'}, {'name': '王启明', 'province': '福建'}, {'name': '张殿琳', 'province': '陕西'}, {'name': '朱静', 'province': '上海'}, {'name': '彭孝军', 'province': '湖南'}, {'name': '赵东元', 'province': '辽宁'}, {'name': '吴硕贤', 'province': '福建'}, {'name': '陶瑞宝', 'province': '上海'}, {'name': '陈创天', 'province': '浙江'}, {'name': '刘颂豪', 'province': '广东'}, {'name': '李永舫', 'province': '重庆'}, {'name': '曲钦岳', 'province': '山东'}, {'name': '陈文新', 'province': '湖南'}, {'name': '桂建芳', 'province': '湖北'}, {'name': '丁奎岭', 'province': '河南'}, {'name': '周又元', 'province': '上海'}, {'name': '孙儒泳', 'province': '浙江'}, {'name': '徐如人', 'province': '浙江'}, {'name': '李安民', 'province': '重庆'}, {'name': '李吉均', 'province': '四川'}, {'name': '胡海岩', 'province': '上海'}, {'name': '汤涛', 'province': '安徽'}, {'name': '林其谁', 'province': '福建'}, {'name': '杨学明', 'province': '浙江'}, {'name': '赵进东', 'province': '江苏'}, {'name': '张仁和', 'province': '重庆'}, {'name': '解思深', 'province': '山东'}, None, {'name': '陈凯先', 'province': '重庆'}, {'name': '钱逸泰', 'province': '江苏'}, {'name': '郑建华', 'province': '吉林'}, {'name': '舒红兵', 'province': '重庆'}, {'name': '邢定钰', 'province': '上海'}, {'name': '潘建伟', 'province': '浙江'}, {'name': '刘丛强', 'province': '贵州'}, {'name': '周秀骥', 'province': '江苏'}, {'name': '管晓宏', 'province': '四川'}, {'name': '曹春晓', 'province': '浙江'}, {'name': '王鼎盛', 'province': '重庆'}, {'name': '任詠华', 'province': '香港'}]
for data in result:
    print(data["province"])
    if data["province"] not in result_:
        result_[data["province"]] = 1
    else:
        result_[data["province"]] += 1
    time.sleep(2)

# print ("rl" in result_)
# # result_["ello"] = 123
print(result_)