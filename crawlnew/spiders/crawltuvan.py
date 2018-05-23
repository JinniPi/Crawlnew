import scrapy
#from crawlnew.items import NewItem
import urllib.parse
import re

def to_write(uni_str):
	return urllib.parse.unquote(uni_str.encode('utf8')).decode('utf8');

class crawltuvan(scrapy.Spider):

	name = "tuvan"
	allowed_domains = ['vnexpress.net']
	start_urls = ['https://vnexpress.net/tin-tuc/phap-luat/tu-van']
	count = 0
	sets = set()
	items = []

	def parse(self, response):
		# self.log('trang ở đây')
		urls = response.xpath('//h3[@class="title_news"]/a[1]/@href').extract()
		for url in urls:
			url = response.urljoin(url)
			if url in self.sets or re.search("/infographics/",url) != None or re.search("/tu-van/",url) == None or re.search("/ho-so-pha-an/",url) != None :
				continue
			else:
				self.sets.add(url)
			yield scrapy.Request(url=url, callback=self.parse_details)


		# return items

		next_page_url = response.css('div#pagination.pagination.mb10 > a.next::attr(href)').extract_first()
		# self.log('trang ở đây'+ next_page_url)
		self.count = self.count + 1
		if next_page_url:
			if self.count < 1000:
				next_page_url =  response.urljoin(next_page_url)
				self.log('trang ở đây'+ next_page_url)
				yield scrapy.Request(url=next_page_url, callback=self.parse)

	def parse_details(self,response):
		# url_check = response.xpath('//link[@rel="amphtml"]/@href').extract_first()
		# if url_check in self.sets == False:
		#  self.sets.add(url_check)
		# parsedTexts = []
		# for text in texts:
		# 	# print("[Here]" + text)
		# 	parsedTexts.append(to_write(str(text)))
		# 	parsedTexts.append(text)
		
		text_result = ''
		texts = response.xpath('//p[@class="Normal"]/text()').extract()
		for text in texts:
		  text_result = text_result + text
		if text_result != '':
			yield {
				'group': "nhóm 6",
				'link':  response.xpath('//link[@rel="amphtml"]/@href').extract_first(),
				'title': response.xpath('//h1[@class="title_news_detail mb10"]/text()').extract_first(),
				'sapo':  response.xpath('//h2[@class="description"]/text()').extract_first(),
				'text':  text_result,}
	

			
		

		

	
		
