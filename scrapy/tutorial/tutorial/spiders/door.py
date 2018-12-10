# -*- coding: utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from tutorial.items import DoorItem
import redis

_conn = redis.Redis(host='localhost', port=6379, db=1)


def process_links(a, b, c):
    print(locals())
    exit()


class DoorSpider(CrawlSpider):
    """load and save as file
    """
    name = 'door'
    allowed_domains = ['6711.com']
    start_urls = ['http://www.6711.com/']

    rules = [Rule(
        LinkExtractor(allow=r'6711/'),
        callback='parse_item',
        process_links=process_links,
        follow=True)
    ]

    def parse_item(self, response):
        i = A6711Item()
        i['prefix'] = response.url[
            response.url.index("//")+2:response.url.index(".")]
        i['url'] = response.url
        print(dir(response))
        return i


#
