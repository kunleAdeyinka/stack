# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

from stack.items import *


class StackPipeline(object):
	#StackOverflow pipeline for storing scraped items in the database
    def __init__(self):
        self.conn = psycopg2.connect(host='localhost', database='scrape', user='postgres', password='admin', port='5432')
	self.cursor = self.conn.cursor()
		
    def process_item(self, item, spider):
        try:
            if type(item) is StackItem:
                self.cursor.execute('''INSERT INTO questions (title, url) VALUES (%s, %s);''', (item.get('title'), item.get('url'),))

	    self.conn.commit()
	    self.cursor.fetchall()
			
	except psycopg2.DatabaseError, e:
            print "Error: %s" % e
	return item
		
