# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Tutorial2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Youku(scrapy.Item):
    collection_name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    href = scrapy.Field()


class Youtube(scrapy.Item):
    search_flag = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    href = scrapy.Field()
