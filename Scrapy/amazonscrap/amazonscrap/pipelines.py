# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# import pymongo
#
# class AmazonscrapPipeline:
#     def __init__(self):
#         self.con = pymongo.MongoClient(
#             host= 'localhost',
#             port= 27017
#         )
#         db = self.con['amazon_products']
#         self.collection = db['amazon_product_details']
#     #
#     def process_item(self, item, spider):
#         for i in range(len(item['product_name'])):
#             product = {
#                 'product_name': item['product_name'][i],
#                 'product_price': float(item['product_price'][i]),
#                 'product_reviews': int(item['product_reviews'][i].replace(',', '')),  # Convert reviews to an integer
#                 'product_image': item['product_image'][i]
#             }
#             self.collection.insert_one(product)  # Insert each product separately
#         return item

from itemadapter import ItemAdapter
import mysql.connector

class AmazonscrapPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="tiger",
                    database="amazon_products"
                )
        self.cur = self.con.cursor()

    def create_table(self):
        self.cur.execute("""DROP TABLE IF EXISTS amazon_product_details""")
        self.cur.execute("""create table amazon_product_details(product_name text, 
                                                                product_price float,
                                                                product_reviews int,
                                                                product_image text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        for i in range(len(item['product_name'])):
            self.cur.execute("""
                INSERT INTO amazon_product_details (product_name, product_price, product_reviews, product_image) 
                VALUES (%s, %s, %s, %s)
            """, (
                item['product_name'][i],
                float(item['product_price'][i]),
                int(item['product_reviews'][i].replace(',', '')),
                item['product_image'][i]
            ))
        self.con.commit()

