from typing import Any
import scrapy
from scrapy.http import Response
from ..items import QuotescrapItem


class QuoteSpider(scrapy.Spider):
    name= "quote"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        items = QuotescrapItem()

        title = response.css('span.text::text').extract()
        author = response.css('.author::text').extract()
        tag = response.css('div a.tag::text').extract()

        items["title"] = title
        items["author"] = author
        items["tag"] = tag

        yield items
