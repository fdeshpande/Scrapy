# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class AmazonBooksPipeline:
    def __init__(self):
        self.create_database_connection()

    def create_database_connection(self):
        self.conn = pymongo.MongoClient(
            host= 'localhost',
            port= 27017
        )
        db = self.conn['amazon_books']
        self.collection = db['book_details']

    def process_item(self, item, spider):
        for i in range(len(item["book_name"])):
            book_ = {
                "book_name" : item["book_name"][i],
                "author" : item["author"][i],
                "number_of_reviews" : item["number_of_reviews"][i]
            }
            self.collection.insert_one(book_)
        return item
