from typing import Any
import scrapy
from scrapy.http import Response
from ..items import AmazonscrapItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    page_number=2
    start_urls = [
        'https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A1040660&page=1'
    ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        item = AmazonscrapItem()
        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_price = response.css('.a-price-whole::text').extract()
        product_reviews = response.css('.a-size-base.s-underline-text::text').extract()
        product_image = response.css('img.s-image::attr(src)').extract()

        item["product_name"]=product_name
        item["product_price"]=product_price
        item["product_reviews"]=product_reviews
        item["product_image"]=product_image

        yield item

    # Pagination logic
        if self.page_number <= 400:
            self.page_number += 1
            next_page = f'https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A1040660&page={self.page_number}'
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)


