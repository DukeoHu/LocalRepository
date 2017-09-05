# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    novel_name = scrapy.Field()
    novel_brief = scrapy.Field()
    novel_author = scrapy.Field()
    novel_num = scrapy.Field()
    novel_url = scrapy.Field()
    novel_status = scrapy.Field()
