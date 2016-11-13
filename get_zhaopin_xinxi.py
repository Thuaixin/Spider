from bs4 import BeautifulSoup
import requests
import pymongo
import time
import requests.packages.urllib3.exceptions
from urllib.error import HTTPError
from datetime import datetime
import random
import socket
from get_xiciIP import get_xiciip

client = pymongo.MongoClient('localhost', 27017)
ganji_zhaopin = client['ganji_zhaopin']
zhaopin_xinxi = ganji_zhaopin['zhaopin_xinxi']
zhaopin_xinxi_url = ganji_zhaopin['zhaopin_xinxi_url']
_ip = ganji_zhaopin['_ip']
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}


start_time = datetime.now()
def get_zhaopin_xinxi(zhaopin_xinxi_url): #记得加入招聘分类
    now_time = datetime.now()
    if isinstance(((now_time - start_time).seconds/900), int):
        print('已运行15分钟，现在开始休息150s')
        time.sleep(150)
    elif isinstance(((now_time - start_time).seconds/900), float):
        if list(zhaopin_xinxi.find({ 'zhaopin_xinxi_url' :zhaopin_xinxi_url[0]})) ==[]:
            while int(_ip.find({'title': None}).count()) <= 20:
                print('正在获取可用代理IP，请稍后！')
                get_xiciip(2)
            proxy_ip = random.choice([i['IP'] for i in _ip.find({'title': None})])
            proxies = {'http' : proxy_ip}
            i = 1
            while i :
                try:
                    time.sleep(4)
                    # print(zhaopin_xinxi_url[0])
                    req_xinxi = requests.get(zhaopin_xinxi_url[0], headers = headers, proxies = proxies, timeout = 20)
                except (ConnectionError, ConnectionResetError, requests.exceptions.ProxyError, requests.packages.urllib3.exceptions.MaxRetryError, requests.packages.urllib3.exceptions.NewConnectionError, ConnectionRefusedError):
                    print('IP被封')
                    _ip.update({'IP': proxy_ip}, {'$set': {'title': '不可用的'}})
                    time.sleep(5)
                    i = 0
                except socket.error:
                    print('IP超时')
                    _ip.update({'IP': proxy_ip}, {'$set': {'title': '不可用的'}})
                    time.sleep(5)
                    i = 0
                else:
                    soup = BeautifulSoup(req_xinxi.text, 'lxml')
                    if 1:
                        if soup.find('span', 'firm-name'):
                            gongsi_name = soup.select('div.ad-firm-logo > span.firm-name > a')[0].get_text().split('                                        ')[1]
                        else:
                            gongsi_name = ''
                        if soup.find('div', 'rt_txt'):
                            try:
                                gongsi_hangye = soup.select('div.detail-r-companyInfo > div > span > a')[0].get_text()
                                gongsi_xingzhi = soup.select('div.detail-r-companyInfo > div > span > a')[1].get_text()
                                gongsi_guimo = soup.select('div.detail-r-companyInfo > div > span')[-1].get_text()
                            except IndexError:
                                gongsi_hangye = ''
                                gongsi_xingzhi = ''
                                gongsi_guimo = ''
                        else:
                            gongsi_xingzhi = ''
                            gongsi_hangye = ''
                            gongsi_guimo = ''
                        if soup.find('div', 'd-c-left-hear'):
                            title = soup.select('div.l-d-con > div.d-c-left > div.d-c-left-hear > h1')[0].get_text()
                            fabu_time = soup.select('div.l-d-con > div.d-c-left > div.d-c-left-hear > p > span:nth-of-type(1)')[0].get_text()
                            # liulan = soup.select('div.l-d-con > div.d-c-left > div.d-c-left-hear > p > span:nth-of-type(2)')[0].get_text()
                            toudi = soup.select('div.l-d-con > div.d-c-left > div.d-c-left-hear > p > span:nth-of-type(3)')[0].get_text()
                        else:
                            title = ''
                            fabu_time = ''
                            # liulan = ''
                            toudi = ''
                        if soup.find('div', 'l-d-con'):
                            zhiwei = soup.select('div.l-d-con > div.d-c-left > div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(1) > em > a')[0].get_text()
                            money = soup.select('div.l-d-con > div.d-c-left > div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(2) > em')[0].get_text()
                            xueli = soup.select('div.l-d-con > div.d-c-left > div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(3) > em')[0].get_text()
                            jingyan = list(map(lambda x: x.text,soup.select('div.l-d-con > div.d-c-left > div.d-c-left-age.d-c-left-firm.mt-30 > ul > li:nth-of-type(4) > em')))[0]
                        else:
                            zhiwei = ''
                            money = ''
                            xueli = ''
                            jingyan = ''
                        if soup.find('p', 'detail-map-top'):
                            add = soup.select('p.detail-map-top')[0].get_text()
                        else:
                            add = ''
                        zhaopin_xinxi.insert_one({'gongsi_name' : gongsi_name, 'gongsi_xingzhi' : gongsi_xingzhi, 'gongsi_guimo' : gongsi_guimo, 'gongsi_hangye' : gongsi_hangye, 'title' : title, 'fabu_time' : fabu_time,  'toudi' : toudi, 'zhiwei' : zhiwei, 'money' : money, 'xueli' : xueli, 'jingyan' : jingyan, 'add' : add, 'zhaopin_xinxi_url' :zhaopin_xinxi_url[0], 'fenlei' : zhaopin_xinxi_url[1]})
                        req_xinxi.close()
                        print('抓取成功')
                        i = 0
                    else:
                        req_xinxi.close()
                        print('该页面未找到需爬取的信息，请检查是否存在问题，页面是：', zhaopin_xinxi_url[0])
                        i = 0
        else:
            print('该页面已被爬取')


# get_zhaopin_xinxi('http://wh.ganji.com/zpzixunguwen/2282904753x.htm')
