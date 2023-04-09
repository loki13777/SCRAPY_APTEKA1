# паук для проверки работоспособности прокси
import scrapy
import json

class AptekaSpider(scrapy.Spider):
    name = "ip_cheker"
    start_urls = ['https://whoer.net/ru']




    def get_ip(self, response):

        print(response.css('strong.your-ip::text').get())

