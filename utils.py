# -*- coding:utf-8 -*-
import cfg


def trans_header_to_dict(headers):
    """
    :parameter headers :
    :return dict_headers
    """
    headers = headers.split('\n')
    headers = [item.strip(' ') for item in headers]
    headers = [item.strip(' ') for item in headers if len(item) > 0]

    dict_headers = {}
    for item in headers:
        index = item.find(':')
        if index == -1:
            raise Exception('the headers data goes wrong, please check: ' + item)
        k = item[: index].strip(' ')
        v = item[index + 1:].strip(' ')
        dict_headers[k] = v

    return dict_headers


if __name__ == "__main__":
    header_origin = cfg.BAIDU_TRANSLATION_HEADERS

    print trans_header_to_dict(header_origin)
