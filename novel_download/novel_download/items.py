# -*- coding: utf-8 -*-
import scrapy

class DownloadItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
