# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import AbosItem


class FooSpider(scrapy.Spider):
    name = "foo"
    allowed_domains = ["abos5.com", "sourceforge.net"]
    start_urls = (
        'http://www.abos5.com/',
        # 'http://sourceforge.net/projects/shadowsocksgui/files/dist/'
    )

    def parse(self, response):
        for link in response.xpath('//a/@href').extract():
            yield AbosItem(link=link)

        return
        # sample scripts
        # for h3 in response.xpath('//h3').extract():
        #     yield AbosItem(title=h3)

        # for url in response.xpath('//a/@href').extract():
        #     yield scrapy.Request(url, callback=self.parse)
