# Scrapy uses this class to find the exact data to scrape

import scrapy

from scrapy.selector import Selector
from stack.items import StackItem


class StackSpider(scrapy.Spider):
	name = "stack" #the name of the spider
	allowed_domains = ["stackoverflow.com"]	#contains the base URLs for the allowed domains for the spider to crawl
	start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ] # list of URLs for the spider to start crawling from
	
	def parse(self, response):
		questions = Selector(response).xpath('//div[@class="summary"]/h3')
		
		for question in questions:
			item = StackItem()
			item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
			item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
			yield item
	
	
