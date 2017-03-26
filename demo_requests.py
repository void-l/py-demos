# -*- coding:utf-8 -*-
import requests
import json


def get_baidu_translation_collection():
    headers = {
        'Host': 'fanyi.baidu.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://fanyi.baidu.com/',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cookie': 'BAIDUID=2A69256500084BDE59B370E789589709:FG=1; BIDUPSID=7447B3FB210243BC214F81B85E15F5F9; PSTM=1489889990; BDSFRCVID=52DsJeC62RiWSg5iFCHVK9roOg8_ID7TH6aIWlQSRmLS-RJlxSTlEG0Pfx8g0KubB4u4ogKK3gOTH4nP; H_BDCLCKID_SF=JJ4O_C-5tCvKeJbYK4oj5KCyMfca5C6JKCOa3RA8Kb7VbpFRQRbkbftd2-te-xnEKK5E5-59L-J-MKJJQ-5f3MrDyf64ajJZfJuDoDtMJIDabP365IFMD5oH-frMetJya4o2WDkatqb5OR5Jj65CMq-9bNo00fJ7Qe08QJ7v5KnrOq-63MA--fFihbQgQtrrL-jNaJRyLMbSsq0x0-jWe-bQypoa3j3tJIOMahkb5h7xOKbk056jK4JKDH0OtjoP; H_PS_PSSID=1462_18195_21083_17001_20928; locale=zh; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=ZiYzR2Q2xMdzRHemkzYU9reFlsQWUxWUllcX5JWXRPUFpGbnR5TjZnVGR0fnhZSVFBQUFBJCQAAAAAAAAAAAEAAAB6YhYwwfWyqGNvZGluZwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN0q1VjdKtVYSj; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1490365141; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1490365159'
    }

    r = requests.get("http://fanyi.baidu.com/collection", headers=headers)
    print 'url', r.url
    print 'headers', r.headers
    # print 'text', r.text
    # print 'content', r.content
    print 'encoding', r.encoding

    # f = open("fanyi.html", 'w+')
    # f.write(r.content)
    # f.flush()
    # f.close()

    url = 'http://fanyi.baidu.com/pcnewcollection?req=get'
    data = {
        'dstStatus': 'all',
        'order': 'time',
        'direction': 'all',
        'page': '0',
        'pagesize': '146'
    }

    rs = requests.post(url, data=data, headers=headers)
    json_data = rs.json()  #dict
    # print type(json_data), json_data['totalpage']
    return json_data

if __name__ == '__main__':
    collection = get_baidu_translation_collection()
    print collection['total']