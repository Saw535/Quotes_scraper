import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        quotes = []
        authors = {}

        for quote in response.css("div.quote"):
            quote_data = {
                "tags": quote.css("meta.keywords::attr(content)").get().split(", "),
                "author": quote.css("span small::text").get(),
                "quote": quote.css("span.text::text").get()
            }
            quotes.append(quote_data)

            author_name = quote_data["author"]
            if author_name not in authors:
                authors[author_name] = {
                    "fullname": author_name,
                    "born_date": "",
                    "born_location": "",
                    "description": ""
                }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
        else:
            with open("quotes.json", "w") as quotes_file:
                json.dump(quotes, quotes_file, indent=4)
            with open("authors.json", "w") as authors_file:
                authors_data = list(authors.values())
                json.dump(authors_data, authors_file, indent=4)