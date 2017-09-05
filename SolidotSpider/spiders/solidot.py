# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy import Request
from SolidotSpider.items import SolidotspiderItem

class SolidotSpider(scrapy.Spider):
    name = "solidot"
    allowed_domains = ["www.solidot.org"]
    start_urls = 'http://www.solidot.org/'

    def start_requests(self):
        for i in range(1, 10):
            for m in range(1, 32):
                if m < 10:
                    times = '20170' + str(i) + '0' + str(m)
                else:
                    times = '20170' + str(i) + str(m)
                start_urls = self.start_urls + '?issue=' + str(times)
                yield Request(start_urls, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        tds = soup.find_all('div', 'block_m')
        item = SolidotspiderItem()
        for td in tds:
            item['article_title'] = str(td.find_all('a')[0].get_text()) + '--' + str(td.find_all('a')[1].get_text())
            genre = td.find_all('a')[0].get_text()
            if len(genre) == 2:
                item['article_genre'] = genre
            time = td.find('div', 'talk_time').get_text().split()
            item['article_time'] = str(time[1]) + str(time[2])
            item['article_author'] = time[0]
            item['article_brief'] = td.find('div', 'p_mainnew').get_text()
            yield item



