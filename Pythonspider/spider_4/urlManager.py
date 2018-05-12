# coding:utf-8

class urlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        return self.new_urls != 0

    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,url):
        if url is None or len(url) == 0:
            return
        for url in url:
            self.add_new_url(url)


    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return  new_url

    def new_urls_size(self):
        return len(self.new_urls)

    def old_urls_size(self):
        return len(self.old_urls)

