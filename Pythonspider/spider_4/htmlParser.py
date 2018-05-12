# coding:utf-8
import lxml,re,urllib
from bs4 import BeautifulSoup

class htmlParser(object):

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        # print(html_cont)
        soup = BeautifulSoup(html_cont,"lxml")
        new_urls = self._get_new_urls(page_url,soup)
        new_datas = self._get_new_data(page_url,soup)
        return new_urls,new_datas

    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        # print(type(new_urls))
        # print(soup.content)
        # print(soup.find_all("a"))
        links = soup.find_all("a",href = re.compile(r"/item/.+\d+$"))
        # print(links)
        for link in links:
            new_url = link.get("href")
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        # print(new_urls)
        return  new_urls

    def _get_new_data(self,page_url,soup):
        new_datas = {}
        new_datas["url"] = page_url
        # print (soup.find("dd",class_ = "lemmaWgt-lemmaTitle-title"))
        title = soup.find("dd",class_ = "lemmaWgt-lemmaTitle-title").find("h1")
        new_datas["title"] = title.get_text()
        summary = soup.find("div",class_ = "lemma-summary")
        # Str = summary.text.strip().strip("\n")
        new_datas["summary"] = summary.text.strip().strip("\n")
        # print(new_datas)
        return new_datas