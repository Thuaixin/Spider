import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
ganji_zhaopin = client['ganji_zhaopin']
zhaopin_xinxi_url = ganji_zhaopin['zhaopin_xinxi_url']
zhaopin_xinxi = ganji_zhaopin['zhaopin_xinxi']
while True:
    time.sleep(5)
    print(zhaopin_xinxi_url.find().count(), zhaopin_xinxi.find().count())
    print('set: ', len(set([i['xinxi_url'] for i in zhaopin_xinxi_url.find()])), len(set([i['zhaopin_xinxi_url'] for i in zhaopin_xinxi.find()])))