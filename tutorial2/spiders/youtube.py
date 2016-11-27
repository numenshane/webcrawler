import scrapy
from scrapy.spider import Spider
from tutorial2.items import Youtube
import re
import chardet


class YoutubeSpider(Spider):
    name = "youtube"

    def __init__(self, search_flag=None, *args, **kwargs):
        self.index=0
        super(YoutubeSpider, self).__init__(*args, **kwargs)
        print chardet.detect(search_flag)['encoding']
        if re.search('ascii', chardet.detect(search_flag)['encoding']):
            self.search_flag = search_flag
        else:
            self.search_flag = unicode(search_flag, 'gbk').encode('utf-8')

        self.start_urls = [
            "https://www.youtube.com/results?search_query=%s" % self.search_flag
        ]
        self.allowed_domains = ["youtube.com"]

    def parse(self, response):
        self.index = self.index + 1

        quotes = scrapy.Selector(response)
        youtubeItem = Youtube()
        for quote in quotes.css('div.yt-lockup-content'):
            #id = quote.xpath('.//@data-sessionlink').extract()[0].encode('utf-8')
            name = quote.xpath('.//@title').extract()[0].encode('utf-8')
            href = "http://www.youtube.com" + quote.xpath('.//@href').extract()[0].encode('utf-8')
            id = quote.xpath('.//@href').extract()[0].encode('utf-8').split('/')[1]
            print id,name,href
            # if re.search(self.search_flag, name):
            #     print '%s,%s' % (name, href)
            youtubeItem['id'] = id
            youtubeItem['name'] = name
            youtubeItem['href'] = href
            youtubeItem['search_flag'] = self.search_flag
            yield youtubeItem

        nextPage = quotes.xpath('//*[@id="content"]/div/div/div/div[1]/div/div[2]/div[2]/a[7]/@href').extract()[0]
        print nextPage
        print self.index
        if nextPage is not None:
            nextPage = quotes.response.urljoin(nextPage)
            yield scrapy.Request(nextPage, callback=self.parse, dont_filter=True)
