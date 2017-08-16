# -*- coding:utf-8 -*-


class Coca(object):
    INDEX = 'index'
    WORD = 'word'
    TRANSLATION = 'translation'
    DESC = "desc"
    CREATEDAT = 'createdAt'
    UPDATEDTA = 'updatedAt'

    def __init__(self):
        self.index = 0
        self.word = ''
        self.translation = ''
        self.createdAt = 0
        self.updatedAt = 0
        self.desc = ''
