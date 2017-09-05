# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SolidotspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    article_genre = scrapy.Field()
    article_title = scrapy.Field()
    article_time = scrapy.Field()
    article_brief = scrapy.Field()
    article_author = scrapy.Field()
