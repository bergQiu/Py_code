# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['http://baidu.com']
    start_urls = ['http://http://baidu.com/']

    def parse(self, response):
        pass
