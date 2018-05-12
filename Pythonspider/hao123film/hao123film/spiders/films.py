# -*- coding: utf-8 -*-
import scrapy
from hao123film.items import Hao123FilmItem
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class FilmsSpider(scrapy.Spider):
    name = 'films'
    allowed_domains = ['v.hao123.baidu.com/']
    base_url = "http://v.hao123.baidu.com/"
    num = 3
    start_urls = ['http://v.hao123.baidu.com/v/search?channel=movie']

    def parse(self, response):
        li = response.xpath(".//ul[@class='wg-c-list clearfix']/li")
        for each in li:
            url = each.xpath("./a/@href").extract()[0]
            # print(url)
            yield scrapy.Request(url,callback=self.parse_1,dont_filter=True)
        next_page =  self.base_url + response.xpath(".//a[@class='next-btn']/@href").extract()[0]
        self.num -= 1
        if self.num:
            yield scrapy.Request(url = next_page,callback=self.parse,dont_filter=True)


    def parse_1(self,response):
        # body = response.body.decode("utf-8")
        name = response.xpath(".//div[@class='info']//h1/@title").extract()[0]
        area = response.xpath(".//div[@class='info']/p/span[@monkey='area']/a/text()").extract()[0]
        era = response.xpath(".//div[@class='info']/p/span[@monkey='decade']/a/text()").extract()[0]
        score = response.xpath(".//div[@class='info']//span/text()").extract()[0]
        style  = ",".join(response.xpath(".//div[@class='info']/p/span[@monkey='category']/a/text()").extract())
        introduction = response.xpath(".//div[@class='info']/p[@class='abstract']/em/text()").extract()[0]
        image_url =  response.xpath(".//div[@class='poster']//img/@src").extract()[0]
        # print({"name":name,"area":area,"era":era,"score":score,"style":style,"introduction":introduction})
        item = Hao123FilmItem(name = name,area = area,era = era, score = score, style = style,introduction = introduction,image_url=image_url)
        yield item
        # pass

if __name__=="__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl("films")
    process.start()