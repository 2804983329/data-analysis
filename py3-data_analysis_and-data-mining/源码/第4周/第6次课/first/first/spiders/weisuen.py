# -*- coding: utf-8 -*-
import scrapy
from first.items import FirstItem
from scrapy.http import Request
class WeisuenSpider(scrapy.Spider):
    name = "weisuen"
    allowed_domains = ["baidu.com"]
    '''
    start_urls = (
        'http://www.baidu.com/',
    )
    '''
    def start_requests(self):
        ua={"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
        yield Request('http://www.qiushibaike.com/',headers=ua)
    def parse(self, response):
        item=FirstItem()
        item["content"]=response.xpath("/html/head/title/text()").extract()
        yield item