# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

str_serializer = "".join


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DoorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    prefix = scrapy.Field(str_serializer=str_serializer)
    url = scrapy.Field(str_serializer=str_serializer)

#
