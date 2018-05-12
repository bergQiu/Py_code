# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time

driver = webdriver.Chrome()
driver.get("http://baidu.com")
assert u"百度" in driver.title
elem = driver.find_element_by_name("wd")
elem.clear()
elem.send_keys(u"孙悟空")
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert u"孙悟空" not in driver.page_source
driver.close()
