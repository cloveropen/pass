import requests
from bs4 import BeautifulSoup
import motor.motor_asyncio
import asyncio

url = 'https://drugs.dxy.cn/category/1001.htm'
headers = {
    'authority': 'drugs.dxy.cn',
    'method': 'GET',
    'path': '/category/1001.htm?page=28',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'UM_distinctid=17211eb0f4784a-0bf1f3f4f51738-d373666-2a3000-17211eb0f487d6; _ga=GA1.2.842680072.1589438496; __auc=0b75ef1517211eba8de46c132b4; DXY_USER_GROUP=29; __utmz=129582553.1589442827.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=1.842680072.1589438496.1593597052.1593597052.1; __utmz=1.1593597052.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ifVisitOldVerBBS=false; Hm_lvt_8a6dad3652ee53a288a11ca184581908=1598346986; _gid=GA1.2.1586522370.1598410731; CLASS_CASTGC=1774de57b74c310b8a3027bbf234a812204b8a010eb5555197cec2f71395e888c4dffd3917b15a5d96a94f19f63c2fff4a97ea26e362d93847c242bf7db5b5a5a62cde8be94fdc8c95b55ca2da19de560063699354becdb1527c223ef72b2f9abad3ebfe3b53d16f8f8355dc8a1f9bbb2a6c9ac1dd7aa0ef898f6223b276f230818f0b0f5c74dfa00581d4b53a4e3e05ccf94a62a409e76e531d445a4cb0f6bc3c98391463bd45801f14085cd9bb4301969c0253d39e62a896fcc7badcdb0cb933918a498544c8d95ec6e34ed3ee622bffe5b184204b804b07386b3a5aa0bec821fd5dec356e011e8c007160aca782c6240c5df8315c81aabaa8c62c9ade11a1; JUTE_BBS_DATA=4b462e5127c88dcbba8dd2ed5fce26d9d4a0d7cf906a0bebc329e3b2578a37bd6386e3d0f4dff4e43ded3de51bfd1c700b2fc6773f17782a1b13401a88e600efa45217e9b16006f16d814f0221b58157d1331d3bbe84b33a00d3a5c8ef8892e9c70e2957a42b138a; route=76fe8badbf970cea48a83fee22e3ae12; DRUGSSESSIONID=D51A0B791036A4C8F8D6333394C1D9E2-n1; __asc=1baa89a61742daa042361f2b642; __utma=129582553.842680072.1589438496.1598431542.1598493951.54; __utmc=129582553; Hm_lvt_d1780dad16c917088dd01980f5a2cfa7=1598398824,1598410914,1598420339,1598493951; Hm_lpvt_d1780dad16c917088dd01980f5a2cfa7=1598494237; __utmb=129582553.17.10.1598493951',
    'dnt': '1',
    'referer': 'https://drugs.dxy.cn',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}

db_uri = "mongodb://drug:你的密码@ip:27017/drug"
db_conn_args = {
    "zlibCompressionLevel": 7,
    "compressors": "zlib"
}

# 获取网页数据
def get_html(url: str, headers: dict) -> str:
    r = requests.get(url, headers)
    html = ''
    if r.status_code == 200:
        html = r.text
        print(html)
    return html

# 解析药品名称_厂家
async def parse_drug_factory(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    top_elm = soup.find('div', attrs={'id': 'container'})
    #print(soup.prettify())
    soup1 = BeautifulSoup(str(top_elm), 'html.parser')
    elems = soup1.findAll('div', attrs={'class': 'fl'})
    #print(type(elems))
    i = 0
    tcate_name = ''
    for tvalue in elems:
        # 获取药品名称-生产厂家  商品名  成分 适应症
        #print(tvalue.string)
        #print(tvalue.contents)
        if tvalue.string !=None:
            #是表头分类
            tcate_name = tvalue.string
        else:
            #print(str(tvalue.contents))
            tstr = str(tvalue.contents)
            #提取url链接
            tbnum:int = tstr.find("href=",0)
            tstr = tstr[tbnum + 6:len(tstr)]
            tenum: int = tstr.find("\"",0)
            turl = tstr[0:tenum]
            print("turl="+turl)
            tstr = tstr[tenum+1:]
            # 提取药品名-生产厂家
            tenum = tstr.find("</a>")
            tcname = tstr[0:tenum].replace("\t","").replace(" ","")
            print("tcname="+tcname)
            # 提取商品名
            tstr = tstr[tenum+4:]
            soup2 = BeautifulSoup(tstr, 'html.parser')
            elems2 = soup2.find('b')
            ttrade_name_title: str = elems2.text
            print("ttrade_name_title="+ttrade_name_title)
            tenum = tstr.find("</b>")
            tstr = tstr[tenum + 4:]
            tenum = tstr.find("<b>")
            ttrade_name_cont: str = tstr[0:tenum].replace("\t","").replace(" ","")
            print("ttrade_name_cont=" + ttrade_name_cont)
            '''#提取成份
            elems2 = BeautifulSoup(tstr, 'html.parser').find('b')
            tcont_title:str = elems2.text
            print("tcont_title=" + tcont_title)
            tenum = tstr.find("</b>")
            tstr = tstr[tenum + 4:]
            tenum = tstr.find("</b>")
            tcont_conts: str = tstr[0:tenum].replace("\t", "").replace(" ", "")
            print("tcont_cont=" + tcont_conts)
            # 提取适应症
            elems2 = BeautifulSoup(tstr, 'html.parser').find('b')
            tindications_title: str = elems2.text
            print("tindications_title=" + tindications_title)
            tenum = tstr.find("</b>")
            tstr = tstr[tenum + 4:]
            tenum = tstr.find("</p>")
            tindications_conts: str = tstr[0:tenum].replace("\t", "").replace(" ", "")
            print("tindications_conts=" + tindications_conts)
'''
            print("tstr=" + tstr)
            print("---------------------")
        print(str(i) * 12+tcate_name)
        i = i +1
    #tclass1_str = str(elems.contents)

    #print(tclass1_str)
    print('----------------------------')
    '''result = re.split('\\n', tclass1_str)
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
            result = await db.drug_list.insert_one(document)
            print('result %s' % repr(result.inserted_id))
'''
async def main():
    html = get_html(url, headers)
    await parse_drug_factory(html)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
