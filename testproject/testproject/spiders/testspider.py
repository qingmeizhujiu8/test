# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TestprojectItem


class TestspiderSpider(CrawlSpider):
    name = 'testspider'
    allowed_domains = ['wz.sun0769.com']
    offset = 0
    url = 'http://wz.sun0769.com/index.php/question/report?page=' + str(offset)
    start_urls = [url]

    def parse(self, response):
        link_list = response.xpath("//a[@class='news14']/@href").extract()
        for each in link_list:
            # 对每页的帖子发送请求，获取帖子内容里面指定数据返回给管道文件
            yield scrapy.Request(each, callback=self.deal_link)
        self.offset += 30
        if self.offset <= 124260:
            url = 'http://wz.sun0769.com/index.php/question/report?page=' + str(self.offset)
            # 对指定分页发送请求，响应交给parse函数处理
            yield scrapy.Request(url, callback=self.parse)

    # 从每个分页帖子内容获取数据，返回给管道
    def deal_link(self, response):
        item = TestprojectItem()
        item['url'] = response.url
        item['title'] = response.xpath("//div[@class='pagecenter p3']//strong[@class='tgray14']/text()").extract()[0]
        item['number'] = \
        response.xpath("//div[@class='pagecenter p3']//strong[@class='tgray14']/text()").extract()[0].split(' ')[
            -1].split(':')[-1]

        if len(response.xpath("//div[@class='contentext']")) == 0:
            item['content'] = ''.join(response.xpath("//div[@class='c1 text14_2']/text()").extract())
        else:
            item['content'] = ''.join(response.xpath("//div[@class='contentext']/text()").extract())
        yield item

