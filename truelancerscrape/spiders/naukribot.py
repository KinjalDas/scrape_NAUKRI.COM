# -*- coding: utf-8 -*-
import scrapy


class NaukribotSpider(scrapy.Spider):
	name = 'naukribot'
	allowed_domains = ['naukri.com']
	start_urls = ['http://www.naukri.com/information-technology-jobs/']
	count=0
	COUNT_MAX=200	
	page_count=1
	
	last_id=None
	def parse(self, response):
		job_list={}
		for jobs in response.css('.row'):
			job_list['desig']=jobs.css('.desig::text').extract()
			job_list['org']=jobs.css('.org::text').extract()
			job_list['desc']=jobs.css('span.desc::text').extract()
			self.count=self.count+1		
			yield job_list
		
		if(self.count<self.COUNT_MAX):
			self.page_count+=1	
			next_url='https://www.naukri.com/information-technology-jobs-%d' % self.page_count
			print(self.page_count)
			yield scrapy.Request(url=next_url,callback=self.parse)
			
