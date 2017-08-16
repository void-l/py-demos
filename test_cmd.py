# -*- coding:utf-8 -*-

import sys
import getopt

'''
http://www.runoob.com/python/python-command-line-arguments.html

getopt.getopt(args, options[, long_options])
    args: 要解析的命令行参数列表。
    options: 以列表的格式定义，options后的冒号(:)表示该选项必须有附加的参数，不带冒号表示该选项不附加参数。
    long_options: 以字符串的格式定义，long_options 后的等号(=)表示如果设置该选项，必须有附加的参数，否则就不附加参数。
    该方法返回值由两个元素组成: 第一个是 (option, value) 元组的列表。 第二个是参数列表，包含那些没有'-'或'--'的参数。
'''

if __name__ == "__main__":
    print len(sys.argv), sys.argv
