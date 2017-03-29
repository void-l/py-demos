# -*- coding:utf-8 -*-
import leancloud
import cfg


leancloud.init(cfg.LC_APP_KEY, cfg.LC_MASTER_KEY)


def save_translation(name="Translation", id_="", values={}):
    if translation_exists(id_=id_):
        print "save id %s exists" % id_
        return

    Translation = leancloud.Object.extend(name)
    instance = Translation()

    for k, v in values.iteritems():
        instance.set(k, v)

    instance.save()


def translation_exists(name="Translation", id_=''):
    Translation = leancloud.Object.extend(name)
    query = leancloud.Query(Translation)
    query.equal_to('id', id_)

    result = query.find()
    if len(result) > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    save_translation(id_='234', values={"key1": "value1", "key2": 2})

    # translation_exists(id_='234')