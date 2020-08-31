import scrapy

class PostSpider(scrapy.Spider):
    name="posts"
    start_urls=['http://blog.scrapinghub.com/page/1/',
                'http://blog.scrapinghub.com/page/2/'
    ]

    def parse(self,response):
        page = response.url.split('/')[-1]
        filename = 'post-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)


# scrapy crawl posts
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
