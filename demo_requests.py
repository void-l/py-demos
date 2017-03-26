# -*- coding:utf-8 -*-
import requests
import utils, cfg


def get_baidu_translation_collection():
    header_origin = cfg.BAIDU_TRANSLATION_HEADERS
    headers = utils.trans_header_to_dict(header_origin)

    r = requests.get("http://fanyi.baidu.com/collection", headers=headers)
    print 'url', r.url
    print 'headers', r.headers
    # print 'text', r.text
    # print 'content', r.content
    print 'encoding', r.encoding

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
    return json_data

if __name__ == '__main__':
    collection = get_baidu_translation_collection()
    print collection['total']