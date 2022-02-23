import scrapy

# Подключили поля Item и импортировали GitParseItem поля
from ..items import GitParseItem

# Даем название нашему проекту и начальный url
class Git_Spider(scrapy.Spider):
    name = 'repository'
    start_urls = ['https://github.com/jmportilla']

# Метод для обработки собранной информации
    def parse(self, response):
        for i in response.css('div.pinned-item-list-item-content a::attr(href)'):
            yield response.follow(i, callback=self.parse_repository)

# Метод для сбора информации с ресурса
    def parse_repository(self, response):
        item = GitParseItem()
        item['name'] = response.css('div.application-main a::text')[1].get(),
        item['link'] = response.css('div.application-main a')[3].get().split()[6].split(',')[3].split('"')[3],
        item['starts'] = response.css('div.application-main span.text-bold::text').get(),
        item['forks'] = response.css('span.text-bold::text')[1].get(),
        item['watching'] = response.css('strong::text')[-2].get(),
        item['commit'] = response.css('div.Layout-main span strong::text').get(),
        item['release'] = response.css('div.BorderGrid-row')[1].get().split('"')[-1].split('>')[1].split('<')[0],
        item['description'] = response.xpath('//*[@id="readme"]/div[2]/article/p/text()').extract()

        yield item
