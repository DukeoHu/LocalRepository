import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request #request模块，需要跟进url
from Novels.items import NovelsItem#导入刚才定义好的字段

class Myspider(scrapy.Spider):
    name = 'Novels'
    bash_url = 'http://www.x23us.com'
    bashurl = '.html'

    def start_requests(self):
        yield Request('http://www.x23us.com/quanben/1', self.parse)
    def parse(self, response):
        max_num = BeautifulSoup(response.text, 'lxml').find('div', class_='pagelink').find_all('a')[-1].get_text()#获取最大页码
        for num in range(1, int(max_num)):
            url = self.bash_url + '/quanben/' + str(num)
            print(url)
            yield Request(url, callback=self.get_name)

    def get_name(self, response):
        tds = BeautifulSoup(response.text, 'html.parser').find_all('tr', bgcolor='#FFFFFF')
        for td in tds:
            novel_name = td.find_all('a')[1].get_text() #1
            novel_url = td.find('a')['href']
            novel_author = td.find_all('td')[2].get_text() #2
            novel_num = td.find_all('td')[-3].get_text() #-3
            novel_status = td.find_all('td')[-1].get_text() #-1
            yield Request(novel_url, callback=self.get_chapterurl, meta={'novel_name':novel_name,
                                                                         'novel_url':novel_url,
                                                                         'novel_author':novel_author,
                                                                         'novel_num':novel_num,
                                                                         'novel_status':novel_status})

    def get_chapterurl(self, response):
        item = NovelsItem()
        print(response.meta)
        brief = BeautifulSoup(response.text, 'lxml').find('div', class_='bdsub').find_all('dd')[3].find_all('p')[1].get_text()#####
        item['novel_name'] = str(response.meta['novel_name'])
        item['novel_url'] = str(response.meta['novel_url'])
        item['novel_author'] = str(response.meta['novel_author'])
        item['novel_num'] = str(response.meta['novel_num'])
        item['novel_status'] = str(response.meta['novel_status'])
        item['novel_brief'] = brief
        return item


