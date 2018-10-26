# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['i.nagoya-u.ac.jp']
    start_urls = ['https://www.i.nagoya-u.ac.jp/en/']

    def parse(self, response):
        for url in response.css("li.col-xs-12 .discription a::attr(href)").extract():
            yield scrapy.Request("https://www.i.nagoya-u.ac.jp" + url, self.parse_content)


    def parse_content(self, response):
        yield {"title": response.css("h2.entry-title::text").extract_first()}
            

        
