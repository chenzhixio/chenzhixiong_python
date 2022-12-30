"""
 -----*--------------*-------
__author__ :  chenzhixiong
__time__ :  2022.11.11
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
