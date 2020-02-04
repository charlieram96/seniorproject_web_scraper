# -*- coding: utf-8 -*-
import scrapy
from ws_seniorproject.items import WsSeniorprojectItem


class Project1Spider(scrapy.Spider):
    name = 'project1'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=nike+shoes+men&i=fashion-womens-shoes&crid=155J3BB8KTU8M&sprefix=nike+shoes%2Cfashion-womens-shoes%2C469&ref=nb_sb_ss_i_6_10']

    def parse(self, response):
         items = WsSeniorprojectItem()
         title = response.css('span.a-size-base-plus.a-color-base.a-text-normal::text').extract()
         dollars = response.css('span.a-price-whole::text').extract()
         cents = response.css('span.a-price-fraction::text').extract()
         rating = response.css('span.a-icon-alt::text')[4:].extract()
         reviews_number = response.css('span.a-size-base::text').extract()
         items['product_name'] = title
         items['product_sale_price_dollars'] = dollars
         items['product_sale_price_cents'] = cents
         items['product_rating'] = rating
         items['product_number_of_reviews'] = reviews_number
         yield items
