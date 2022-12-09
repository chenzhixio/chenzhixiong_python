"""
 -----*--------------*-------
__author__ :  chenzhixiong
__time__ :  2022.11.11
-*- coding: utf-8 -*-
 -----*--------------*-------
"""
import requests

def newnotice(msg):
    """企业微信通知----群@所有人通知"""
    data = {
        "msgtype": "text",
        "text": {
            "content": msg,
            "mentioned_list": ["@陈志雄"],
        }
    }
    requests.post('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=8655c089-5d81-4589-8d9b-01c1b54ec573', json=data)


if __name__ == '__main__':
    newnotice("通知测试")
