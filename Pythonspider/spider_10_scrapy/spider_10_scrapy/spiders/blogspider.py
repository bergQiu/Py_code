# coding:utf-8

import scrapy
# from items import Spider10ScrapyItem
from spider_10_scrapy.items import  Spider10ScrapyItem
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.shell import inspect_response

class blogsSpider(scrapy.Spider):
    name = "blogs"
    allowed_domains = ["cnblogs.com"]
    # 入口URL
    start_urls = ["http://www.cnblogs.com/qiyeboy/default.html?page=1"]

    def parse(self, response):
        # 解析Response
        papers = response.xpath(".//*[@class='day']")
        print("start parse")
        for paper in papers:
            inspect_response(response, self)
            url  = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postCon']/div/text()").extract()[0]
            # content = paper.xpath(".//*[@class='c_b_p_esc']/a/text()").extract()[0]
            item = Spider10ScrapyItem(url=url,title=title,time=time,content=content)
            request = scrapy.Request(url=url,callback=self.parse_body)
            request.meta['item'] = item
            yield  request
            # yield item
            # print (url,title,time,content)
        next_page = scrapy.Selector(response).re(u'<a href="(\S*)">下一页</a>')
        if next_page:
            scrapy.Request(url=next_page[0],callback=self.parse)
        # pass

    def parse_body(self,response):
        item = response.meta['item']
        body = response.xpath(".//*[@class='postBody']")
        item['cimage_urls'] = body.xpath('.//img//@src').extract()
        yield item

if __name__=="__main__":
    # 方法一
    # process = CrawlerProcess({
    #     "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    # })
    # process = CrawlerProcess(get_project_settings())
    # 方法二
    process = CrawlerProcess(get_project_settings())
    process.crawl("blogs")
    process.start()














