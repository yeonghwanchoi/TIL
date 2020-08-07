import scrapy
from playnomore.items improt PlaynomoreItem
class PlaynomoreSpider(scrapy.Spider):
    name="Playnomore"
    customn_setting = {
        "DOWNLOADER_MIEDLEWARES":{
            "scrapy.downloadmiddlewares.useragent.UserAgentMiddleware":None,
            "scrapy_fake_useragent.middleware.RandomUserAgentMiddleware":400,
        }
    }
    def start_requests(self):
        urls = ["http://playnomore.co.kr/category/bag/24/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
        for parse(self, response):
            links = response.xpath("//*[@id='contents']/div[2]/div/ul/li/div[1]/a/@href").extract()
            links = list(map(lambda data:response.urljoin(data),links))
            for link in links 
                yeild scrapy.Request(link, callback(self.parse_content))
    def parse_content(self, response):
        item = PlaynomoreItem()
        title1 = response.xpath("//*[@id=contents]/div[1]/div[1]/div[2]/div[1]/font/text()")[0].extract()
        title2 = response.xpath("//*[@id='contents]/div[1]/div[1]/div[2]/div[1]/text()").extract()
        title = title1 + " " .join(title2)
        price =response.xpath("//*[@id='contents']/div[1]/div[1]/div[2]/div[2]/text").extract()
        img = response.xpath('//*[@id="contents"]/div[1]/div[1]/div[1]/div[2]/ul/li[6]/img/@src').extract()
        yield item
