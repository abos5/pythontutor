# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import json
from tutorial.items import BarItem
import redis


r = redis.Redis(host='localhost', port=6379, db=2)


def filter_request(req):
    if r.sismember('crapied:urls', req.url):
        return
    r.sadd('crapied:urls', req.url)
    r.incr('crapied:counter')
    return req


class BarSpider(CrawlSpider):
    name = 'bar'
    allowed_domains = ['abos5.com', 'readthedocs.org']
    start_urls = ['http://doc.abos5.com/scrapy/']

    rules = (
        Rule(
            LinkExtractor(allow=r'intro/'),
            callback='parse_item',
            follow=True,
            process_request=filter_request),
        # Rule(LinkExtractor(
        #     allow=r'topics/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(
        #     allow=r'javascript/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(
        #     allow=r'css/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = BarItem()
        i['title'] = response.xpath('//title/text()').extract()
        # i['links'] = response.xpath('//a/@href').extract()
        i['scripts'] = response.xpath(
            '//script[@type="text/javascript"]/@src').extract()
        i['source'] = response.url
        return i
