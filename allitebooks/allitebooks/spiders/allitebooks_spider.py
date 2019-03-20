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
        page = response.url.split("/")[-2]
        filename = 'allitebooks-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
