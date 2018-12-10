import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from opengameart.items import ArtItem


class ArtSpider(scrapy.Spider):
    '''
    stop here
    http://opengameart.org/art-search-advanced?keys=&title=&field_art_tags_tid_op=and&field_art_tags_tid=&name=&field_art_type_tid[9]=9&field_art_type_tid[10]=10&field_art_type_tid[7273]=7273&field_art_type_tid[14]=14&field_art_type_tid[12]=12&field_art_type_tid[13]=13&field_art_type_tid[11]=11&field_art_licenses_tid[2]=2&field_art_licenses_tid[3]=3&field_art_licenses_tid[6]=6&field_art_licenses_tid[5]=5&field_art_licenses_tid[10310]=10310&field_art_licenses_tid[4]=4&field_art_licenses_tid[8]=8&field_art_licenses_tid[7]=7&sort_by=count&sort_order=DESC&items_per_page=24&collection=&page=50&field_art_type_tid%2525255B%2525255D=9
    '''
    name = 'art'

    start_urls = [
        'http://opengameart.org/content/cobblestone-tileset',
        'http://opengameart.org/content/sci-fi-space-simple-bullets',
        'http://opengameart.org/content/heal-spell',
        'http://opengameart.org/content/desert-tileset',
        'http://opengameart.org/content/bitmap-font-0',
        'http://opengameart.org/content/isometric-parts-2',
        'http://opengameart.org/content/more-isometric-parts',
        'http://opengameart.org/content/magic-flame',
        'http://opengameart.org/content/classic-dungeon-walls',
        'http://opengameart.org/content/timbered-house',
    ]

    def parse(self, response):
        found = response.css('[download] ::attr("href")')
        urls = found.extract()

        for u in urls:
            item = ArtItem()
            item['url'] = u
            yield item


# eof
