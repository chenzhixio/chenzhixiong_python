import re
from time import sleep
from common.loger_handler import mylog
from page_element.test_page_key import test_page_load


class test_Yuntai_setting(test_page_load):
    """云台设置"""

    def Yuntai_setting_000(self):
        try:
            self.set_type("可见光")
            text1 = self.visible_light.exists
            mylog.info(F"可见光切换：{not text1}")
            self.set_type("红外")
            text2 = self.infra_red.exists
            mylog.info(F"红外模式切换：{not text2}")
            self.set_type("分屏")
            text3 = self.split_screen.exists
            mylog.info(F"分屏模式切换：{not text3}")
            self.set_type("可见光")
            text4 = self.visible_light.exists
            mylog.info(F"可见光切换：{not text4}")
            return [text1, text2, text3, text4]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_setting_001(self):
        try:
            self.set_type("可见光")
            self.operation_set_load()
            sleep(2)
            list_text = []
            for i in [1, 2, 3, 1]:
                sleep(2)
                self.anti_flicker.click()
                sleep(2)
                self.driver.xpath(F'//android.widget.ListView/android.widget.LinearLayout[{i}]').click()
                sleep(2)
                self.operation_set_load()
                sleep(10)
                text = self.anti_flicker.get_text()
                list_text.append(text)
            self.driver.click(343, 199)
            mylog.info(F"预期：关闭-------实际：{list_text[0]}")
            mylog.info(F"预期：50Hz-------实际：{list_text[1]}")
            mylog.info(F"预期：60Hz-------实际：{list_text[2]}")
            mylog.info(F"预期：关闭-------实际：{list_text[3]}")
            return list_text
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_setting_002(self):
        try:
            list_text = []
            self.set_type("可见光")
            self.operation_set_load()
            for i in [1, 2, 3, 4, 1, 2, 3, 4, 1]:
                sleep(2)
                self.photo_size.click()
                sleep(2)
                self.driver.xpath(F'//android.widget.ListView/android.widget.LinearLayout[{i}]').click()
                sleep(2)
                self.operation_set_load()
                sleep(10)
                text = self.photo_size.get_text()
                list_text.append(text)
                mylog.info(F"本次照片分辨率：{text}")
            self.driver.click(343, 199)
            return list_text
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_setting_003(self):
        try:
            text_lsit = []
            for i in ["分屏", "红外"]:
                sleep(2)
                self.set_type(i)
                self.operation_set_load()
                sleep(2)
                self.photo_size.click()
                sleep(2)
                text1 = self.driver.xpath(F'//android.widget.ListView/android.widget.LinearLayout[1]')
                if text1.exists:
                    text1.click()
                    text2 = self.photo_size.get_text()
                else:
                    text2 = "分辨率不可设置"
                mylog.info(F"{i}模式，设置分辨率后：{text2}")
                text_lsit.append(text2)
                self.driver.click(343, 199)
            return text_lsit
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_setting_004(self):
        try:
            list_text = []
            self.set_type("可见光")
            self.operation_set_load()
            for i in [1, 2, 3, 1]:
                sleep(2)
                self.video_quality.click()
                sleep(2)
                self.driver.xpath(F'//android.widget.ListView/android.widget.LinearLayout[{i}]').click()
                sleep(2)
                self.operation_set_load()
                sleep(10)
                text = self.video_quality.get_text()
                list_text.append(text)
                mylog.info(F"本次视频尺寸：{text}")
            self.driver.click(343, 199)
            return list_text
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_setting_005(self):
        try:
            text_lsit = []
            for i in ["分屏", "红外"]:
                sleep(2)
                self.set_type(i)
                self.operation_set_load()
                self.video_quality.click()
                sleep(2)
                text1 = self.driver.xpath(F'//android.widget.ListView/android.widget.LinearLayout[2]')
                if text1.exists:
                    text1.click()
                    text2 = self.video_quality.get_text()
                else:
                    text2 = "视频尺寸不可设置"
                mylog.info(F"{i}模式，设置视频尺寸后：{text2}")
                text_lsit.append(text2)
                self.driver.click(343, 199)
            return text_lsit
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_setting_006(self):
        try:
            self.set_type("红外")
            self.operation_set_load()
            self.enhance_mode.click()
            self.driver.xpath("//*[contains(@text,'低增益')]").click()
            sleep(2)
            self.operation_set_load()
            sleep(5)
            text1 = self.enhance_mode.get_text()
            mylog.info(F"预期结果：低增益--------实际结果：{text1}")
            self.enhance_mode.click()
            self.driver.xpath("//*[contains(@text,'高增益')]").click()
            sleep(2)
            self.operation_set_load()
            sleep(5)
            text2 = self.enhance_mode.get_text()
            mylog.info(F"预期结果：高增益--------实际结果：{text2}")
            self.driver.click(343, 199)
            return [text1, text2]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_setting_007(self):
        try:
            self.all_set.click()
            self.load_set.click()
            sleep(2)
            self.driver.swipe(1201, 1168, 1551, 1168)
            sleep(2)
            self.driver.click(599, 268)
            self.all_set.click()
            self.load_set.click()
            sleep(2)
            text1 = self.pitch_speed.get_text()
            mylog.info(F"预期结果：100--------实际结果：{text1}")
            sleep(2)
            self.driver.swipe(1516, 1168, 1201, 1168)
            sleep(2)
            self.driver.click(599, 268)
            self.all_set.click()
            self.load_set.click()
            sleep(2)
            text2 = self.pitch_speed.get_text()
            sleep(2)
            self.driver.swipe(1201, 1168, 1551, 1168)
            sleep(2)
            self.driver.click(599, 268)
            mylog.info(F"预期结果：5--------实际结果：{text2}")
            return [text1, text2]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a