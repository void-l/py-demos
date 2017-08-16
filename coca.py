# -*- coding:utf-8 -*-
import requests
from lxml import html
from model import Coca
import lchelper
import time

base_url = r'https://www.shanbay.com'


def getCatalog():
    url_path = r'/wordbook/103867/'
    categories = []
    rs = requests.get(base_url + url_path)
    tree = html.fromstring(rs.text)
    for item in tree.xpath("//td[@class='wordbook-wordlist-name']/a"):
        # print item.xpath('./@href')[0], item.xpath('./text()')[0]
        categories.append(
            {'href': item.xpath('./@href')[0], 'desc': item.xpath('./text()')[0]})
    return categories


def getPage(url):
    # url_path = r'/wordlist/103867/194194/'
    wordlist = []
    for index in range(1, 6):
        rs = requests.get(url, {"page": str(index)})
        # print rs.url

        tree = html.fromstring(rs.text)
        # print rs.text

        for item in tree.xpath("//tr[@class='row']"):
            # print item.xpath("./td[@class='span2']/strong/text()")[0]
            # print item.xpath("./td[@class='span10']/text()")[0]
            wordlist.append(
                {'word': item.xpath("./td[@class='span2']/strong/text()")[0],
                 'translation': item.xpath("./td[@class='span10']/text()")[0]})

    return wordlist


def main():
    # categories = getCatalog()
    # print categories

    categories = [{'href': '/wordlist/103867/194782/', 'desc': 'wordlist 17700-17800'},
                  {'href': '/wordlist/103867/194785/', 'desc': 'wordlist 17800-17900'},
                  {'href': '/wordlist/103867/194788/', 'desc': 'wordlist 17900-18000'},
                  {'href': '/wordlist/103867/194791/', 'desc': 'wordlist 18000-18100'},
                  {'href': '/wordlist/103867/194794/', 'desc': 'wordlist 18100-18200'},
                  {'href': '/wordlist/103867/194797/', 'desc': 'wordlist 18200-18300'},
                  {'href': '/wordlist/103867/194800/', 'desc': 'wordlist 18300-18400'},
                  {'href': '/wordlist/103867/194803/', 'desc': 'wordlist 18400-18500'},
                  {'href': '/wordlist/103867/194806/', 'desc': 'wordlist 18500-18600'},
                  {'href': '/wordlist/103867/194812/', 'desc': 'wordlist 18600-18700'},
                  {'href': '/wordlist/103867/194815/', 'desc': 'wordlist 18700-18800'},
                  {'href': '/wordlist/103867/194818/', 'desc': 'wordlist 18800-18900'},
                  {'href': '/wordlist/103867/194824/', 'desc': 'wordlist 18900-19000'},
                  {'href': '/wordlist/103867/194827/', 'desc': 'wordlist 19000-19100'},
                  {'href': '/wordlist/103867/194833/', 'desc': 'wordlist 19100-19200'},
                  {'href': '/wordlist/103867/194836/', 'desc': 'wordlist 19200-19300'},
                  {'href': '/wordlist/103867/194839/', 'desc': 'wordlist 19300-19400'},
                  {'href': '/wordlist/103867/194842/', 'desc': 'wordlist 19400-19500'},
                  {'href': '/wordlist/103867/194845/', 'desc': 'wordlist 19500-19600'},
                  {'href': '/wordlist/103867/194848/', 'desc': 'wordlist 19600-19700'},
                  {'href': '/wordlist/103867/194851/', 'desc': 'wordlist 19700-19800'},
                  {'href': '/wordlist/103867/194854/', 'desc': 'wordlist 19800-19900'},
                  {'href': '/wordlist/103867/194857/', 'desc': 'wordlist 19900-20000'},
                  {'href': '/wordlist/103867/194860/', 'desc': 'wordlist 20000-20100'},
                  {'href': '/wordlist/103867/194863/', 'desc': 'wordlist 20100-20200'}]

    index = 14927
    for category in categories:
        url = base_url + category['href']
        desc = category['desc']
        print url, desc

        time.sleep(1)

        wordlist = getPage(url)

        for word in wordlist:
            coca = Coca()
            coca.desc = desc
            coca.index = index
            coca.word = word['word']
            coca.translation = word['translation']

            if lchelper.coca_save(coca):
                index += 1


if __name__ == '__main__':
    main()
