# -*- coding: utf-8 -*-


from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import json
from tutorial.items import ZhihuItem
import redis


r = redis.Redis(host='localhost', port=6379, db=2)


def filter_request(req):
    if r.zscore('crapied:question', req.url):
        return
    question = req.url.rstrip('/')
    begin = question.rindex('/') + 1
    question = int(question[begin:])
    r.publish('crapied:question', question)  # req.url
    r.zadd('crapied:question', req.url, question)
    r.incr('crapied:question:counter')
    return req


class ZhihuSpider(CrawlSpider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com', ]
    start_urls = ['http://www.zhihu.com/people/wonderful-vczh']

    rules = (
        Rule(
            LinkExtractor(allow=r'question/\d+$'),
            callback='parse_item',
            follow=True,
            process_request=filter_request),
    )

    def parse_item(self, response):
        i = ZhihuItem()
        i['title'] = response.xpath('//title/text()').extract()
        i['url'] = response.url
        return i
