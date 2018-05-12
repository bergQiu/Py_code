# -*- coding:utf-8 -*-

from pyecharts import Bar
import json,random

if __name__ == '__main__':
	fs = open('result.json',encoding = 'utf-8')
	data = json.load(fs)
	# for k in data:
	# 	print('%s---%s'%(k,data[k]))
	# s_name,p_num = pyecharts.cast(data)
    #
	#  Bar 柱形图堆叠显示  is_stack = True
	# s_name = [key for key in data]
	# p_num = [data[key] for key in data]
	# p_num_ = [data[key] for key in data]
    #
	# bar = Bar("中科院院士省份分布统计")
	# # 主要方法，用于添加图表的数据和设置各种配置项
	#  Bar 柱形图堆叠显示  is_stack = True
	# bar.add("人数",s_name,p_num,is_stack=True)
	# bar.add("人数_", s_name, p_num_, is_stack=True)
	# bar.render("stackTrue.html")

	# 标记线和标记点实例
	# bar.add("人数", s_name, p_num,mark_point=["average"])
	# bar.add("人数_", s_name, p_num_,mark_line=["max","min"])
	# bar.render("stackTrue.html")

	# x,y轴交换 is_convert =  True
	# bar.add("人数", s_name, p_num)
	# bar.add("人数_", s_name, p_num_,is_convert  = True)
	# bar.render("stackTrue.html")

	# Bar - datazoom - slider 示例
	attr = ["{}天".format(i) for i in range(30)]
	v1 = [random.randint(1, 30) for _ in range(30)]
	print(v1)
	bar = Bar("Bar - datazoom - slider 示例")
	bar.add("", attr, v1, is_label_show=True, is_datazoom_show=True)
	bar.render("stackTrue.html")
