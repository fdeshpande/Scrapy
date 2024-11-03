# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonscrapItem(scrapy.Item):
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_reviews = scrapy.Field()
    product_image = scrapy.Field()

