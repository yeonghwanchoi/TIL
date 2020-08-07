import scrapy
from incruit.items import IncruitItem

class Spider(scrapy.Spider):
    name = "Incruit"
    allow_domain = ["https://www.incruit.com/"]
    start_urls = ["http://people.incruit.com/resumeguide/pdslist.asp?page=1\
    &listseq=1&sot=&pds1=1&pds2=11&pds3=&pds4=&schword=&rschword=&lang=&price=&occu_b_group=150&occu_m_group=&occu_s_group=&career=&pass=Y&compty=&rank=&summary=&goodsty="]

    def parse(self, response):
        links = response.xpath('//*[@id="content"]/div[7]/table/tbody/tr/td[2]/a/@href').extract()
        links = [response.urljoin(link) for link in links]       
        for link in links:
            yield scrapy.Request(link, callback=self.parse_content)

    def parse_content(self, response):
        item = IncruitItem()
        item["contents"] = response.xpath('//*[@id="detail_info"]/span[2]/p/text()')[0].extract()
        item["title"] = response.xpath('//*[@id="detail_info"]/span[2]/div/p[2]/span/strong/span/text()'.format())[0].extract()
        yield item
