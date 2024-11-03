import scrapy
from ..items import  QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self,response):
        items = QuotetutorialItem()
        all_div_quote = response.css('div.quote')
        for quote in all_div_quote:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tags = quote.css('.tag::text').extract()

            items['title']=title
            items['author']=author
            items['tags']=tags

            yield items