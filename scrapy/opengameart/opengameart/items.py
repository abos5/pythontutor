# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArtItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()


class SoundItem(scrapy.Item):
    # define the fields for your item here like:
    ogg = scrapy.Field()
    mp3 = scrapy.Field()


# eof
