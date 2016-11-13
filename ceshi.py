import pymongo
import random
import requests
client = pymongo.MongoClient('localhost', 27017)
ganji_zhaopin = client['ganji_zhaopin']
zhaopin_xinxi_url = ganji_zhaopin['zhaopin_xinxi_url']
_ip = ganji_zhaopin['_ip']

# proxy_ip = [i['IP'] for i in _ip.find({'title' : None})]
# print(proxy_ip)
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}
req_url = requests.get('http://wh.ganji.com/zprenliziyuan/2302191528x.htm', headers = headers)


# print(list(_ip.find({"IP" : "http://113.81.64.80:9000", 'titlt' : '不可用的'})))
# a = []
# for i in zhaopin_xinxi_url.find():
#     a.append(i['fenlei'])
#
# print(set(a))
# for i in range (1, 5):
#     print('i:', i)
#     a =3
#     while a:
#         a -= 1
#         print('a', a)
#         i =1
#         global i
#         # i = 1
#         print('i2', i)