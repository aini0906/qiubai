# -*- coding: utf-8 -*-
import scrapy
from qiubai.items import QiubaiItem

class QiubaiSpider(scrapy.Spider):
    name = "Qiubai"
    #allowed_domains = ["http://www.qiushibaike.com/"]
    start_urls = (
        'http://www.qiushibaike.com//',
    )
    url = 'http://www.qiushibaike.com'
    page = 1
    def parse(self, response):
        #fp = open('qiubai.html','w')
        #fp.write(response.body)
        #fp.close()
        item = QiubaiItem()
        selector = scrapy.Selector(response)
        qiubais = selector.xpath('//div[@class="article block untagged mb15"]')
        for qiubai in qiubais :
            item['name'] = qiubai.xpath('div[1]/a[2]/h2/text()').extract()
            item['content'] = qiubai.xpath('div[2]/text()').extract()
            item['vote'] = qiubai.xpath('div[3]/span[1]/i/text()').extract()
            yield item
            pageNum = selector.xpath('//ul[@class="pagination"]/li[last()-1]/a/span/text()').extract()[0]
            if self.page <= pageNum:
                self.page += 1
                yield scrapy.http.Request('http://www.qiushibaike.com/8hr/page/'+str(self.page)+'?s=4878824',callback=self.parse)

