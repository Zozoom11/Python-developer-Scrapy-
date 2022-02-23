import pymongo
from scrapy.item import Item

'''
Работа с бд pymongo, подключаемся к бд и передаем в ее инф. 
собранную пауком из item.py (словарь в данном случае)
'''

class MongoDBPipeline(object):
    DB_URI = 'mongodb+srv://pygitscrapy:Y19hWeJKJ14Ryf0x@cluster0.muwwv.mongodb.net/csrapy_db?retryWrites=true&w=majority'
    DB_NAME	= 'csrapy_db'

    def open_spider(self,	spider):
        self.client	= pymongo.MongoClient(self.DB_URI)
        self.db = self.client[self.DB_NAME]

    def	close_spider(self,	spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db['csrapy_db']
        post = dict(item) if isinstance(item, Item) else item
        collection.insert_one(post)
        return item