import scrapy
from naver_article.items import NaverArticleItem
from selenium import webdriver

class ArticleSpider(scrapy.Spider):
    name = "NaverArticle"
    allow_domain = ["https://news.naver.com"]
    start_urls = ["https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=100"]
    
    def parse(self, response):
        driver = webdriver.Chrome()
        for code in range(100, 106):
            url = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1={}".format(code)
            driver.get(url)
            elements = driver.find_elements_by_xpath('//*[@id="section_body"]/ul/li/dl/dt[2]/a')
            links = [element.get_attribute("href") for element in elements]        
            for link in links:
                yield scrapy.Request(link, callback=self.parse_content)
        driver.quit()
    
    def parse_content(self, response):
        item = NaverArticleItem()
        item['title'] = response.xpath('//*[@id="articleTitle"]/text()')[0].extract()
        item['category'] = response.xpath('//*[@id="lnb"]/ul/li[@class="on"]/a/@href')[0].extract().split("=")[-1]
        content = response.xpath('//*[@id="articleBodyContents"]/text()').extract()
        item['content'] = "".join(content).strip()
        item['link'] = response.url
        yield item
