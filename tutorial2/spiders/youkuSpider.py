# -*- coding: utf-8 -*-
#encoding=utf-8
import scrapy
from scrapy.spider import Spider
from tutorial2.items import Youku
import chardet
import re
import sys

class YoukuSpider(Spider):

    name = "youku"

    def __init__(self, search_flag=None, collection_name=None, *args, **kwargs):
        super(YoukuSpider, self).__init__(*args, **kwargs)

        print search_flag
        self.search_flag = search_flag
        print chardet.detect(self.search_flag)
        if re.search('ascii', chardet.detect(search_flag)['encoding']) \
                or re.search('utf-8',chardet.detect(search_flag['encoding'])):
            self.search_flag = search_flag
        else:
            self.search_flag = unicode(search_flag, chardet.detect(search_flag)['encoding']).encode('utf-8')
        self.start_urls = [
            "http://www.soku.com/search_video/q_%s?" % self.search_flag
        ]
        self.allowed_domains = ["soku.com"]
        self.collection_name = unicode(collection_name, "gbk").encode('utf-8')
        self.index = 0

    def parse(self, response):
        self.index = self.index + 1
        quotes = scrapy.Selector(response)
        youkuItem = Youku()
        for quote in quotes.css('div.v-link'):
            name = quote.xpath('.//@title').extract()[0]
            href = quote.xpath('.//@href').extract()[0]
            id = href.split('?')[0].split('/')[-1].split('.')[0]
            youkuItem['id'] = id
            youkuItem['name'] = name
            youkuItem['href'] = href
            youkuItem['collection_name'] = self.collection_name
            yield youkuItem

        nextPage = quotes.css('li.next a::attr(href)').extract_first()
        print self.index
        if nextPage is not None:
            nextPage = quotes.response.urljoin(nextPage)
            yield scrapy.Request(nextPage, callback=self.parse, dont_filter=True)
