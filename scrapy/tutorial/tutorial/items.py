# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


str_serializer = "".join


class DoorItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    prefix = Field(str_serializer=str_serializer)
    url = Field(str_serializer=str_serializer)


class TutorialItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()


class ZhihuItem(Item):
    title = Field(serializer=str_serializer)
    url = Field(serializer=str_serializer)


class AbosItem(Item):
    title = Field(serializer=str_serializer)
    link = Field(serializer=str_serializer)
    desc = Field(serializer=str_serializer)
    filename = Field(serializer=str_serializer)


class BarItem(Item):
    title = Field(serializer=str_serializer)
    # links = Field()
    scripts = Field()
    source = Field()

# end of file
