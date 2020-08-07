import scrapy
from naver_movie.items import NaverMovieItem

class Spider(scrapy.Spider):
    name = "NaverMovie"
    allow_domain = ["https://movie.naver.com"]
    start_urls = ["https://movie.naver.com/movie/running/current.nhn"]
    
    def parse(self, response):
        links = response.xpath(
            '//*[@id="content"]/div[1]/div[1]/div[3]/ul/li/dl/dt/a/@href').extract()    
        links = [response.urljoin(link) for link in links]
        for link in links:
            yield scrapy.Request(link, callback=self.parse_content)
    
    def parse_content(self, response):
        item = NaverMovieItem()
        item["title"] = response.xpath(
            '//*[@id="content"]/div[1]/div[2]/div[1]/h3/a[1]/text()')[0].extract()
        try:
            item["count"] = response.xpath(
                '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[5]/div/p[2]/text()')[0].extract()
        except:
            item["count"] = "0명"
        star = response.xpath(
            '//*[@id="actualPointPersentBasic"]/div/em/text()').extract()
        item["star"] = "".join(star)
        item["link"] = response.url
        yield item
