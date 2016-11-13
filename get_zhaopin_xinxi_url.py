from bs4 import BeautifulSoup
import requests
import pymongo
import time
import random
from urllib.error import HTTPError
import socket
from get_xiciIP import get_xiciip
import requests.packages.urllib3.exceptions

client = pymongo.MongoClient('localhost', 27017)
ganji_zhaopin = client['ganji_zhaopin']
zhaopin_xinxi_url = ganji_zhaopin['zhaopin_xinxi_url']
_ip = ganji_zhaopin['_ip']
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.87 Safari/537.36 QQBrowser/9.2.5748.400'
}


# def get_zhaopin_xinxi_url(fenlei): #fenlei = (fenlei_list, fenlei_url_list)
#     for page in range(1, 80):
#         print('现在页面：', page)
#         while int(_ip.find({'title' : None}).count()) <= 20:
#             print('正在获取可用代理IP，请稍后！')
#             get_xiciip(3)
#         proxy_ip = random.choice([i['IP'] for i in _ip.find({'title' : None})])
#         if list(_ip.find({'IP' : proxy_ip, 'title' : '不可用的'})) == []:
#             proxies = {'http': proxy_ip}
#             fenlei_url = fenlei[1] + 'o{}/'.format(page)
#             time.sleep(8)
#             try:
#                 req_fenlei_url = requests.get(fenlei_url, headers=headers, proxies = proxies, timeout = 20)
#             except (requests.packages.urllib3.exceptions.ProtocolError, requests.exceptions.ConnectionError, UnboundLocalError,HTTPError, ConnectionError, ConnectionResetError, requests.exceptions.ProxyError, requests.packages.urllib3.exceptions.MaxRetryError, requests.packages.urllib3.exceptions.NewConnectionError, ConnectionRefusedError, requests.exceptions.ChunkedEncodingError):
#                 # req_fenlei_url.close()
#                 print('测试失败（ip被封）')
#                 _ip.update({'IP' : proxy_ip}, {'$set' : {'title' : '不可用的'}})
#                 # time.sleep(100)
#                 continue
#             except socket.error:
#                 print('测试失败（ip超时）')
#                 _ip.update({'IP': proxy_ip}, {'$set': {'title': '不可用的'}})
#                 continue
#             # except TimeoutError:
#             #     req_fenlei_url.close()
#             #     ip_list.remove(proxy_ip)
#             #     time.sleep(100)
#             #     continue
#             # except ConnectionError:
#             #     req_fenlei_url.close()
#             #     ip_list.remove(proxy_ip)
#             #     time.sleep(100)
#             #     continue
#             # except ConnectionResetError:
#             #     req_fenlei_url.close()
#             #     ip_list.remove(proxy_ip)
#             #     time.sleep(100)
#             #     continue
#             # except requests.exceptions.ProxyError:
#             #     req_fenlei_url.close()
#             #     ip_list.remove(proxy_ip)
#             #     time.sleep(100)
#             #     continue
#             # except requests.packages.urllib3.exceptions.MaxRetryError:
#             #     req_fenlei_url.close()
#             #     ip_list.remove(proxy_ip)
#             #     time.sleep(100)
#             #     continue
#             # except requests.packages.urllib3.exceptions.NewConnectionError:
#             #     req_fenlei_url.close()
#             #     ip_list.remove(proxy_ip)
#             #     time.sleep(100)
#             #     continue
#             # except ConnectionRefusedError:
#             #     req_fenlei_url.close()
#             #     ip_list.remove(proxy_ip)
#             #     time.sleep(100)
#             #     continue
#             print('测试成功')
#             soup = BeautifulSoup(req_fenlei_url.text, 'lxml')
#             if soup.find('a', 'list_title'):
#                 for xinxi_url in soup.select('dl.list-noimg.job-list.clearfix > dt > a.list_title.gj_tongji'):
#                     xinxi_url = xinxi_url.get('href')
#                     if list(zhaopin_xinxi_url.find({'xinxi_url': xinxi_url})) != []:
#                         req_fenlei_url.close()
#                         continue
#                     else:
#                         zhaopin_xinxi_url.insert_one({'xinxi_url': xinxi_url, 'fenlei': fenlei[0]})
#                         req_fenlei_url.close()
#                         continue
#             else:
#                 req_fenlei_url.close()
#                 break
#         else:
#             print('错误')

# def get_zhaopin_xinxi_url(fenlei): #fenlei = (fenlei_list, fenlei_url_list)
#     for page in range(1, 80):
#         fenlei_url = fenlei[1] + 'o{}/'.format(page)
#         time.sleep(5)
#         try:
#             req_fenlei_url = requests.get(fenlei_url, headers=headers)
#         except HTTPError:
#             req_fenlei_url.close()
#             time.sleep(40)
#             continue
#         if req_fenlei_url.status_code != 200:
#             req_fenlei_url.close()
#             time.sleep(61)
#             continue
#         else:
#             # time.sleep(2)
#             soup = BeautifulSoup(req_fenlei_url.text, 'lxml')
#             if soup.find('a', 'list_title'):
#                 for xinxi_url in soup.select('dl.list-noimg.job-list.clearfix > dt > a.list_title.gj_tongji'):
#                     xinxi_url = xinxi_url.get('href')
#                     if list(zhaopin_xinxi_url.find({'xinxi_url': xinxi_url})) != []:
#                         req_fenlei_url.close()
#                         continue
#                     else:
#                         zhaopin_xinxi_url.insert_one({'xinxi_url': xinxi_url, 'fenlei': fenlei[0]})
#                         req_fenlei_url.close()
#             else:
#                 req_fenlei_url.close()
#                 break
    # try:
    #     req_fenlei_url = requests.get(fenlei_url, headers = headers)
    #     if req_fenlei_url.status_code == 404:
    #         pass
    #     else:
    #         # time.sleep(2)
    #         soup = BeautifulSoup(req_fenlei_url.text, 'lxml')
    #         if soup.find('a', 'list_title'):
    #             for xinxi_url in soup.select('dl.list-noimg.job-list.clearfix > dt > a.list_title.gj_tongji'):
    #                 xinxi_url = xinxi_url.get('href')
    #                 if zhaopin_xinxi_url.find({'xinxi_url': xinxi_url}):
    #                     pass
    #                 else:
    #                     zhaopin_xinxi_url.insert_one({'xinxi_url': xinxi_url, 'fenlei': fenlei[0]})
    #         else:
    #             pass
    #         req_fenlei_url.close()
    # except ConnectionResetError:
    #     print('10054错误')



    # if req_fenlei_url.status_code == 404:
    #     pass
    # else:
    #     #time.sleep(2)
    #     soup = BeautifulSoup(req_fenlei_url.text, 'lxml')
    #     if soup.find('a', 'list_title'):
    #         for xinxi_url in soup.select('dl.list-noimg.job-list.clearfix > dt > a.list_title.gj_tongji'):
    #             xinxi_url = xinxi_url.get('href')
    #             if zhaopin_xinxi_url.find({'xinxi_url' : xinxi_url}):
    #                 pass
    #             else:
    #                 zhaopin_xinxi_url.insert_one({'xinxi_url': xinxi_url, 'fenlei': fenlei[0]})


# print(list(zhaopin_xinxi_url.find({'xinxi_url': "http://wh.ganji.com/zptaobao/2338795832x.htm"})))

def get_zhaopin_xinxi_url(fenlei): #fenlei = (fenlei_list, fenlei_url_list)
    page = 1
    while page <= 80:
        print('现在页面：', page)
        while int(_ip.find({'title' : None}).count()) <= 20:
            print('正在获取可用代理IP，请稍后！')
            get_xiciip(3)
        proxy_ip = random.choice([i['IP'] for i in _ip.find({'title' : None})])
        proxies = {'http': proxy_ip}
        fenlei_url = fenlei[1] + 'o{}/'.format(page)
        time.sleep(4)
        try:
            req_fenlei_url = requests.get(fenlei_url, headers=headers, proxies = proxies, timeout = 20)
        except (requests.packages.urllib3.exceptions.ProtocolError, requests.exceptions.ConnectionError, UnboundLocalError,HTTPError, ConnectionError, ConnectionResetError, requests.exceptions.ProxyError, requests.packages.urllib3.exceptions.MaxRetryError, requests.packages.urllib3.exceptions.NewConnectionError, ConnectionRefusedError, requests.exceptions.ChunkedEncodingError):
            print('测试失败（ip被封）')
            _ip.update({'IP' : proxy_ip}, {'$set' : {'title' : '不可用的'}})
            page = page
            print('IP被封时page:', page)
        except socket.error:
            print('测试失败（ip超时）')
            _ip.update({'IP': proxy_ip}, {'$set': {'title': '不可用的'}})
            page = page
            print('IP超时时page:', page)
        else:
            print('IP测试成功')
            soup = BeautifulSoup(req_fenlei_url.text, 'lxml')
            if soup.find('a', 'list_title'):
                for xinxi_url in soup.select('dl.list-noimg.job-list.clearfix > dt > a.list_title.gj_tongji'):
                    xinxi_url = xinxi_url.get('href')
                    if list(zhaopin_xinxi_url.find({'xinxi_url': xinxi_url})) != []:
                        print('存在相同信息')
                        continue
                    else:
                        zhaopin_xinxi_url.insert_one({'xinxi_url': xinxi_url, 'fenlei': fenlei[0]})
                        print('已存入数据库')
                        continue
                req_fenlei_url.close()
                print('该页面抓取完毕, page : ', page)
                page = page + 1
            else:
                req_fenlei_url.close()
                print('所有页面抓取完毕, page : ', page)
                page = page + 1
