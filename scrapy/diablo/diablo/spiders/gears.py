# -*- coding: utf-8 -*-

import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import redis
from diablo.items import SkillItem, SkillEnhanceItem


r = redis.Redis(host='localhost', port=6379, db=1)
redk_url = 'crapied:hash:url'
redk_gear = 'crapied:hash:gear'
reg_skill = re.compile(r'^.*/cn/skill/(\w+)/active/$')


def filter_request(url):
    '''
    crapied:hash:url  url => 1
    crapied:hash:gear gear_name => gear_info.json
    '''
    if r.hsetnx(redk_url, url, 1):
        return True

    return False


class GearsSpider(CrawlSpider):
    name = "gears"
    allowed_domains = ["db.d.163.com"]
    start_urls = ['http://db.d.163.com/cn/']

    def parse(self, response):
        # scrapy.logger.warning
        self.logger.debug("hi")
        return response.request

    def parse_item(self, response):
        i = SkillItem()
        i['uid'] = response.url
        return i


class HelloSpider(CrawlSpider):
    name = "hello"

    allowed_domains = ["db.d.163.com"]
    start_urls = ["http://db.d.163.com/cn/"]

    rules = (
        Rule(LinkExtractor(allow=(r'/cn/',), deny=(r'/tw/',))),
    )

    def parse(self, response):
        # urls = response.css('div.m-nav ::attr(href)').extract()
        urls = response.css('a ::attr(href)').extract()
        item = self.try_parse_skill(response)
        if item:
            yield item

        # self.logger.info(urls)
        for url in urls:
            next_page = response.urljoin(url)
            if not filter_request(next_page):
                continue
            # self.logger.info(next_page)
            yield scrapy.Request(
                next_page,
                callback=self.parse
            )

    def try_parse_skill(self, response):
        match = reg_skill.match(response.url)
        if not match:
            return

        groups = match.groups()
        if not len(groups):
            return

        item = SkillItem()
        item['uid'] = response.url
        item['level'] = response

        return item


# eof
