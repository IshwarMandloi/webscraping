import  scrapy
from ..items import WebscrapingItem


class Digital(scrapy.Spider):
	name ='digital'
	start_urls = [
		'http://quotes.toscrape.com/'
	]

	"""
	def parse(self,response):
		title = response.css('title::text').extract()
		yield {'titletext': title}

	"""
	def parse(self,response):

		items = WebscrapingItem()

		all_div_digital = response.css('div.quote')

		for digital in all_div_digital:
			
			title = all_div_digital.css('span.text::text').extract()
			author = all_div_digital.css('.author::text').extract()
			tag = all_div_digital.css('.tag::text').extract()

			items['title'] = title
			items['author'] = author
			items['tag'] = tag

			yield items