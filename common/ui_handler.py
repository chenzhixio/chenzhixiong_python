"""
 -----*--------------*-------
__author__ :  chenzhixiong
获取配置数据
-*- coding: utf-8 -*-
 -----*--------------*-------
"""
import time


class Browser(object):
    """UI自动化父类"""

    def __init__(self, driver):
        """初始化操作"""
        self.driver = driver

    def devices_on(self):
        """点亮屏幕"""
        self.driver.screen_on()

    def devices_off(self):
        """熄灭屏幕"""
        self.driver.screen_off()

    def devices_button(self, keys):
        """
        模拟按键:
        回到主屏幕: home
        返回：back
        方向键左，右，上，下，中心： left   right  up  down  center
        回车，   enter
        删除，   del
        电源键，  power
        后台，   recent
        音量+，  volume_up
        音量-，  volume_down
        禁音键： volume_mute
        参考 Android KEYCODE   https://blog.csdn.net/yaoyaozaiye/article/details/122826340
        """
        self.driver.press(keys)

    def devices_text_click(self, *element):
        """text定位并点击"""
        time.sleep(1)
        self.driver.xpath(*element).click()

    def devices_xy_click(self, x, y):
        """xy轴定位并点击"""
        time.sleep(1)
        self.driver.click(x, y)

    def devices_slide(self, x1, y1, x2, y2):
        """起始xy和结束xy"""
        self.driver.swipe(x1, y1, x2, y2)

    def devices_png(self, path):
        """截屏屏幕"""
        self.driver.screenshot(path)











