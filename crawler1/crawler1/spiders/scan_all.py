import scrapy

class PostSpider(scrapy.Spider):
    name="posts2"
    start_urls=[
        'http://blog.scrapinghub.com/'
    ]

    def parse(self, response):
        for post in response.css('div.post-item'):
            yield {
                'title': post.css('.post-header h2 a::text')[0].get(),
                'date' : post.css('.post-header a::text')[1].get()
            }


# scrapy crawl posts -o posts.json
#scrapy shell https://blog.scrapinghub.com
 # response.css('title')
# response.css('title').get()
# response.css('title::text').get()
#response.css('h2::text').get()
#response.css('h2::text').get()
# response.css('h2::text').getall()
# response.css('h2::text').getall()
#response.css('.post-header a::text').getall()
#response.css('p::text').re(r'(\w+) you (\w+)')
# post=response.css('div.post-item')[0]
# post.css('.post-header h2 a::text').get()

