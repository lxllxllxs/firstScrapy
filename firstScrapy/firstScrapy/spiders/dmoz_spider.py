import scrapy

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    start_urls = [
        "http://d.weibo.com/1087030002_2975_2002_0"
        # "http://www.runoob.com/python/python-basic-syntax.html"
    ]


    def parse(self, response):
        els = response.xpath("//ul")
        for el in els:
            item = DmozItem()
            item['title'] = el.xpath('./li/a/text()').extract()
            yield item