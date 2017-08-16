# -*- coding:utf-8 -*-
import codecs
import chardet


def get_encoding(content):
    encoding = chardet.detect(content)['encoding']
    # print encoding
    return encoding


def convert2utf8(f):
    content = codecs.open(f, 'r').read()
    encoding = get_encoding(content)
    if encoding is None:
        print "can't detect file encoding", f

    content = content.decode(encoding)
    print f, encoding
    if encoding != 'utf-8' and encoding != 'UTF-8-SIG':
        print "convert"
        codecs.open(f, "w", encoding='utf-8').write(content)


if __name__ == "__main__":
    convert2utf8('utils.py')
