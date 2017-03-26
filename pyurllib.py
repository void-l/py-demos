# -*- coding:utf-8 -*-

import urllib
import urllib2

"""
1. 构造数据是使用Request(url, data) 即post方式发送请求；GET方式将编码后的字符加到url后面
2. Headers: user-agent,referer,
3. 设置代理proxy
4. 异常处理 HTTP_Error,URL_Error
5. response.info() /geturl()
"""


def encode_data(values):
    return urllib.urlencode(values)


def use_debuglog():
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(httpHandler, httpsHandler)
    urllib2.install_opener(opener)
    response = urllib2.urlopen('http://www.baidu.com')
    print response


def use_proxy():
    enable_proxy = True
    proxy_handler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8080'})
    null_proxy_handler = urllib2.ProxyHandler({})
    if enable_proxy:
        opener = urllib2.build_opener(proxy_handler)
    else:
        opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)


request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)

# print encode_data({"username": "void", "pwd": "pwd"})

use_debuglog()
