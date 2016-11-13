from multiprocessing import Pool
from get_zhaopin_xinxi_url import get_zhaopin_xinxi_url, zhaopin_xinxi_url
from get_zhaopin_xinxi import get_zhaopin_xinxi
from get_fenlei import fenlei
import time

# def all_links(fenlei):
#     for i in range(10, 80):
#         get_zhaopin_xinxi_url(fenlei, i)


# if __name__ == '__main__':
#     # pool = Pool()
#     # for item in fenlei:
#     #     time.sleep(5)
#     #     get_zhaopin_xinxi_url(item)
#     for item1 in [item['xinxi_url'] for item in zhaopin_xinxi_url.find()]: # 从招聘信息网站获取信息
#         time.sleep(4)
#         get_zhaopin_xinxi(item1)
#     # map(get_zhaopin_xinxi, [item['xinxi_url'] for item in zhaopin_xinxi_url.find()])

if __name__ == '__main__':
    pool = Pool()
    # pool.map(get_zhaopin_xinxi_url, fenlei) # 获取招聘信息网站
    pool.map(get_zhaopin_xinxi, [[item['xinxi_url'], item['fenlei']] for item in zhaopin_xinxi_url.find()]) # 从招聘信息网站获取信息