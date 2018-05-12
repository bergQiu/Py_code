# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import  CrawlerProcess
from scrapy.utils.project import get_project_settings


class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['music.163.com/']
    start_urls = ['http://music.163.com//']

    def parse(self, response):
        pass


if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('music')
    process.start()