# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 将爬虫文件传的数据，处理
# import json # 优化，dict转json,麻烦了些
# 第二种方法，将所有的json对象，存到Json数组中的
# from cryptography.hazmat.primitives.serialization import Encoding
# from scrapy.exporters import JsonItemExporter
#
# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open('duanzi.json','wb') # 以byte写入，也不需要指定编码
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False)
#         self.exporter.start_exporting()
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#     def open_splider(self,splider):
#         print('爬虫开始')
#     def close_splider(self, splider):
#         self.exporter.finish_exporting() # 这样就可以直接转JSON了
#         self.fp.closed()
#         print('爬虫结束了')

# 第三种方法，是按每个json对象写入，处理的，更方便，也不需要开始和结束
from scrapy.exporters import JsonLinesItemExporter

class QsbkPipeline(object):
    def __init__(self):
        self.fp = open('duanzi.json','wb') # 以byte写入，也不需要指定编码
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    def open_splider(self,splider):
        print('爬虫开始')
    def close_splider(self, splider):
        self.fp.closed()
        print('爬虫结束了')




