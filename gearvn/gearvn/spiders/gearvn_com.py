import scrapy
from ..items import GearvnItem
from scrapfly import ScrapeConfig
from scrapfly.scrapy import ScrapflyMiddleware, ScrapflyScrapyRequest, ScrapflySpider, ScrapflyScrapyResponse

class GearvnComSpider(ScrapflySpider):
    name = 'gearvn.com'
    allowed_domains = ['faf.com']
    start_urls = [
        ScrapeConfig('https://gearvn.com/products/laptop-gaming-acer-aspire-7-a715-42g-r4xx')
    ]

    def parse(self, response: ScrapflyScrapyResponse):
        item = GearvnItem()
        item['name'] = response.xpath('//h1[@class="product_name"]/text()').extract_first()
        item['image_urls'] = ['https://product.hstatic.net/1000026716/product/aspire_a715__3__7cddf7dd053c444f9ca44f30fcd70d67.jpg']
        yield item
