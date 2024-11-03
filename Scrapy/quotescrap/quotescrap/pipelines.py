# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class QuotescrapPipeline:
    def __init__(self):
        self.create_database_connection()
        self.create_table()
    def create_database_connection(self):
        self.con = mysql.connector.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = 'tiger',
            database = 'quote'
        )
        self.cur = self.con.cursor()

    def create_table(self):
        self.cur.execute("""DROP TABLE IF EXISTS quote_table""")
        self.cur.execute("""create table quote_table(title text,author text,tag text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        for i in range(len(item["author"])):
            self.cur.execute("""insert into quote_table(title, author, tag) values(%s, %s, %s)""", (
                item["title"][i],
                item["author"][i],
                item["tag"][i]
            ))
        self.con.commit()

