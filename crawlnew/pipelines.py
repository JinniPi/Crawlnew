# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from .models import db_connect,CrawlDB,create_table
from sqlalchemy.orm import sessionmaker

class CrawlnewPipeline(object):
	def __init__(self):
		#self.file = codecs.open('thethao.json', 'w', encoding='utf-8')
		engine = db_connect()
		create_table(engine)
		self.Session = sessionmaker(bind=engine)

	def process_item(self, item, spider):
		# line = json.dumps(dict(item), ensure_ascii=False) + "\n"
		# self.file.write(line)
		# return item
		session = self.Session()
		Crawldb = CrawlDB()
		Crawldb.origin = item["origin"]
		Crawldb.link = item["link"]
		Crawldb.title = item["title"]
		Crawldb.sapo = item["sapo"]
		Crawldb.content = item["content"] 

		try:
			session.add(Crawldb)
			session.commit()
		except:
			session.rollback()
			raise
		finally:
			session.close()

		return item

	# def spider_closed(self, spider):
	# 	self.file.close()
