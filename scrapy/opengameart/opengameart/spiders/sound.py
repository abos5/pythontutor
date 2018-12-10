import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from opengameart.items import SoundItem


class SoundSpider(scrapy.Spider):
    '''
    '''
    name = 'sound'

    start_urls = [
        'http://opengameart.org/art-search-advanced?keys=&title=&field_art_tags_tid_op=and&field_art_tags_tid=&name=&field_art_type_tid%5B%5D=12&field_art_type_tid%5B%5D=13&field_art_licenses_tid%5B%5D=2&field_art_licenses_tid%5B%5D=3&field_art_licenses_tid%5B%5D=6&field_art_licenses_tid%5B%5D=5&field_art_licenses_tid%5B%5D=10310&field_art_licenses_tid%5B%5D=4&field_art_licenses_tid%5B%5D=8&field_art_licenses_tid%5B%5D=7&sort_by=count&sort_order=DESC&items_per_page=24&Collection=&page=0',
    ]

    def parse(self, response):
        found = response.css('.play-button')

        pages = [
            response.urljoin(u)
            for u in response.css('.pager-item a ::attr("href")').extract()
        ]

        for f in found:
            item = SoundItem()
            item['mp3'] = f.css('::attr("data-mp3-url")').extract_first()
            item['ogg'] = f.css('::attr("data-ogg-url")').extract_first()
            yield item

        for p in pages:
            yield scrapy.Request(p, callback=self.parse)


# eof
