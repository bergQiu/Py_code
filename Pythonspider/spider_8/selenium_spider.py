# -*- coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs
import time
import datetime

class qunaspider(object):

    def get_hotel(self,driver,to_city,fromdate,todate):
        ele_tocity = driver.find_element_by_name("toCity")
        ele_fromdate = driver.find_element_by_id("fromDate")
        ele_todate = driver.find_element_by_id("toDate")
        ele_search = driver.find_element_by_class_name("search-btn")
        ele_tocity.clear()
        ele_tocity.send_keys(to_city)
        # ele_tocity.click()
        ele_fromdate.clear()
        ele_fromdate.send_keys(fromdate)
        ele_todate.clear()
        ele_todate.send_keys(todate)
        ele_search.click()
        page_num = 0
        while True:
            try:
                WebDriverWait(driver,10).until(
                    #C.title_contains(unicode(to_city))
                    EC.title_contains(to_city)
                )
            except Exception as e:
                print (e)
                break

            js = "window.scrollTo(0,document.body.scrollHeight);"
            driver.execute_script(js)
            time.sleep(5)

            htm_const = driver.page_source
            print(htm_const)
            exit()
            print("END")
            soup = BeautifulSoup(htm_const,"html.parser",from_encoding="utf-8")
            infos = soup.find_all(class_="item_hotel_info")
            f = codecs.open(to_city + fromdate + u".html" ,"a","utf-8")
            for info in infos:
                f.write(str(page_num)+"--"*50)
                content = info.get_text().replace("","").replace("\t","").strip()
                for line in [ln for ln in content.splitlines() if ln.strip()]:
                    f.write(line)
                    f.write("\r\n")
            f.close()
            try:
                next_page = WebDriverWait(driver,10).until(
                    EC.visibility_of(driver.find_element_by_css_selector(".item.next"))
                )
                next_page.click()
                page_num+=1
                time.sleep(10)
            except Exception as e:
                print(e)
                break

    def craw(self,root_url,to_city):
        today =datetime.date.today().strftime("%Y-%m-%d")
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        tomorrow =tomorrow.strftime("%Y-%m-%d")
        driver = webdriver.Chrome(executable_path="C:\\Users\QZL\AppData\Local\Google\Chrome\Application\chormedirver\chromedriver.exe")
        driver.set_page_load_timeout(50)
        driver.get(root_url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        self.get_hotel(driver,to_city,today,tomorrow)


if __name__=="__main__":
    spider = qunaspider()
-    spider.craw("http://hotel.qunar.com/",u"上海")









