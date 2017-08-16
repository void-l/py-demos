# -*- coding:utf-8 -*-
import leancloud
import cfg
from model import Coca

leancloud.init(cfg.LC_APP_KEY, cfg.LC_MASTER_KEY)

CLASS_COCA = "Coca"
CLASS_TRANSLATION = "Translation"


def save_translation(name=CLASS_TRANSLATION, id_="", values={}):
    if translation_exists(id_=id_):
        print "save id %s exists" % id_
        return

    Translation = leancloud.Object.extend(name)
    instance = Translation()

    for k, v in values.iteritems():
        instance.set(k, v)

    instance.save()


def translation_exists(name=CLASS_TRANSLATION, id_=''):
    Translation = leancloud.Object.extend(name)
    query = leancloud.Query(Translation)
    query.equal_to('id', id_)

    result = query.find()
    if len(result) > 0:
        return True
    else:
        return False


def coca_save(coca):
    if coca_exists(coca.word):
        print 'word %s already exists.' % coca.word
        return False

    Coca = leancloud.Object.extend(CLASS_COCA)
    instance = Coca()

    instance.set(coca.WORD, coca.word)
    instance.set(coca.TRANSLATION, coca.translation)
    instance.set(coca.INDEX, coca.index)
    instance.set(coca.DESC, coca.desc)

    instance.save()
    return True


def coca_exists(word):
    Coca = leancloud.Object.extend(CLASS_COCA)
    query = leancloud.Query(Coca)
    query.equal_to('word', word)

    try:
        result = query.find()
        if len(result) > 0:
            return True
        else:
            return False
    except Exception as e:
        print 'exception', e.message
        return False

if __name__ == "__main__":
    # save_translation(id_='234', values={"key1": "value1", "key2": 2})

    # translation_exists(id_='234')

    coca = Coca()
    coca.index = 1
    coca.word = 'newword'
    coca.translation = 'translation'

    coca_save(coca)
