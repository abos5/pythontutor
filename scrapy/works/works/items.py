# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


def str_serializer(str):
    return "".join(str)


class WorksItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass


class EasyItem(Item):
    body = Field()
    title = Field(serializer=str_serializer)

# end of file
