# -*- coding:utf-8 -*-
import requests
import utils
import cfg
import lchelper


def get_baidu_translation_collection():
    header_origin = cfg.BAIDU_TRANSLATION_HEADERS
    headers = utils.trans_header_to_dict(header_origin)

    # r = requests.get("http://fanyi.baidu.com/collection", headers=headers)
    # print 'url', r.url
    # print 'headers', r.headers
    # print 'text', r.text
    # print 'content', r.content
    # print 'encoding', r.encoding

    url = 'http://fanyi.baidu.com/pcnewcollection?req=get'
    data = {
        'dstStatus': 'all',
        'order': 'time',
        'direction': 'all',
        'page': '0',
        'pagesize': '30'
    }
    rs = requests.post(url, data=data, headers=headers)
    json_data = rs.json()
    # get total
    total = json_data['total']
    data['pagesize'] = total

    rs = requests.post(url, data=data, headers=headers)
    json_data = rs.json()

    return json_data


if __name__ == '__main__':
    collection = get_baidu_translation_collection()['pageinfo']
    print len(collection)

    for word in collection:
        id_ = word['id']
        lchelper.save_translation(id_=id_, values=word)
