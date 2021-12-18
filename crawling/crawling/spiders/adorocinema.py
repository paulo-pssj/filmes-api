import scrapy
from crawling.items import FilmeItem

class AdorocinemaSpider(scrapy.Spider):
    name = 'adorocinema'
    allowed_domains = ['www.adorocinema.com']
    start_urls = ['http://www.adorocinema.com/filmes/numero-cinemas/']

    def __init__(self):
        super().__init__()
        self.URL_BASE = "http://www.adorocinema.com"
        self.URL_SESSAO = "/filmes/numero-cinemas/"
    
    def parse(self, response):
        
        for div in response.xpath("//li[@class='mdl']"):
            movies = FilmeItem()
            link = None
            
            if div.xpath("./div/div/h2/a/@href").get():
                link = self.URL_BASE + div.xpath("./div/div/h2/a/@href").get()
            
            movies['titulo'] = div.xpath("./div/div/h2/a/text()").get()
            movies['link'] = link
            movies['sinopse'] = div.xpath("./div//div[@class='synopsis']/div/text()").get()
            
            
            for page in response.xpath("//div[@class='pagination-item-holder']/a[re:test(@href, 'page')]/@href").getall():
                yield scrapy.Request(self.URL_BASE + page, callback=self.parse)
            
            yield movies
