# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from SolidotSpider.items import SolidotspiderItem

class SolidotspiderPipeline(object):
    def __init__(self):
        # 链接数据库
        connection = pymongo.MongoClient(host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'])
        # 如果数据库需要账号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        db = connection[settings['MONGODB_DB']]  # 获得数据库的句柄
        self.post = db[settings['MONGODB_COLLECTION']]  # 获得collection的句柄

    def process_item(self, item, spider):
        self.post.insert(dict(item))
        return item
