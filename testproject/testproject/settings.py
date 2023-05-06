# -*- coding: utf-8 -*-
BOT_NAME = 'testproject'
SPIDER_MODULES = ['testproject.spiders']
NEWSPIDER_MODULE = 'testproject.spiders'
# log日志文件默认保存在当前目录，下面为日志级别，当大于或等于INFO时将被保存
LOG_FILE = 'dongguan.log'
LOG_LEVEL = 'INFO'
# 爬取深度设置
# DEPTH_LIMIT = 1
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dongguan (+http://www.yourdomain.com)'
# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
  'testproject.pipelines.TestprojectPipeline': 300,
}
