import scrapy


class JobScraperSpider(scrapy.Spider):
    name = "job_scraper"
    allowed_domains = ["in.linkedin.com"]
    start_urls = ["https://in.linkedin.com/"]

    def parse(self, response):
        pass
