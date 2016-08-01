# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# The project scrapes data from Stack Overflow to grab new questions (title and URL)
# Scraped data is stored in postgres
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#Holds the data that we plan to scrape 
class StackItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()