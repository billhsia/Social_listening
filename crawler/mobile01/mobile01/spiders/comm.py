 
import scrapy
from scrapy.http import Request, FormRequest


class comm(scrapy.Spider):
	name = "comm"
 	allowed_domains = ["www.mobile01.com"]
 	start_urls = [
 		"http://www.mobile01.com/forumtopic.php?c=16&p="
 		]

 	def parse(self, response):
 		result = []
 		for sid in range(2):
 			link = response.url+str(sid)
 			print link