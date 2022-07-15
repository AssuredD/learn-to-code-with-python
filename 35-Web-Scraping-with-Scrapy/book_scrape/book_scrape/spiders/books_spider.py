from gc import callbacks
import scrapy


class BookSpider(scrapy.Spider):
    name = "books"
    star_urls = [
        "http://books.toscrape.com"
    ]

    # def start_requests(self):
    #     return [
    #         scrapy.Request(url="http://books.toscrape.com",
    #                        callback=self.parse)
    #     ]

    def parse(self, response):
        for entry in response.css("article.product_pod"):
            title = entry.css("h3 a: : attr(title)").get()
            price = entry.css("p.price_color::text").get()
            yield {"title": title, "price": price}

        next_page = response.css("li.next a::attr(href)".get())

        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    # boris.paskhaver@nyu.edu

    # scrapy crawl books -o books.json
