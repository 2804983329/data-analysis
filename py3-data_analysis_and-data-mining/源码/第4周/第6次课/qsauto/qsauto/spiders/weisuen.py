# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from qsauto.items import QsautoItem


class WeisuenSpider(CrawlSpider):
    name = 'weisuen'
    allowed_domains = ['qiushibaike.com']
    '''
    start_urls = ['http://www.qiushibaike.com/']
    '''
    def start_requests(self):
        ua={"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
        yield Request('http://www.qiushibaike.com/',headers=ua)
    rules = (
        Rule(LinkExtractor(allow='article'), callback='parse_item', follow=True), #follow是否跟进，即爬取一个后是否从当前页面提取链接继续爬取
    )

    def parse_item(self, response):
        i = QsautoItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i["content"]=response.xpath("//div[@class='content']/text()").extract()
        i["link"]=response.xpath("//link[@rel='canonical']/@href").extract()
        print(i["content"])
        print(i["link"])
        print("")
        return i
