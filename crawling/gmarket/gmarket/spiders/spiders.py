import scrapy
from gmarket.items import GmarketItem

class Spider(scrapy.Spider):#여러게 크롤링하고 싶다면 스파이더 추가
    
    name = "GmarketBestSellers"
    allow_domain=["gmarket.co.kr"]
    start_urls= ["http://corners.gmarket.co.kr/Bestsellers"] #처음 시작하는 url
    
    def parse(self, response):
        links = response.xpath(
            "//*[@id='gBestWrap']/div/div[3]/div[2]/ul/li[1]/div[1]/a/@href").extract()
        for link in links: 
            yield scrapy.Request(link, callback=self.parse_content)#yield 
    def parse_content(self, response):
        item = GmarketItem()
        item["title"] = response.xpath('//*[@id="itemcase_basic"]/h1/text()')[0].extract().strip()
        item["s_price"]=response.xpath('//*[@id="itemcase_basic"]/h1/text()')[0].extract().strip()
        
        try:
            item["o_price"]=response.xpath('//*[@id="itemcase_basic"]/p/span/span/text()')[0].extract().strip()
        except:
            item["o_price"]=item["s_price"]
        item["link"]= response.url
        yield item
