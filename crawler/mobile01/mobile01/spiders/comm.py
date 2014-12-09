# -*- coding: utf-8 -*-
import sys
 
import scrapy
import json
from scrapy.http import Request, FormRequest
from scrapy.spider import Spider
from scrapy.selector import Selector
from ..items import Mobile01Item

class comm(scrapy.Spider):
	name = "mobile01"
	allowed_domains = ["www.mobile01.com"]
	start_urls = [
		"http://www.mobile01.com/forumtopic.php?c=27&p=%d" % int(i+1) for i in range(1)
		]

	def parse(self, response):
		request = Request(response.url, callback = self.parse_profile)
		yield request

	def parse_profile(self, response):
		sel = Selector(response)
		itemResult=[]
		rows = sel.xpath('//tr')
		print len(rows)
		for row in rows:
			title = row.xpath('.//a[@class="topic_gen"]/text()').extract()
			if len(title) > 0:
				item = Mobile01Item()
				item['title'] = title[0]
				item['author'] = row.xpath('.//a/p/text()').extract()[1]
				item['link'] = row.xpath('.//span[@class="subject-text"]/a[contains(@class,"topic_gen")]/@href').extract()[0]
				item['content'] = 'test'
				item['total'] = dict(item)
				itemResult.append(item)
		return itemResult

