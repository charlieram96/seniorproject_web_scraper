# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WsSeniorprojectItem(scrapy.Item):
  product_name = scrapy.Field()
  product_sale_price_dollars = scrapy.Field()
  product_sale_price_cents = scrapy.Field()
  product_rating = scrapy.Field()
  product_number_of_reviews = scrapy.Field()
  #product_availability = scrapy.Field()
