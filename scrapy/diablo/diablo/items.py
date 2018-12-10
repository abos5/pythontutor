# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DiabloItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class GearItem(scrapy.Item):
    uid = scrapy.Field()


class MaterialItem(scrapy.Item):
    uid = scrapy.Field()


class SkillItem(scrapy.Item):
    uid = scrapy.Field()
    level = scrapy.Field()
    element = scrapy.Field()
    trigger_pro = scrapy.Field()
    cost = scrapy.Field()
    desc = scrapy.Field()


class SkillEnhanceItem(scrapy.Item):
    uid = scrapy.Field()
    level = scrapy.Field()
    element = scrapy.Field()
    trigger_pro = scrapy.Field()
    cost = scrapy.Field()
    desc = scrapy.Field()


class GearEnhanceItem(scrapy.Item):
    uid = scrapy.Field()
    desc = scrapy.Field()
    level = scrapy.Field()


# eof
