# -*- coding: utf-8 -*-
import scrapy
from first.items import FirstItem
from scrapy.http import Request

class QsbkSpider(scrapy.Spider):
    name = "qsbk"
    allowed_domains = ["qiushibaike.com"]
    '''
    start_urls = (
        'http://www.qiushibaike.com/',
    )
    '''
    def start_requests(self):
        ua={"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
        yield Request('http://www.qiushibaike.com/',headers=ua)
    def parse(self, response):
        it=FirstItem()
        it["content"]=response.xpath("//div[@class='content']/span/text()").extract()
        it["link"]=response.xpath("//a[@class='contentHerf']/@href").extract()
        yield it

