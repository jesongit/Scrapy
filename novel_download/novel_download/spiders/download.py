# -*- coding: utf-8 -*-
import re
import scrapy
from novel_download.items import DownloadItem

class DownloadSpider(scrapy.Spider):
    name = 'download'
    start_urls = ['https://www.bequge.com/42_42237/',]

    def clean(self, str):
        str = re.sub(u'[\u3000, \xa0]', '', str).replace(' ', '').replace('\r', '')
        return str

    def parse(self, response):
        for a in response.xpath('//dd/a')[13:15]:
            #print(a)
            yield response.follow(a, self.parse_content)

    def parse_content(self, response):

        title = response.xpath('//*[@class="bookname"]/h1/text()').extract()[0]
        content = response.xpath('//*[@id="content"]/text()').extract()
        content = title + '\n' + self.clean(''.join(content)) + '\n'

        item = DownloadItem()
        item['title'] = title
        item['content'] = content
        yield item