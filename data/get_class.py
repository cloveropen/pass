import asyncio

import requests
#import pandas as pd
from bs4 import BeautifulSoup
import re
import motor.motor_asyncio
import time

url = 'https://drugs.dxy.cn/'
headers = {
    'authority': 'drugs.dxy.cn',
    'method': 'GET',
    'path': '/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'UM_distinctid=17211eb0f4784a-0bf1f3f4f51738-d373666-2a3000-17211eb0f487d6; _ga=GA1.2.842680072.1589438496; __auc=0b75ef1517211eba8de46c132b4; DXY_USER_GROUP=29; __utmz=129582553.1589442827.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=1.842680072.1589438496.1593597052.1593597052.1; __utmz=1.1593597052.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); CLASS_CASTGC=8ba176403eb7d66229dc893aef8841d2d056ac5631702a4680a25b211275ea938014b83bab7ebe994b66311f0d8e9dba0197efa6e607efa49d1de39ea6bb257636ad1a4a82c554ce410ecbbdbc7a2993fb5f4b53f65f90470cb69fccb0abc44cdddbf9b984a4c149b511723f0b5b6218f20e1b47e017b5b026afaeccf654084f36035aed5320ee16deadf10f17fce7e72ad06a98a369ba3ae94e8537ace30ab483c150dcf1b9e42bbb57f075594ca8eb898804926c2d123431cfd5ad14b9e04d36038e2f0e8b9489ee00b1cce04a4f99974ac72aa737ec0696b88bb1c6dc6e4001de41f1080e1b5a988f337793b35755d290f42c22d786bdfe5b7f43c25edde8; JUTE_BBS_DATA=714d1c4fc79c9a99fe623d1e3d0d2af34283154a41ff4be4d7afbea567c9606258ec724d5153485791ef9d4cd5eadc54665580b9bf1e5e66afae7c841721e9f9e52ba7fc3df62fee0fc1cc06ad8ec647e4c976c4501ca5483ce03bf22d6627d488dbda3acdb93f2c; JUTE_SESSION_ID=13d9ea1e-03bf-4314-b0d3-89ac6ff83e1d; ifVisitOldVerBBS=false; Hm_lvt_8a6dad3652ee53a288a11ca184581908=1598346986; route=76fe8badbf970cea48a83fee22e3ae12; DRUGSSESSIONID=229E7EFE4E8709B0FED740F81592DA2E-n1; __asc=eb9cfa0117427fe71100703333e; __utma=129582553.842680072.1589438496.1593734390.1598398821.47; __utmc=129582553; __utmt=1; Hm_lvt_d1780dad16c917088dd01980f5a2cfa7=1598344919,1598398824; __utmb=129582553.2.10.1598398821; Hm_lpvt_d1780dad16c917088dd01980f5a2cfa7=1598398826',
    'dnt': '1',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}
headers1 = {
    'authority': 'drugs.dxy.cn',
    'method': 'GET',
    'path': '/drug/101754.htm',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'UM_distinctid=17211eb0f4784a-0bf1f3f4f51738-d373666-2a3000-17211eb0f487d6; _ga=GA1.2.842680072.1589438496; __auc=0b75ef1517211eba8de46c132b4; DXY_USER_GROUP=29; __utmz=129582553.1589442827.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=1.842680072.1589438496.1593597052.1593597052.1; __utmz=1.1593597052.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ifVisitOldVerBBS=false; Hm_lvt_8a6dad3652ee53a288a11ca184581908=1598346986; route=76fe8badbf970cea48a83fee22e3ae12; __utmc=129582553; __asc=b404134017428934d5fa7cd7401; __utma=129582553.842680072.1589438496.1598401172.1598408578.49; DRUGSSESSIONID=6DEAFDA2DCA14672582D5E9CF79BE790-n1; _gid=GA1.2.1586522370.1598410731; CLASS_CASTGC=1774de57b74c310b8a3027bbf234a812204b8a010eb5555197cec2f71395e888c4dffd3917b15a5d96a94f19f63c2fff4a97ea26e362d93847c242bf7db5b5a5a62cde8be94fdc8c95b55ca2da19de560063699354becdb1527c223ef72b2f9abad3ebfe3b53d16f8f8355dc8a1f9bbb2a6c9ac1dd7aa0ef898f6223b276f230818f0b0f5c74dfa00581d4b53a4e3e05ccf94a62a409e76e531d445a4cb0f6bc3c98391463bd45801f14085cd9bb4301969c0253d39e62a896fcc7badcdb0cb933918a498544c8d95ec6e34ed3ee622bffe5b184204b804b07386b3a5aa0bec821fd5dec356e011e8c007160aca782c6240c5df8315c81aabaa8c62c9ade11a1; JUTE_BBS_DATA=4b462e5127c88dcbba8dd2ed5fce26d9d4a0d7cf906a0bebc329e3b2578a37bd6386e3d0f4dff4e43ded3de51bfd1c700b2fc6773f17782a1b13401a88e600efa45217e9b16006f16d814f0221b58157d1331d3bbe84b33a00d3a5c8ef8892e9c70e2957a42b138a; Hm_lvt_d1780dad16c917088dd01980f5a2cfa7=1598344919,1598398824,1598410914; Hm_lpvt_d1780dad16c917088dd01980f5a2cfa7=1598411165; __utmt=1; __utmb=129582553.18.10.1598408578',
    'dnt': '1',
    'referer': 'https://drugs.dxy.cn/category/1227.htm',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
}

db_uri = "mongodb://drug:eastwillpass58@121.36.48.65:27017/drug"
db_conn_args = {
                    "zlibCompressionLevel": 7,
                    "compressors": "zlib"
                }
# 获取网页数据
def get_html(url: str, headers: dict) -> str:
    r = requests.get(url, headers1)
    html = ''
    if r.status_code == 200:
        html = r.text
        # print(html)
    return html


# 解析一级药理分裂
async def parse_class1(html: str):
    # dfs = pd.read_html(html,attrs={'class':'sidemenu'})
    # print(dfs[0])

    htmlSoup = BeautifulSoup(html, 'html.parser')
    elems = htmlSoup.find('div', attrs={'class': 'sidemenu'})
    tclass1_str = str(elems.contents)

    print(tclass1_str)
    print('----------------------------')
    result = re.split('\\n', tclass1_str)
    print(result)
    print('----------------------------')
    for value in result:
        if value.startswith("<li"):
            tcode = re.findall(r'\d+', value)[0]
            print(tcode)
            hSoup = BeautifulSoup(value, 'html.parser')
            telm = hSoup.find('li')
            tname = telm.get_text()
            print(tname)
            # 写入mongodb
            client = motor.motor_asyncio.AsyncIOMotorClient(db_uri, **db_conn_args)
            db = client.get_database("drug")
            document = {'code': tcode, 'cname': tname}
            result = await db.class1.insert_one(document)
            print('result %s' % repr(result.inserted_id))

# 解析二级药理分类
async def parse_class2(html: str):
    htmlSoup = BeautifulSoup(html, 'html.parser')
    elems = htmlSoup.find('div', attrs={'class': 'common_main ml279'})

    i = 0
    for value in elems.contents:
        # print(value)
        # print(str(i)+'----------------------------'+str(type(value)))
        if str(value) == '':
            continue
        hSoup = BeautifulSoup(str(value), 'html.parser')
        elm = hSoup.find_all('h3')
        # print('0000000000000000000000000'+str(type(elm)))
        if elm is None:
            print('-')
        else:
            # print(elm.contents)
            for tvalue2 in elm:
                tout_str = str(tvalue2).replace("h3", "")
                # print(str(type(tvalue2))+"__"+tout_str)
                tcode = re.findall(r'\d+', tout_str)[0]
                print(tcode)
                tname = tvalue2.get_text()
                print(tname)
                i = i + 1
                # 写入mongodb数据库
                connection_args = {
                    "zlibCompressionLevel": 7,
                    "compressors": "zlib"
                }
                client = motor.motor_asyncio.AsyncIOMotorClient(db_uri, **db_conn_args)
                db = client.get_database("drug")
                document = {'code': tcode,'cname':tname}
                result = await db.class2.insert_one(document)
                print('result %s' % repr(result.inserted_id))

        print(str(i) * 10)


async def main():
    html = get_html(url, headers1)
    await parse_class1(html)

    # await parse_class2(html)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

