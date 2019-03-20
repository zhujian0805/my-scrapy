#!/usr/bin/env python

import scrapy


class AllitebooksSpider(scrapy.Spider):
    name = "allitebooks"

    def start_requests(self):
        urls = [
            'http://allitebooks.com',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for book in response.css("div.entry-body"):
            yield {
                'name': book.css("h2.entry-title").css("a::text").get()
            }
