import re
from time import sleep
from common.loger_handler import mylog
from page_element.page_key import PageKey


class test_Yuntai_setting(PageKey):
    """云台设置"""

    def Yuntai_setting_001(self):
        try:
            self.set_type("可见光")
            text_list = []
            distinguish_list = []
            for i in [1, 2, 3, 1]:
                self.operation_set_load(7)
                self.video_quality.click()
                sleep(1)
                self.driver.xpath(F'//android.widget.ListView/android.widget.LinearLayout[{i}]').click()
                sleep(3)
                distinguish = self.photo_video_distinguish(F"Yuntai_setting_001_{i}")
                self.operation_set_load(7)
                sleep(3)
                text = self.video_quality.get_text()
                distinguish_list.append(distinguish)
                text_list.append(text)
                mylog.info(F"本次视频尺寸：{text}------拍照识别：{distinguish}")
            sleep(1)
            self.driver.click(self.x, self.y)
            return text_list, distinguish_list
        except BaseException as a:
            self.failed_operation()
            raise a

    def Yuntai_setting_002(self):
        try:
            self.set_type("可见光")
            text_list = []
            distinguish_list = []
            for i in [1, 2, 3, 4, 1]:
                self.operation_set_load(7)
                self.photo_size.click()
                sleep(1)
                self.driver.xpath(F'//android.widget.ListView/android.widget.LinearLayout[{i}]').click()
                sleep(3)
                distinguish = self.photo_video_distinguish(F"Yuntai_setting_002_{i}")
                self.operation_set_load(7)
                sleep(3)
                text = self.photo_size.get_text()
                distinguish_list.append(distinguish)
                text_list.append(text)
                mylog.info(F"本次照片分辨率：{text}-------拍照识别：{distinguish}")
            sleep(1)
            self.driver.click(self.x, self.y)
            return text_list, distinguish_list
        except BaseException as a:
            self.failed_operation()
            raise a

    def Yuntai_setting_003(self):
        try:
            self.set_type("可见光")
            text_list = []
            distinguish_list = []
            for i in [1, 2, 3, 1]:
                self.operation_set_load(7)
                self.anti_flicker.click()
                sleep(1)
                self.driver.xpath(F'//android.widget.ListView/android.widget.LinearLayout[{i}]').click()
                sleep(3)
                distinguish = self.photo_video_distinguish(F"Yuntai_setting_003_{i}")
                self.operation_set_load(7)
                sleep(3)
                text = self.anti_flicker.get_text()
                distinguish_list.append(distinguish)
                text_list.append(text)
                mylog.info(F"抗闪烁：{text}----------拍照识别：{distinguish}")
            sleep(1)
            self.driver.click(self.x, self.y)
            return text_list, distinguish_list
        except BaseException as a:
            self.failed_operation()
            raise a

    def Yuntai_setting_004(self):
        try:
            self.set_type("红外")
            self.operation_set_load(7)
            self.enhance_mode.click()
            self.driver.xpath("//*[contains(@text,'低增益')]").click()
            sleep(2)
            distinguish1 = self.photo_video_distinguish("Yuntai_setting_004_01")
            self.operation_set_load(7)
            sleep(5)
            text1 = self.enhance_mode.get_text()
            mylog.info(F"预期结果：低增益--------实际结果：{text1}------{distinguish1}")
            self.enhance_mode.click()
            self.driver.xpath("//*[contains(@text,'高增益')]").click()
            sleep(2)
            distinguish2 = self.photo_video_distinguish("Yuntai_setting_004_02")
            self.operation_set_load(7)
            sleep(5)
            text2 = self.enhance_mode.get_text()
            mylog.info(F"预期结果：高增益--------实际结果：{text2}------{distinguish2}")
            self.driver.click(343, 199)
            return [text1, text2, distinguish1, distinguish2]
        except BaseException as a:
            self.failed_operation()
            raise a

    def Yuntai_setting_005(self):
        try:
            self.set_type("分屏")
            text_list = []
            distinguish_list = []
            for i in [1, 2, 3, 1]:
                self.operation_set_load(7)
                self.video_quality.click()
                sleep(1)
                self.driver.xpath(F'//android.widget.ListView/android.widget.LinearLayout[{i}]').click()
                sleep(3)
                distinguish = self.photo_video_distinguish(F"Yuntai_setting_005_{i}", "分屏")
                self.operation_set_load(7)
                sleep(3)
                text = self.video_quality.get_text()
                text_list.append(text)
                distinguish_list.append(distinguish)
                mylog.info(F"本次视频尺寸：{text}--------拍照识别：{distinguish}")
            sleep(1)
            self.driver.click(self.x, self.y)
            return text_list, distinguish_list
        except BaseException as a:
            self.failed_operation()
            raise a

    def Yuntai_setting_006(self):
        try:
            self.set_type("分屏")
            text_list = []
            distinguish_list = []
            for i in [1, 2, 3, 4, 1]:
                self.operation_set_load(7)
                self.photo_size.click()
                sleep(1)
                self.driver.xpath(F'//android.widget.ListView/android.widget.LinearLayout[{i}]').click()
                sleep(3)
                distinguish = self.photo_video_distinguish(F"Yuntai_setting_006_{i}", "分屏")
                self.operation_set_load(7)
                sleep(3)
                text = self.photo_size.get_text()
                text_list.append(text)
                distinguish_list.append(distinguish)
                mylog.info(F"本次照片分辨率：{text}-------拍照识别：{distinguish}")
            sleep(1)
            self.driver.click(self.x, self.y)
            return text_list, distinguish_list
        except BaseException as a:
            self.failed_operation()
            raise a

    def Yuntai_setting_007(self):
        try:
            self.set_type("分屏")
            text_list = []
            distinguish_list = []
            for i in [1, 2, 3, 1]:
                self.operation_set_load(7)
                self.anti_flicker.click()
                sleep(1)
                self.driver.xpath(F'//android.widget.ListView/android.widget.LinearLayout[{i}]').click()
                sleep(3)
                distinguish = self.photo_video_distinguish(F"Yuntai_setting_008_{i}", "分屏")
                self.operation_set_load(7)
                sleep(3)
                text = self.anti_flicker.get_text()
                distinguish_list.append(distinguish)
                text_list.append(text)
                mylog.info(F"抗闪烁：{text}--------拍照识别：{distinguish}")
            sleep(1)
            self.driver.click(self.x, self.y)
            return text_list, distinguish_list
        except BaseException as a:
            self.failed_operation()
            raise a

    def Yuntai_setting_008(self):
        try:
            self.set_type("分屏")
            self.operation_set_load(7)
            for i in range(3):
                sleep(2)
                self.driver.swipe(1267, 916, 1551, 370)
            sleep(2)
            self.driver.click(1213, 316)
            self.operation_set_load(7)
            for i in range(3):
                sleep(2)
                self.driver.swipe(1267, 916, 1551, 370)
            sleep(2)
            text1 = self.pitch_speed.get_text()
            mylog.info(F"预期结果：5--------实际结果：{text1}")
            sleep(2)
            self.driver.click(1555, 316)
            sleep(2)
            self.operation_set_load(7)
            for i in range(3):
                sleep(2)
                self.driver.swipe(1267, 916, 1551, 370)
            sleep(2)
            text2 = self.pitch_speed.get_text()
            sleep(2)
            self.driver.click(self.x, self.y)
            mylog.info(F"预期结果：100--------实际结果：{text2}")
            return [text1, text2]
        except BaseException as a:
            self.failed_operation()
            raise a