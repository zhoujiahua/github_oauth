#! /usr/bin/python3
from urllib import request


class Spider:
    # url = 'https://www.douyu.com/g_LOL'
    # url = 'https://www.douyu.com/japi/search/api/getHotList'
    url = 'http://news.baidu.com/'
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        print(htmls)


    def go(self):
        self.__fetch_content()


spider = Spider()
spider.go()