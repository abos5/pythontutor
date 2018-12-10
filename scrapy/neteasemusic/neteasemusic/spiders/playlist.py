# -*- coding: utf-8 -*-
import scrapy
import redis
from neteasemusic import items
import urllib

conn = redis.Redis(**{
    'host': 'localhost',
    'port': 6379,
    'db': 1,
    # 'password': 'abos',
})


def redk(suffix):
    return ':'.join(['spider:netease', suffix])

def makeUrl(suffix):
    return ''.join(['http://music.163.com', suffix])


class PlaylistSpider(scrapy.Spider):
    limit = 35
    name = "playlist"
    allowed_domains = ["music.163.com"]
    start_urls = []

    def __init__(self):
        start_url = '&'.join([
            'http://music.163.com/discover/playlist/?order=hot',
            urllib.urlencode({
                'limit': str(self.limit),
                'offset': conn.get(redk('listofplaylist'))
            })
        ])

        conn.incr(redk('listofplaylist'), self.limit)

        self.start_urls = [
            start_url
        ]

        super(PlaylistSpider, self)

    def parse(self, response):
        print response.url
        msks = response.css('body a.msk ::attr("href")').extract()
        for url in msks:
            yield scrapy.Request(makeUrl(url))

    def parse_playlist(self, response):
        print response.url

    def parse_song(self, response):
        print response.url

    def parse_comment(self, response):
        print response.url


