import scrapy
#from crawlnew.items import NewItem
import urllib.parse
import re
import MySQLdb
from crawlnew.models import db_connect,CrawlDB,create_table
from sqlalchemy.orm import sessionmaker

def to_write(uni_str):
	return urllib.parse.unquote(uni_str.encode('utf8')).decode('utf8');

class crawlgiaitri(scrapy.Spider):
	#khởi tạo các thuộc tính của spider

	name = "giaitri"
	allowed_domains = ['vnexpress.net']
	start_urls = ['https://giaitri.vnexpress.net/']
	count = 0
	sets = set() # ban đầu set khởi tạo rỗng
	# items = []
	def __init__(self,*a, **kw):
		super(crawlgiaitri, self).__init__(*a, **kw)
		self.sets = self.get_setUrl()


	#Hàm này load link từ database lên đưa vào sets 
	def get_setUrl(self):
		engine = db_connect()
		Session = sessionmaker(bind=engine)
		session = Session()
		quotedb = CrawlDB()
		try:
			session.commit()
			list_obj = session.query(CrawlDB).all()
			for obj in list_obj:
				self.sets.add(obj.link)
			return self.sets
		except:
			session.rollback()
			raise
		finally:
			session.close()

	 
	#Đây là hàm khi bắt đầu crawl đi vào.
	def parse(self, response):
		print('----------')
		print(len(self.sets))
		# if self.count == 0: # Nếu trang crawl là 0 thì load link từ csdl lên.Lần đầu tiên crawl (khi trong csdl chưa có thì trả về rỗng)
		# 	self.get_setUrl()
		urls = response.xpath('//h3[@class="title_news"]/a[1]/@href').extract()
		print(self.sets)
		print('-------------')
		print(len(self.sets))
		for url in urls:
			# url = response.urljoin(url)
			#xét url có trong set hoặc url có phải photo ,video hay k?
			if re.search("/infographics/",url) != None or re.search("/photo/",url) != None or re.search("/video/",url) !=None:
				continue
			if url in self.sets :
				print('url trùng')
				print(url)
				continue
			else:
				self.sets.add(url)
				yield scrapy.Request(url=url, callback=self.parse_details)
		# crawl sang trang kế tiếp
		next_page_url = response.css('p#pagination.pagination.mb10 > a.next::attr(href)').extract_first()
		print("kiem tra")
		print(self.sets)
		self.count = self.count + 1
		if next_page_url:
			if self.count < 5:
				next_page_url =  response.urljoin(next_page_url)
				# self.log('trang ở đây'+ next_page_url)
				yield scrapy.Request(url=next_page_url, callback=self.parse) #Gọi lại hàm Parse
		print(len(self.sets))
	
	#Crawl chi tiết từng link
	def parse_details(self,response):
		text_result = ''
		texts = response.xpath('//p[@class="Normal"]/text()').extract()
		for text in texts:
		  text_result = text_result + text
		if text_result != '':
			yield {
				'origin': "nhóm 6",
				'link':  response.xpath('//link[@rel="amphtml"]/@href').extract_first(),
				'title': response.xpath('//h1[@class="title_news_detail mb10"]/text()').extract_first(),
				'sapo':  response.xpath('//h2[@class="description"]/text()').extract_first(),
				'content':  text_result,}
	

			
		

		

	
		
