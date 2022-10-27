"""
 -----*--------------*-------
__author__ :  chenzhixiong
__time__ :  14:34
-*- coding: utf-8 -*-
 -----*--------------*-------
"""
import logging
from common.path_handler import Config


class MyLogger(object):
    isinstance = None
    count = 0

    def __new__(cls, *args, **kwargs):
        mylog = logging.getLogger('mylog')
        mylog.setLevel('DEBUG')
        sh = logging.StreamHandler()
        sh.setLevel('DEBUG')
        mylog.addHandler(sh)

        fh = logging.FileHandler(Config.log_path, encoding='utf8')
        fh.setLevel('DEBUG')
        mylog.addHandler(fh)
        fmt = '%(asctime)s - %(levelname)s: %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        mylog.removeFilter(fh)
        return mylog


mylog = MyLogger()


if __name__ == "__main__":
    mylog.info("666")