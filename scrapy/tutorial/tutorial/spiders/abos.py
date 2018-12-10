# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import AbosItem

_urls_logged = []


class AbosSpider(scrapy.Spider):
    name = "abos"
    allowed_domains = ["abos5.com"]
    start_urls = (
        # 'http://www.abos5.com/',
        'http://doc.abos5.com/scrapy/',
    )
    doabspath = False

    def __init__(self, doabspath=None, *arg, **kwargs):
        super(scrapy.Spider, self).__init__(*arg, **kwargs)

        if doabspath is not None:
            self.doabspath = True

        self.domain = 'http://doc.abos5.com'

    def parse(self, response):
        import os.path
        filename = "downloads/" + self.name + '/' + response.url.split("/")[-2]

        if self.doabspath:
            filename = os.path.abspath(filename)

        for sel in response.xpath('//ul/li'):
            item = AbosItem()
            item['link'] = sel.xpath('a/@href').extract()
            url = self.make_url_from_link(item['link'], response)

            item['title'] = sel.xpath('a/text()').extract()
            item['desc'] = sel.xpath('text()').extract()
            item['filename'] = [filename]
            yield item
            if url:
                self.log("request: %s" % url, 'INFO')
                yield scrapy.Request(url, callback=self.parse)

    def make_url_from_link(self, link, response):
        """resolve everyt href from an a tag of html

        havn't solve the ".." situation yet.
        """
        if not link:
            return False

        url = link[0]
        if "#" in url:
            url = url[:url.index("#")]

        if not url:
            return False

        if 'http' in url and url.index('http') == 0:
            if self.domain not in url:
                return False
            url = url
        elif response.url[-1] != "/" and url[0] != "/":
            url = response.url + "/" + url
        else:
            url = response.url + url

        if url in _urls_logged:
            return False

        _urls_logged.append(url)
        self.log("save: %s" % url, 'INFO')
        return url


# end of file
