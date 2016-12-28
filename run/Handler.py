#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-11-22 01:53:39
# Project: Allmovie

from pyspider.libs.base_handler import *
import re


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('www.allmovie.com/themes', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            if re.match("http://www.allmovie.com/characteristic/theme/\S+",each.attr.href, re.U):
                self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            if re.match("http://www.allmovie.com/movie/\S+",each.attr.href, re.U):
                self.crawl(each.attr.href, callback=self.list_page)
    
    @config(priority=2)
    def list_page(self, response):
        return {        
            "url": response.url,
            
            "title": response.doc('.movie-info > [itemprop="name"]').text(),
            
            "year": response.doc('.movie-info > [itemprop="name"] > span').text(),

            "overview": response.doc('.synopsis > [itemprop="description"]').text(),
            
            "themes": response.doc('.themes > .charactList').text().split(" | "),
            
            "keyword": response.doc('.keywords > .charactList').text().split(", "),

            "moods": response.doc('.moods > .charactList').text().split(" | "),

            "genres": response.doc('.header-movie-genres > a').text().split(" "),
            "sub-generes": response.doc('.header-movie-subgenres > a').text().split(" ")
        }