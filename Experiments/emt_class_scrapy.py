import scrapy

class EMTSpider(scrapy.Spider):
    name = 'emt_spider'
    start_urls = ["https://njems.njlincs.net/jsp/rlm/catalog.jsp?pgm_id=62&end_dayrng_id=365"]

    def parse(self, response):
        for a in response.css("tr > td"):
            yield {
                'start_date': a.css('.htmGHOT-row').get(),
            }
