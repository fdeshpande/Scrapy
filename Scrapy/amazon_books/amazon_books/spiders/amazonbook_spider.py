from typing import Any

from scrapy.utils.response import open_in_browser

from ..items import AmazonBooksItem
import scrapy
from scrapy.http import Response,FormRequest


class AmazonBookSpider(scrapy.Spider):
    name = "book"
    page_number = 2
    start_urls = [
        "https://quotes.toscrape.com/login"
    ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        token = response.css('form input[name="csrf_token"]::attr(value)').extract_first()  # Check token field name
        return FormRequest.from_response(response,
                                         formdata={
                                             'csrf_token': token,
                                             'username': 'deshpande2@gmail.com',
                                             'password': 'Falguni@123'
                                         }, callback=self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
        items = AmazonBooksItem()

        items["book_name"] = response.css('span.text::text').extract()
        items["author"] = response.css('.author::text').extract()
        items["number_of_reviews"] = response.css('.tag::text').extract()

        yield items

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.start_scraping)