
import scrapy
from scrapy import Field

'''
Field() Словарь, содержащий все объявленные поля для этого элемента, 
Item - позволяет определять имена полей (name,link и т.д.)
'''

class GitParseItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    starts = scrapy.Field()
    forks = scrapy.Field()
    watching = scrapy.Field()
    commit = scrapy.Field()
    release = scrapy.Field()
    description = scrapy.Field()

