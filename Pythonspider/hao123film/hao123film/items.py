# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Hao123FilmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    area = scrapy.Field()
    era = scrapy.Field()
    score = scrapy.Field()
    style = scrapy.Field()
    introduction = scrapy.Field()
    image_url = scrapy.Field()
    pass
