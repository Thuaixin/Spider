from bs4 import BeautifulSoup
import requests
import pymongo
import time

url = 'http://wh.ganji.com/zhaopin'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}

def get_zhaopin_fenlei(url):
    req_url = requests.get(url, headers = headers)
    soup = BeautifulSoup(req_url.text, 'lxml')
    fenlei_list = [i.get_text() for i in soup.select('div.f-all-news > dl > dt > a')]
    fenlei_url_list = ['http://wh.ganji.com'+i.get('href') for i in soup.select('div.f-all-news > dl > dt > a')]
    return fenlei_list,fenlei_url_list

# fenlei_list = get_zhaopin_fenlei(url)[0]
# fenlei_url_list = get_zhaopin_fenlei(url)[1]
fenlei_list = ['销售', '技工/工人', '行政/后勤', '人力资源', '餐饮/酒店', '客服', '淘宝职位', '超市/百货/零售', '家政/安保', '司机', '财务/审计/税务', '房地产中介/经纪/开发', '美容/美发', '保健按摩', '运动健身', '汽车销售与服务', '计算机/网络/通信', '市场/公关/媒介', '广告/会展', '美术/设计/创意', '媒体/影视/表演', '旅游', '金融/投资/证券', '保险', '咨询/顾问', '翻译', '教育/培训', '编辑/出版/印刷', '法律', '贸易/运输/物流', '生产/制造', '电气/能源/动力', '物业管理', '建筑/装修', '机械/仪器仪表', '医药/生物工程', '医院/医疗/护理', '农/林/牧/渔', '环保', '其它']
fenlei_url_list = ['http://wh.ganji.com/zpshichangyingxiao/', 'http://wh.ganji.com/zpjigongyibangongren/', 'http://wh.ganji.com/zpxingzhenghouqin/', 'http://wh.ganji.com/zprenliziyuan/', 'http://wh.ganji.com/zpjiudiancanyin/', 'http://wh.ganji.com/zpkefu/', 'http://wh.ganji.com/zptaobao/', 'http://wh.ganji.com/zpbaihuolingshou/', 'http://wh.ganji.com/zpjiazhenganbao/', 'http://wh.ganji.com/zpsiji/', 'http://wh.ganji.com/zpcaiwushenji/', 'http://wh.ganji.com/zpfangjingjiren/', 'http://wh.ganji.com/zpmeirongmeifazhiwei/', 'http://wh.ganji.com/zpbaojiananmo/', 'http://wh.ganji.com/zpyundongjianshenzhiwei/', 'http://wh.ganji.com/zpqiche/', 'http://wh.ganji.com/zpjisuanjiwangluo/', 'http://wh.ganji.com/zpshichanggongguan/', 'http://wh.ganji.com/zpguanggaohuizhanzhiwei/', 'http://wh.ganji.com/zpmeishusheji/', 'http://wh.ganji.com/zpmeitiyingshi/', 'http://wh.ganji.com/zplvyouzhiwei/', 'http://wh.ganji.com/zpjinrongtouzizhengquan/', 'http://wh.ganji.com/zpbaoxianjingjiren/', 'http://wh.ganji.com/zpzixunguwen/', 'http://wh.ganji.com/zpfanyi/', 'http://wh.ganji.com/zpjiaoyupeixun/', 'http://wh.ganji.com/zpbianjichuban/', 'http://wh.ganji.com/zpfalv/', 'http://wh.ganji.com/zpmaoyiyunshu/', 'http://wh.ganji.com/zpshengchanzhizaozhiwei/', 'http://wh.ganji.com/zpdianqinengyuan/', 'http://wh.ganji.com/zpwuye/', 'http://wh.ganji.com/zpjianzhuzhuangxiu/', 'http://wh.ganji.com/zpjixieyiqiyibiao/', 'http://wh.ganji.com/zpyiyaoshengwu/', 'http://wh.ganji.com/zpyiyuanyiliao/', 'http://wh.ganji.com/zpnonglin/', 'http://wh.ganji.com/zphuanjingbaohu/', 'http://wh.ganji.com/zpqita/']
length = len(fenlei_list)
# fenlei = []
# for a,b in zip(fenlei_list, fenlei_url_list):
#     fenlei.append((a,b))
fenlei = [('广告/会展', 'http://wh.ganji.com/zpguanggaohuizhanzhiwei/'),
          ('美术/设计/创意', 'http://wh.ganji.com/zpmeishusheji/'),
          ('媒体/影视/表演', 'http://wh.ganji.com/zpmeitiyingshi/'),
          ('旅游', 'http://wh.ganji.com/zplvyouzhiwei/'),
          ('保险', 'http://wh.ganji.com/zpbaoxianjingjiren/'),
          ('编辑/出版/印刷', 'http://wh.ganji.com/zpbianjichuban/'),
          ('法律', 'http://wh.ganji.com/zpfalv/'),
          ('贸易/运输/物流', 'http://wh.ganji.com/zpmaoyiyunshu/'),
          ('翻译', 'http://wh.ganji.com/zpfanyi/'),
          ('教育/培训', 'http://wh.ganji.com/zpjiaoyupeixun/'),
          ('咨询/顾问', 'http://wh.ganji.com/zpzixunguwen/'),
          ('金融/投资/证券', 'http://wh.ganji.com/zpjinrongtouzizhengquan/'),
          ('建筑/装修', 'http://wh.ganji.com/zpjianzhuzhuangxiu/'),
          ('计算机/网络/通信', 'http://wh.ganji.com/zpjisuanjiwangluo/'),
          ('销售', 'http://wh.ganji.com/zpshichangyingxiao/'),
          ('技工/工人', 'http://wh.ganji.com/zpjigongyibangongren/'),
          ('行政/后勤', 'http://wh.ganji.com/zpxingzhenghouqin/'),
          ('人力资源', 'http://wh.ganji.com/zprenliziyuan/'),
          ('餐饮/酒店', 'http://wh.ganji.com/zpjiudiancanyin/'),
          ('客服', 'http://wh.ganji.com/zpkefu/'),
          ('淘宝职位', 'http://wh.ganji.com/zptaobao/'),
          ('超市/百货/零售', 'http://wh.ganji.com/zpbaihuolingshou/'),
          ('家政/安保', 'http://wh.ganji.com/zpjiazhenganbao/'),
          ('司机', 'http://wh.ganji.com/zpsiji/'),
          ('财务/审计/税务', 'http://wh.ganji.com/zpcaiwushenji/'),
          ('房地产中介/经纪/开发', 'http://wh.ganji.com/zpfangjingjiren/'),
          ('美容/美发', 'http://wh.ganji.com/zpmeirongmeifazhiwei/'),
          ('保健按摩', 'http://wh.ganji.com/zpbaojiananmo/'),
          ('运动健身', 'http://wh.ganji.com/zpyundongjianshenzhiwei/'),
          ('汽车销售与服务', 'http://wh.ganji.com/zpqiche/'),
          ('市场/公关/媒介', 'http://wh.ganji.com/zpshichanggongguan/'),
          ('生产/制造', 'http://wh.ganji.com/zpshengchanzhizaozhiwei/'),
          ('电气/能源/动力', 'http://wh.ganji.com/zpdianqinengyuan/'),
          ('物业管理', 'http://wh.ganji.com/zpwuye/'),
          ('机械/仪器仪表', 'http://wh.ganji.com/zpjixieyiqiyibiao/'),
          ('医药/生物工程', 'http://wh.ganji.com/zpyiyaoshengwu/'),
          ('医院/医疗/护理', 'http://wh.ganji.com/zpyiyuanyiliao/'),
          ('农/林/牧/渔', 'http://wh.ganji.com/zpnonglin/'),
          ('环保', 'http://wh.ganji.com/zphuanjingbaohu/'),
          ('其它', 'http://wh.ganji.com/zpqita/')]


