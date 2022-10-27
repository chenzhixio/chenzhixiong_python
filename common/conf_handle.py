"""
 -----*--------------*-------
__author__ :  chenzhixiong
获取配置数据
-*- coding: utf-8 -*-
 -----*--------------*-------
"""
from configparser import ConfigParser
from common.path_handler import Config


class MyConfig(ConfigParser):

    def __init__(self):
        super().__init__()

        self.read(Config.ini_path, encoding='utf_8')


myconf = MyConfig()
