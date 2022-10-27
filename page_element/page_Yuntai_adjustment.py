import re
from time import sleep
from common.loger_handler import mylog
from page_element.test_page_key import test_page_load


class test_Yuntai_adjustment(test_page_load):
    """云台俯仰调节"""

    def get_number(self, element):
        """云台俯仰调节后获取角度"""
        sleep(2)
        self.angle.click()
        self.angle_2.click()
        sleep(2)
        element.click()
        sleep(2)
        text = self.get_value()
        return text

    def set_ev(self, element, num):
        """获取EV值选中状态"""
        sleep(2)
        element.click()
        sleep(3)
        self.operation_load_1()
        sleep(6)
        text = element.info.get('selected')
        mylog.info(F"{num}是否为选中状态：{text}")
        return text

    def Yuntai_adjustment_001(self):
        try:
            self.angle.click()
            self.angle_2.click()
            sleep(2)
            self.look_down.click()
            sleep(2)
            self.driver.swipe(1545, 490, 1545, 808)
            sleep(2)
            text1 = self.get_value()
            mylog.info(F"云台下视极限角度为：{text1}")
            self.angle.click()
            self.angle_2.click()
            sleep(2)
            self.hui_zhong.click()
            for i in range(3):
                sleep(3)
                self.driver.swipe(1545, 483, 1545, 235)
            sleep(2)
            text2 = self.get_value()
            mylog.info(F"云台上仰极限角度为：{text2}")
            return text1, text2
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_adjustment_002(self):
        try:
            self.angle.click()
            self.angle_2.click()
            self.driver.swipe(1545, 483, 1541, 225)
            sleep(2)
            self.hui_zhong.click()
            sleep(2)
            text1 = self.get_value()
            mylog.info(F"随意摇动后回中，角度为：{text1}")
            self.angle.click()
            self.angle_2.click()
            self.look_down.click()
            sleep(2)
            self.hui_zhong.click()
            sleep(2)
            text2 = self.get_value()
            mylog.info(F"极限角度后回中，角度为：{text2}")
            return text1, text2
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_adjustment_003(self):
        try:
            self.angle.click()
            self.angle_2.click()
            sleep(2)
            self.driver.swipe(1545, 490, 1545, 225)
            sleep(2)
            text1 = self.get_value()
            mylog.info(F"摇杆向上后角度为：{text1}")
            self.angle.click()
            self.angle_2.click()
            sleep(2)
            self.driver.swipe(1545, 490, 1545, 808)
            sleep(2)
            text2 = self.get_value()
            mylog.info(F"摇杆向下后角度为：{text2}")
            text3 = self.get_number(self.iv_roll_plus)
            mylog.info(F"微调增加后角度为：{text3}")
            text4 = self.get_number(self.iv_roll_minus)
            mylog.info(F"微调减少后角度为：{text4}")
            text5 = self.get_number(self.look_down)
            mylog.info(F"一键下视后角度为：{text5}")
            text6 = self.get_number(self.hui_zhong)
            mylog.info(F"一键回中后角度为：{text6}")
            return [text1, text2, text3, text4, text5, text6]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_adjustment_004(self):
        try:
            self.set_type("可见光")
            self.angle.click()
            self.angle_1.click()
            sleep(2)
            self.driver.swipe(1296, 292, 1607, 292)
            sleep(2)
            self.driver.swipe(1296, 292, 1607, 292)
            sleep(2)
            text1 = self.set_ev(self.EV_f3, "-3")
            text2 = self.set_ev(self.EV_f2, "-2")
            text3 = self.set_ev(self.EV_f1, "-1")
            text4 = self.set_ev(self.EV_0, "0")
            text5 = self.set_ev(self.EV_1, "1")
            text6 = self.set_ev(self.EV_2, "2")
            text7 = self.set_ev(self.EV_3, "3")
            text8 = self.set_ev(self.EV_2, "2")
            text9 = self.set_ev(self.EV_0, "0")
            self.driver.click(599, 268)
            return [text1, text2, text3, text4, text5, text6, text7, text8, text9]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_adjustment_005(self):
        try:
            self.set_type("可见光")
            self.angle.click()
            self.angle_1.click()
            sleep(2)
            self.driver.swipe(1296, 474, 1607, 474)
            sleep(2)
            self.driver.swipe(1296, 474, 1607, 474)
            sleep(2)
            text1 = self.set_ev(self.light_x0, "x0")
            text2 = self.set_ev(self.light_x2, "x2")
            text3 = self.set_ev(self.light_x4, "x4")
            text5 = self.set_ev(self.light_x16, "x16")
            text6 = self.set_ev(self.light_x32, "x32")
            text8 = self.set_ev(self.light_x8, "x8")
            text10 = self.set_ev(self.light_x2, "x2")
            text11 = self.set_ev(self.light_x0, "x0")
            self.driver.click(599, 268)
            return [text1, text2, text3, text5, text6, text8, text10, text11]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_adjustment_006(self):
        try:
            self.set_type("红外")
            self.operation_load_1()
            self.driver.swipe(1296, 474, 1607, 474)
            sleep(2)
            self.driver.swipe(1296, 474, 1607, 474)
            sleep(2)
            text1 = self.set_ev(self.light_x1, "x1")
            text2 = self.set_ev(self.light_x2, "x2")
            text3 = self.set_ev(self.light_x4, "x4")
            text4 = self.set_ev(self.light_x8, "x8")
            text5 = self.set_ev(self.light_x4, "x4")
            text6 = self.set_ev(self.light_x2, "x2")
            text7 = self.set_ev(self.light_x1, "x1")
            sleep(2)
            self.driver.click(599, 268)
            return [text1, text2, text3, text4, text5, text6, text7]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_adjustment_007(self):
        try:
            self.set_type("红外")
            self.operation_load_1()
            self.driver.swipe(1296, 292, 1607, 292)
            sleep(2)
            self.driver.swipe(1296, 292, 1607, 292)
            sleep(2)
            text1 = self.set_ev(self.baire, "白热")
            text2 = self.set_ev(self.rongyan, "熔岩")
            text3 = self.set_ev(self.tiehong, "铁红")
            text4 = self.set_ev(self.retie, "热铁")
            text5 = self.set_ev(self.yiliao, "医疗")
            text6 = self.set_ev(self.beiji, "北极")
            text7 = self.set_ev(self.caihong1, "彩虹1")
            text8 = self.set_ev(self.caihong2, "彩虹2")
            text9 = self.set_ev(self.miaohong, "描红")
            text10 = self.set_ev(self.heire, "黑热")
            text12 = self.set_ev(self.caihong2, "彩虹2")
            text14 = self.set_ev(self.beiji, "北极")
            text16 = self.set_ev(self.retie, "热铁")
            text18 = self.set_ev(self.rongyan, "熔岩")
            text19 = self.set_ev(self.baire, "白热")
            sleep(2)
            self.driver.click(599, 268)
            return [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text12, text14, text16, text18, text19]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_adjustment_008(self):
        try:
            self.logo.click()
            sleep(2)
            text = self.cloudName_1.get_text()
            mylog.info(F"挂载云台识别名称：{text}")
            self.manualFlightBg.click()
            sleep(1)
            self.rwfx_close.click()
            sleep(4)
            return text
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_adjustment_009(self):
        try:
            self.set_type("红外")
            self.operation_load_1()
            self.driver.click(1309, 642)
            sleep(5)
            text1 = self.driver(resourceId="com.gdu.pro2:id/tv_irda_setting_brightness").get_text()
            self.driver.click(0.286, 0.176)
            mylog.info(F"设置红外亮度为：{text1}")
            sleep(2)
            self.operation_load_1()
            self.driver.click(1779, 642)
            sleep(5)
            text2 = self.driver(resourceId="com.gdu.pro2:id/tv_irda_setting_brightness").get_text()
            self.driver.click(1500, 642)
            sleep(2)
            self.driver.click(0.286, 0.176)
            mylog.info(F"设置红外亮度为：{text2}")
            sleep(2)
            return [text1, text2]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def Yuntai_adjustment_010(self):
        try:
            self.set_type("红外")
            self.operation_load_1()
            self.driver.click(1307, 790)
            sleep(5)
            text1 = self.driver(resourceId="com.gdu.pro2:id/tv_irda_setting_contrast").get_text()
            self.driver.click(0.286, 0.176)
            mylog.info(F"设置红外亮度为：{text1}")
            sleep(2)
            self.operation_load_1()
            self.driver.click(1789, 790)
            sleep(5)
            text2 = self.driver(resourceId="com.gdu.pro2:id/tv_irda_setting_contrast").get_text()
            self.driver.click(1500, 790)
            sleep(2)
            self.driver.click(0.286, 0.176)
            mylog.info(F"设置红外亮度为：{text2}")
            sleep(2)
            return [text1, text2]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a





