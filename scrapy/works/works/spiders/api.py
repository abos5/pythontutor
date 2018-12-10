# -*- coding: utf-8 -*-
""" main: http://www.utadiner.abos5.com/interface
required APIs:
    hotel-info.php',
    food-styles.php',
    hotel-album.php',
    hotel-rcmd-foods.php',
    hotel-pref-list.php',
    home-ad-hotels.php',
    hotels-list.php',
    keywords-results-num.php',
    hot-keywords.php',
    add-comment.php',
    add-comment-helpful.php',
    comment-list-get.php',
    hotel-comments.php',
    add-del-fav.php',
    user-fav-list.php',
    add-error-info.php',
    user-info.php',
"""
import scrapy
from works.items import EasyItem
import json


class ApiSpider(scrapy.Spider):
    name = "api"
    allowed_domains = ["utadiner.abos5.com"]
    start_urls = (
        'http://www.utadiner.abos5.com/interface/item-list-get.php?catid=110',
        'http://www.utadiner.abos5.com//index.\
php?m=item&act=ajax&do=subject&op=get_membereffect&in_ajax=1',
    )

    def parse(self, response):
        item = EasyItem()
        try:
            item['body'] = json.loads(response.body)
        except ValueError:
            item['body'] = response.body

        item['title'] = response.url
        return item
