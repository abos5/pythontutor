# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from job.items import DoorItem
import redis

_conn = redis.Redis(host='localhost', port=6379, db=1)

count_url = 1


def process_request(req):
    global count_url
    url = req.url
    count_url = _conn.incr('count_url')
    if _conn.zscore('urls', url):
        return
    else:
        data = {url: count_url}
        _conn.zadd('urls', **data)
        return req


class DoorSpider(CrawlSpider):
    """load and save as file
    """
    name = 'door'
    allowed_domains = ['6711.com']
    start_urls = ['http://www.6711.com/']

    rules = [Rule(
        LinkExtractor(allow=r'6711'),
        callback='parse_item',
        process_request=process_request,
        follow=True)
    ]

    def parse_item(self, response):
        global count_url
        i = DoorItem()
        i['prefix'] = response.url[
            response.url.index("//")+2:response.url.index(".")]
        i['url'] = response.url
        body = response.body  # response.url
        filename = 'htmls/%s.html' % count_url
        f = open(filename, 'wb')
        f.write(body)
        f.close()
        return i


#
