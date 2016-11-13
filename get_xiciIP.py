from bs4 import BeautifulSoup
import requests
import time
from requests import ConnectionError
import socket
import requests.packages.urllib3.exceptions
import pymongo
import random
import sys

client = pymongo.MongoClient('localhost', 27017)
ganji_zhaopin = client['ganji_zhaopin']
_ip = ganji_zhaopin['_ip']
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.87 Safari/537.36 QQBrowser/9.2.5748.400'
}
# 'http://120.132.2.201:9529'
ip_list = []
def get_xiciip(n):
    # ip_list = []
    for i in range(1, n):
        print('测试for循环1 --> i:', i)
        time.sleep(3)
        ip_url = requests.get('http://www.xicidaili.com/{}n/{}/'.format(random.choice(['n', 'w']), i), headers = headers)
        soup = BeautifulSoup(ip_url.text, 'lxml')
        IPS = soup.select('table > tr > td:nth-of-type(2)')
        PORTS = soup.select('table > tr > td:nth-of-type(3)')
        SPEED1 = soup.select('table > tr > td:nth-of-type(7) > div')
        SPEED2 = soup.select('table > tr > td:nth-of-type(8) > div')
        count = 1
        for ip,port,speed1,speed2 in zip(IPS, PORTS, SPEED1, SPEED2):
            print('测试for循环2 --> i:', i, ', 每一页ip数量:', len(IPS), ', count:', count)
            float_speed1 = float(speed1.get('title').split('秒')[0])
            float_speed2 = float(speed2.get('title').split('秒')[0])
            count += 1
            if float_speed1 <= 6 and float_speed2 <= 6:
                proxies = {'http' : 'http://{}:{}'.format(str(ip.get_text()), str(port.get_text()))}
                if list(_ip.find({'IP': "http://{}:{}".format(str(ip.get_text()), str(port.get_text()))})) == []:
                    try:
                        time.sleep(3)
                        req_web = requests.get('http://wh.ganji.com/zhaopin', headers = headers, proxies = proxies, timeout = 10)
                    except (ConnectionRefusedError, ConnectionError, ConnectionResetError, requests.packages.urllib3.exceptions.ProtocolError, requests.exceptions.ChunkedEncodingError):
                        print('测试1 --> ip失效（ip被封）  i:', i)
                        continue
                    except socket.error as e:
                        errno, errstr = sys.exc_info()[:2]
                        if errno == socket.timeout:
                            print('测试1 --> ip失效（超时）  i:', i, e)
                            continue
                        else:
                            print('其他socket错误')
                            continue
                    else:
                        # if list(_ip.find({'IP' : "http://{}:{}".format(str(ip.get_text()), str(port.get_text()))})) == []:
                        _ip.insert_one({'IP' : "http://{}:{}".format(str(ip.get_text()), str(port.get_text()))})
                        ip_list.append('http://{}:{}'.format(str(ip.get_text()), str(port.get_text())))
                        print('测试成功')
                        continue
                else:
                    print('测试2 --> 数据中有重复ip i:', i)
                    continue
            else:
                print('测试3 --> ip速度过小 i:', i)
                continue

    return ip_list

# get_xiciip(2)