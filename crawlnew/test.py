# import scrapy
# from scrapy.crawler import CrawlerProcess
# import re

# class MySpider(scrapy.Spider):
# 	name = "giaoduc"
# 	allowed_domains = ['vnexpress.net']

# 	start_urls = ['https://vnexpress.net/tin-tuc/giao-duc']
# 	# count = 0
# 	# sets = set()
# 	# items = []
# 	inputurl = 'https://vnexpress.net/tin-tuc/giao-duc/nam-sinh-quang-ninh-lap-ky-luc-phan-khoi-dong-o-olympia-3730690.html'

# 	def parse(self,response):

# 		# self.log('trang ở đây')
# 		#urls = response.xpath('//h3[@class="title_news"]/a[1]/@href').extract()
# 		# for url in urls:
# 		# 	url = response.urljoin(url)
# 		# 	if url in self.sets or re.search("/infographics/",url)!=None or re.search("/photo/",url)!=None or re.search("/trac-nghiem/",url)!=None or re.search("/hoc-tieng-anh/",url)!=None or re.search("/giao-duc-40/",url)!=None :
# 		# 		continue
# 		# 	else:
# 		# 		self.sets.add(url)
# 		yield scrapy.Request(url=self.inputurl, callback=self.parse_details)


# 		# return items

# 		# next_page_url = response.css('div#pagination.pagination.mb10 > a.next::attr(href)').extract_first()
# 		# # self.log('trang ở đây'+ next_page_url)
# 		# self.count = self.count + 1
# 		# if next_page_url:
# 		# 	if self.count < 2:
# 		# 		next_page_url =  response.urljoin(next_page_url)
# 		# 		self.log('trang ở đây'+ next_page_url)
# 		# 		yield scrapy.Request(url=next_page_url, callback=self.parse)

# 	def parse_details(self,response):
# 		# url_check = response.xpath('//link[@rel="amphtml"]/@href').extract_first()
# 		# if url_check in self.sets == False:
# 		#  self.sets.add(url_check)
# 		# parsedTexts = []
# 		# for text in texts:
# 		# 	# print("[Here]" + text)
# 		# 	parsedTexts.append(to_write(str(text)))
# 		# 	parsedTexts.append(text)
		
# 		text_result = ''
# 		texts = response.xpath('//p[@class="Normal"]/text()').extract()
# 		for text in texts:
# 		  text_result = text_result + text
# 		if text_result != '':
# 			yield {
# 				'group': "nhóm 6",
# 				'link':  response.xpath('//link[@rel="amphtml"]/@href').extract_first(),
# 				'title': response.xpath('//h1[@class="title_news_detail mb10"]/text()').extract_first(),
# 				'sapo':  response.xpath('//h2[@class="description"]/text()').extract_first(),
# 				'text':  text_result,}
# process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})
# process.crawl(MySpider)
# process.start() # the script will block here until the crawling is finished
print(len(t))

for x in t :
	print(x)
