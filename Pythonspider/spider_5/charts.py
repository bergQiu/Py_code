# -*- coding:utf-8 -*-

from pyecharts import Bar
import json

if __name__ == '__main__':
	fs = open('result.json',encoding = 'utf-8')
	data = json.load(fs)
	# for k in data:
	# 	print('%s---%s'%(k,data[k]))
	# s_name,p_num = pyecharts.cast(data)
    #
	s_name = [key for key in data]
	p_num = [data[key] for key in data]

	bar = Bar("中科院院士省份分布统计")
	# # 主要方法，用于添加图表的数据和设置各种配置项
	bar.add("人数",s_name,p_num,is_stack=True)
	bar.add("人数", s_name, p_num, is_stack=True)
	bar.render("stackTrue.html")
	# print (s_name)
	# print(p_num)