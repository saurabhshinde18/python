import scrapy
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get().strip(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

# Run spider directly
if __name__ == '__main__':
    process = CrawlerProcess(settings={
        "FEEDS": {
            "quotes.json": {"format": "json"},
        },
        "LOG_LEVEL": "ERROR",  # Clean output
        "USER_AGENT": "Mozilla/5.0",  # Optional: avoid bot detection
    })
    process.crawl(QuotesSpider)
    process.start()
