import urllib.request
import urllib.parse
import re
import pymongo
import json
import requests
from lxml import etree

# client=pymongo.MongoClient()
# db=client.investing
# collection=db.stock1


def get_name(search_name):
    # result_list={}
    result_list = []
    j = 1
    url1 = 'https://www.investing.com/equities/%s' % search_name
    url = 'https://www.investing.com/common/modules/js_instrument_chart/api/data.php?pair_id=%s&pair_id_for_news=%s&chart_type=area&pair_interval=86400&candle_count=120&events=yes&volume_series=yes' % (
        pair_id, pair_id)
    headers1 = {
        'Cookie': '__gads=ID=f5089e4f2f622324:T=1498731909:S=ALNI_MZVSEm9TWER8TJlbZZLOzlcGFP0sg; adBlockerNewUserDomains=1498734746; optimizelyEndUserId=oeu1498734748818r0.4865568312206183; editionPostpone=1498734756238; __qca=P0-364377178-1498734759859; travelDistance=4; searchedResults=[{"pairId":944403,"link":"/equities/iflytek-a","symbol":"002230","name":"Iflytek%20Co%20Ltd","type":"Equity%20-%20Shenzhen","flag":"China"}]; PHPSESSID=ac4l8ih6l1qqf5aj7p3e9c7ll2; geoC=CN; gtmFired=OK; StickySession=id.19653929255.124.www.investing.com; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A3%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22102047%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A29%3A%22%2Fequities%2Ftencent-holdings-hk%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A3%3A%22178%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A20%3A%22%2Findices%2Fjapan-ni225%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22944403%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fequities%2Fiflytek-a%22%3B%7D%7D%7D%7D; optimizelySegments=%7B%224225444387%22%3A%22gc%22%2C%224226973206%22%3A%22direct%22%2C%224232593061%22%3A%22false%22%2C%225010352657%22%3A%22none%22%7D; optimizelyBuckets=%7B%228455380705%22%3A%228457490131%22%7D; billboardCounter_1=0; nyxDorf=MTUzYGUyP30%2FYW5ibiMyMT9pP2AxKDo6MDRhZg%3D%3D; _ga=GA1.2.555738570.1498731906; _gid=GA1.2.143466234.1498731906',
        'Host': 'www.investing.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    }
    headers2 = {
        'Cookie': '__gads=ID=f5089e4f2f622324:T=1498731909:S=ALNI_MZVSEm9TWER8TJlbZZLOzlcGFP0sg; PHPSESSID=qf6hfprrv31m6qka642clp82g7; geoC=CN; adBlockerNewUserDomains=1498734746; gtmFired=OK; StickySession=id.95327857748.918.www.investing.com; optimizelyEndUserId=oeu1498734748818r0.4865568312206183; editionPostpone=1498734756238; __qca=P0-364377178-1498734759859; travelDistance=4; searchedResults=[{"pairId":944403,"link":"/equities/iflytek-a","symbol":"002230","name":"Iflytek%20Co%20Ltd","type":"Equity%20-%20Shenzhen","flag":"China"}]; _gat=1; _gat_allSitesTracker=1; _ga=GA1.2.555738570.1498731906; _gid=GA1.2.143466234.1498731906; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A3%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22102047%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A29%3A%22%2Fequities%2Ftencent-holdings-hk%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A3%3A%22178%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A20%3A%22%2Findices%2Fjapan-ni225%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22944403%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fequities%2Fiflytek-a%22%3B%7D%7D%7D%7D; nyxDorf=ZGdiMGUtMWw%2FbmFsN3o0NzdnMmtheGBnNjQ%3D; optimizelySegments=%7B%224225444387%22%3A%22gc%22%2C%224226973206%22%3A%22direct%22%2C%224232593061%22%3A%22false%22%2C%225010352657%22%3A%22none%22%7D; optimizelyBuckets=%7B%228455380705%22%3A%228457490131%22%7D; optimizelyPendingLogEvents=%5B%5D; billboardCounter_1=2',
        'Host': 'www.investing.com',
        'Referer': 'https://www.investing.com/equities/iflytek-a',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    respons = requests.get(url1, headers=headers1).content
    tree = etree.HTML(respons)
    pair_id = tree.xpath('//div/@data-pair-id')[0]
    data = {
        'pair_id': pair_id,
        'pair_id_for_news': pair_id,
        'chart_type': 'area',
        'pair_interval': '86400',
        'candle_count': '120',
        'events': 'yes',
        'volume_series': 'yes'
    }

    get_url = urllib.parse.urlencode(data)
    binary_data = get_url.encode(encoding='utf-8')
    req = urllib.request.Request(url, binary_data, headers2)
    respon = urllib.request.urlopen(req)
    conts = respon.read().decode('utf-8')
    cont = re.findall('"candles":(.*),"events"', conts)
    result = eval(cont[0])
    for i in result:
        # result_list[str(j)]=str(i[1])
        result_list.append(i[1])
        j += 1
    # if result_list:
        # collection.update_one({'id': data['pair_id']}, {'$set':{data['pair_id']:result_list}}, upsert=True)
    # print(type(list_a))
    # for i in list_a:
    #     print(i)
    result_list = json.dumps(result_list)
    return result_list
# a=get_name(111)
# print(a)
