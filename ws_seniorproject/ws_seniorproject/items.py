# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WsSeniorprojectItem(scrapy.Item):
  product_name = scrapy.Field()
  product_sale_price = scrapy.Field()
  #product_sale_price_cents = scrapy.Field()
  product_rating = scrapy.Field()
  rating_count = scrapy.Field()
  percent_5_stars = scrapy.Field()
  percent_4_stars = scrapy.Field()
  percent_3_stars = scrapy.Field()
  percent_2_stars = scrapy.Field()
  percent_1_stars = scrapy.Field()
  #product_availability = scrapy.Field()
  urls = scrapy.Field()
  # 