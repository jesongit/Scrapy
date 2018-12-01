# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NovelDownloadPipeline(object):

    def process_item(self, item, spider):
        path = 'novel\\'
        title = item['title']
        content = item['content']
        filename = path + title + '.txt'
        with open(filename, 'w', encoding = 'utf-8') as f:
            f.write(content)
