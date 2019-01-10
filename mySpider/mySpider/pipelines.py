# -*- coding: utf-8 -*-
import json
import codecs

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    def __init__(self):
        self.file = codecs.open('paper.txt', 'w', 'utf-8')
    def process_item(self, item, spider):
        if item['date']:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.file.write(line)
            return item
