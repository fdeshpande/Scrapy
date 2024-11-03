# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonBooksItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    author = scrapy.Field()
    number_of_reviews = scrapy.Field()

