import scrapy

class NaverArticleItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    category = scrapy.Field()
    link = scrapy.Field()
