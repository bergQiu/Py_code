import scrapy

class TestSpider(scrapy.Spider):
    name = "test"
    #allowed_domains = ["baike.baidu.com"]
    start_urls = [
            "http://baike.baidu.com/search/word?猪八戒/"
            "http://baike.baidu.com/search/word?孙悟空/"
    ]

    def parse(self, response):
        #filename = "like"
        filename = response.url.split("/")[-2]
        #print(filename)
        with open( filename ,"w") as f:
            f.write(response.body)