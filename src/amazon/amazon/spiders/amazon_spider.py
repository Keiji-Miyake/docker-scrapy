import scrapy


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.co.jp']
    start_urls = [
        'https://www.amazon.co.jp/dp/4802611080',
        'https://www.amazon.co.jp/dp/480261179X'
    ]

    def parse(self, response):
        ranking = response.css('#detailBullets_feature_div')
        yield {'ranking': ranking.get()}
