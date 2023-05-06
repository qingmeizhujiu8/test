# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# -*- coding: utf-8 -*-
import json
import codecs


class TestprojectPipeline:
    def __init__(self):
        print('2 管道初始化')
        # 使用codecs写文件，直接设置文件内容编码格式，省去每次都要对内容进行编码
        self.file = codecs.open('newdongguan.json', 'w', encoding='utf-8')
        # 以前文件写法
        # self.file = open('newdongguan.json','w')

    def process_item(self, item, spider):
        print('3 创建文件并写入')
        print(item['title'])
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        # 以前文件写法
        # self.file.write(content.encode('utf-8'))
        self.file.write(content)
        return item

    def close_spider(self):
        print('5 文件关闭')
        self.file.close()
    # def __init__(self):
    #     print('2 管道初始化')
    #     self.file = open('guangzhou.json', 'w')
    #
    # def process_item(self, item, spider):
    #     print('3 创建文件并写入')
    #     content = json.dumps(dict(item), ensure_ascii=False).encode('utf-8') + '\n'
    #     self.file.write(content)
    #     return item
    #
    # def closespider(self):
    #     print('5 文件关闭')
    #     self.file.close()
