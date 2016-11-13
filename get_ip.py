from bs4 import BeautifulSoup
import requests
import time
from requests import ConnectionError
import requests.packages.urllib3.exceptions
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ganji_zhaopin = client['ganji_zhaopin']
_ip = ganji_zhaopin['_ip']
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.87 Safari/537.36 QQBrowser/9.2.5748.400'
}
# 'http://120.132.2.201:9529'
ip_list = []
def get_ip(n):
    # ip_list = []
    for i in range(1, n):
        time.sleep(3)
        ip_url = requests.get('http://www.kuaidaili.com/proxylist/{}/'.format(i), headers = headers)
        soup = BeautifulSoup(ip_url.text, 'lxml')
        IPS = soup.select('table > tbody > tr > td:nth-of-type(1)')
        PORTS = soup.select('table > tbody > tr > td:nth-of-type(2)')
        for ip,port in zip(IPS, PORTS):
            proxies = {'http' : 'http://{}:{}'.format(str(ip.get_text()), str(port.get_text()))}
            if list(_ip.find({'IP': "http://{}:{}".format(str(ip.get_text()), str(port.get_text()))})) == []:
                try:
                    time.sleep(3)
                    req_web = requests.get('http://wh.ganji.com/zhaopin', headers = headers, proxies = proxies)
                except (ConnectionRefusedError, ConnectionError, ConnectionResetError, requests.packages.urllib3.exceptions.ProtocolError, requests.exceptions.ChunkedEncodingError):
                    continue
                else:
                    # if list(_ip.find({'IP' : "http://{}:{}".format(str(ip.get_text()), str(port.get_text()))})) == []:
                    _ip.insert_one({'IP' : "http://{}:{}".format(str(ip.get_text()), str(port.get_text()))})
                    ip_list.append('http://{}:{}'.format(str(ip.get_text()), str(port.get_text())))
            else:
                continue

    return ip_list

# get_ip(10)
# print(ip_list)
