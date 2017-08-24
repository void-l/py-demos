# -*- coding:utf-8 -*-

import os


def files_traversal(path, ext=()):
    for dirpath, dirnames, filenames in os.walk(path):
        exclude_dirs = [dirname for dirname in dirnames if dirname.startswith('.')]

        for exclude in exclude_dirs:
            dirnames.remove(exclude)

        for filename in filenames:
            if filename.split('.')[-1] in ext:
                yield os.path.join(dirpath, filename)


if __name__ == '__main__':
    files = files_traversal('.', ext=('py',))
    for f in files:
        print f
