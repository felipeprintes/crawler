# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import io

class Lenotg1Pipeline(object):
    def open_spider(self, spider):
    	self.file = io.open('arq.csv', 'w', encoding='utf8')

    def close_spider(self,spider):
    	self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
