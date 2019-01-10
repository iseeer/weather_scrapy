import scrapy
from ..items import MyspiderItem
from scrapy.crawler import CrawlerProcess

class MySpider(scrapy.Spider):
    name = "weather"
    allowed_domains = ["weather.com.cn"]
    start_urls = ["http://www.weather.com.cn/weather/101210301.shtml"]
    def parse(self, response):
        papers = response.xpath(".//*[@class='t clearfix']//li")
        for paper in papers:
            date = paper.xpath("./h1/text()").extract()[0]
            weather = paper.xpath("./p[@title]/text()").extract()[0]
            item = MyspiderItem(date=date, weather=weather)
            yield item

if __name__=='__main__':
    process = CrawlerProcess()
    process.crawl(MySpider)
    process.start()
