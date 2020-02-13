# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class WsSeniorprojectPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("myproducts.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS myproducts_tb""")
        self.curr.execute("""create table myproducts_tb(
            product_name text,
            product_sale_price_dollars text,
            product_sale_price_cents text,
            product_rating text,
            product_number_of_reviews text
            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item


    def store_db(self, item):
        self.curr.execute("""insert into myproducts_tb values(?, ?, ?, ?, ?)""", (
         item['product_name'][0],
         item['product_sale_price_dollars'][0],
         item['product_sale_price_cents'][0],
         item['product_rating'][0],
         item['product_number_of_reviews'][0]
        ))
        self.conn.commit()


# import sqlite3
# class WsSeniorprojectPipeline(object):
#      def process_item(self, item, spider):
#             print("Pipeline: " + item[product_name][0])
#             return item
