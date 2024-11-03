# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# to store db in sqlite

# import sqlite3
#
# class QuotetutorialPipeline(object):
#     def __init__(self):
#         self.create_connection()
#         self.create_table()
#
#     def create_connection(self):
#         self.con = sqlite3.connect('myquote.db')
#         self.cur = self.con.cursor()
#
#     def create_table(self):
#         self.cur.execute("""DROP TABLE IF EXISTS quote_tb""")
#         self.cur.execute("""create table quote_tb(title,author,tag)""")
#
#     def process_item(self, item, spider):
#         self.store_db(item)
#         return item
#     def store_db(self,item):
#         self.cur.execute("""Insert into quote_tb Values(?,?,?)""", (
#             item["title"][0],
#             item["author"][0],
#             item["tags"][0]
#         ))
#         self.con.commit()


# to store db in mysql
# from itemadapter import ItemAdapter
# import mysql.connector
#
#
# class QuotetutorialPipeline(object):
#     def __init__(self):
#         self.create_connection()
#         self.create_table()
#
#     def create_connection(self):
#         self.con = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="tiger",
#             database="myquote"
#         )
#         self.cur = self.con.cursor()
#
#     def create_table(self):
#         self.cur.execute("""DROP TABLE IF EXISTS quote_tb""")
#         self.cur.execute("""CREATE TABLE quote_tb (
#                                 title VARCHAR(255),
#                                 author VARCHAR(255),
#                                 tag TEXT
#                             )""")
#
#     def process_item(self, item, spider):
#         self.store_db(item)
#         return item
#
#     def store_db(self, item):
#
#         self.cur.execute("""INSERT INTO quote_tb (title, author, tag) VALUES (%s, %s, %s)""", (
#             item["title"][0],
#             item["author"][0],
#             item["tags"][0]
#         ))
#         self.con.commit()


# to store db in mongodb
from itemadapter import ItemAdapter
import pymongo


class QuotetutorialPipeline(object):
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.con = pymongo.MongoClient(
            host='localhost',
            port=27017
        )
        db = self.con["myquote"]
        self.collection = db["quote_collection"]

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item[0]))
        return item


