import re
from time import sleep
from common.loger_handler import mylog
from page_element.page_key import PageKey


class test_Yuntai_adjustment(PageKey):
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

    def set_ev(self, name, element, num):
        """获取EV值选中状态"""
        sleep(2)
        element.click()
        sleep(3)
        distinguish1, distinguish2 = self.photo_video_distinguish(name)
        self.operation_load(1)
        sleep(6)
        text = element.info.get('selected')
        if distinguish1 == "照片确实存在漏拍":
            mylog.info(F"{num}是否为选中状态：{text}-------{distinguish1}")
        else:
            mylog.info(F"{num}是否为选中状态：{text}-------录像识别：{distinguish1}-----拍照识别：{distinguish2}")
        return text, distinguish1, distinguish2

    def angle_test(self, elemet, a, b, c, d):
        self.operation_load(2)
        for i in range(4):
            self.driver.swipe(a, b, c, d)
            sleep(2)
        elemet.click()
        sleep(3)
        text = self.get_value()
        mylog.info(F"极限角度测试：{text}")
        self.set_huizhong()
        return text

    def Yuntai_adjustment_001(self):
        try:
            self.operation_set_load(7)
            for i in range(3):
                sleep(2)
                self.driver.swipe(1267, 916, 1551, 370)
            sleep(2)
            self.driver.click(1555, 316)
            self.operation_load(2)
            sleep(2)
            self.look_down.click()
            sleep(2)
            self.driver.swipe(1545, 490, 1545, 808)
            sleep(2)
            text1 = self.get_value()
            mylog.info(F"云台下视极限角度为：{text1}")
            self.operation_load(2)
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
            self.failed_operation()
            raise a

    def Yuntai_adjustment_002(self):
        try:
            text1 = self.angle_test(self.look_down, 1545, 483, 1545, 225)  # 向上极限
            text2 = self.angle_test(self.look_down, 1545, 483, 1545, 747)  # 向下极限
            text3 = self.angle_test(self.look_down, 1545, 483, 1388, 483)  # 向左极限
            text4 = self.angle_test(self.look_down, 1545, 483, 1800, 483)  # 向右极限
            self.driver.click(self.x, self.y)
            return [text1, text2, text3, text4]
        except BaseException as a:
            self.failed_operation()
            raise a

    def Yuntai_adjustment_003(self):
        try:
            text1 = self.angle_test(self.hui_zhong, 1545, 483, 1545, 225)   # 向上极限
            text2 = self.angle_test(self.hui_zhong, 1545, 483, 1545, 747)   # 向下极限
            text3 = self.angle_test(self.hui_zhong, 1545, 483, 1388, 483)   # 向左极限
            text4 = self.angle_test(self.hui_zhong, 1545, 483, 1800, 483)   # 向右极限
            self.driver.click(self.x, self.y)
            return [text1, text2, text3, text4]
        except BaseException as a:
            self.failed_operation()
            raise a

    def Yuntai_adjustment_004(self):
        try:
            self.operation_load(2)
            self.driver.swipe(1545, 490, 1545, 225)
            sleep(2)
            text1 = self.get_value()
            mylog.info(F"摇杆向上后角度为：{text1}")
            self.operation_load(2)
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
            self.failed_operation()
            raise a

    def Yuntai_adjustment_005(self):
        try:
            self.set_type("可见光")
            self.operation_load(1)
            self.driver.swipe(1296, 474, 1607, 474)
            sleep(2)
            self.driver.swipe(1296, 474, 1607, 474)
            sleep(2)
            self.light_x0.click()
            sleep(2)
            self.driver.swipe(1296, 292, 1607, 292)
            sleep(2)
            self.driver.swipe(1296, 292, 1607, 292)
            sleep(2)
            values = [[self.EV_f3, "-3"],
                      [self.EV_f1, "-1"],
                      [self.EV_0, "0"],
                      [self.EV_2, "2"],
                      [self.EV_0, "0"]]
            distinguish_list = []
            text_list = []
            for ev in values:
                text, distinguish1, distinguish2 = self.set_ev("Yuntai_adjustment_004", ev[0], ev[1])
                distinguish_list.append(distinguish1)
                distinguish_list.append(distinguish2)
                text_list.append(text)
            self.driver.click(self.x, self.y)
            return text_list, distinguish_list
        except BaseException as a:
            self.failed_operation()
            raise a

    def Yuntai_adjustment_006(self):
        try:
            self.set_type("可见光")
            self.operation_load(1)
            self.driver.swipe(1296, 474, 1607, 474)
            sleep(2)
            self.driver.swipe(1296, 474, 1607, 474)
            sleep(2)
            values = [[self.light_x0, "x0"],
                      [self.light_x4, "x4"],
                      [self.light_x16, "x16"],
                      [self.light_x32, "x32"],
                      [self.light_x8, "x8"],
                      [self.light_x2, "x2"],
                      [self.light_x0, "x0"]]
            distinguish_list = []
            text_list = []
            for ev in values:
                text, distinguish1, distinguish2 = self.set_ev("Yuntai_adjustment_005", ev[0], ev[1])
                distinguish_list.append(distinguish1)
                distinguish_list.append(distinguish2)
                text_list.append(text)
            self.driver.click(self.x, self.y)
            return text_list, distinguish_list
        except BaseException as a:
            self.failed_operation()
            raise a

    def Yuntai_adjustment_007(self):
        try:
            self.set_type("红外")
            self.operation_load(1)
            self.driver.swipe(1296, 292, 1607, 292)
            sleep(2)
            self.driver.swipe(1296, 292, 1607, 292)
            sleep(2)
            values = [[self.baire, "白热"],
                      [self.rongyan, "熔岩"],
                      [self.tiehong, "铁红"],
                      [self.retie, "热铁"],
                      [self.yiliao, "医疗"],
                      [self.beiji, "北极"],
                      [self.caihong1, "彩虹1"],
                      [self.caihong2, "彩虹2"],
                      [self.miaohong, "描红"],
                      [self.heire, "黑热"],
                      [self.caihong2, "彩虹2"],
                      [self.beiji, "北极"],
                      [self.retie, "热铁"],
                      [self.rongyan, "熔岩"],
                      [self.baire, "白热"]]
            distinguish_list = []
            text_list = []
            for ev in values:
                text, distinguish1, distinguish2 = self.set_ev("Yuntai_adjustment_007", ev[0], ev[1])
                distinguish_list.append(distinguish1)
                distinguish_list.append(distinguish2)
                text_list.append(text)
            self.driver.click(self.x, self.y)
            return text_list, distinguish_list
        except BaseException as a:
            self.failed_operation()
            raise a

    def Yuntai_adjustment_008(self):
        try:
            self.set_type("红外")
            self.operation_load(1)
            self.driver.swipe(1296, 474, 1607, 474)
            sleep(2)
            self.driver.swipe(1296, 474, 1607, 474)
            sleep(2)
            values = [[self.light_x1, "x1"],
                      [self.light_x2, "x2"],
                      [self.light_x4, "x4"],
                      [self.light_x8, "x8"],
                      [self.light_x4, "x4"],
                      [self.light_x2, "x2"],
                      [self.light_x1, "x1"]]
            distinguish_list = []
            text_list = []
            for ev in values:
                text, distinguish1, distinguish2 = self.set_ev("Yuntai_adjustment_006", ev[0], ev[1])
                distinguish_list.append(distinguish1)
                distinguish_list.append(distinguish2)
                text_list.append(text)
            self.driver.click(self.x, self.y)
            return text_list, distinguish_list
        except BaseException as a:
            self.failed_operation()
            raise a

    def Yuntai_adjustment_009(self):
        try:
            self.set_type("红外")
            self.operation_load(1)
            self.driver.click(1309, 642)
            sleep(5)
            text1 = self.driver(resourceId="com.gdu.pro2:id/tv_irda_setting_brightness").get_text()
            photo1 = self.photo_video_distinguish("Yuntai_adjustment_008")[0]
            self.driver.click(self.x, self.y)
            mylog.info(F"设置红外亮度为：{text1}---------出图情况：{photo1}")
            sleep(2)
            self.operation_load(1)
            self.driver.click(1779, 642)
            sleep(5)
            text2 = self.driver(resourceId="com.gdu.pro2:id/tv_irda_setting_brightness").get_text()
            self.driver.click(1500, 642)
            sleep(2)
            photo2 = self.photo_video_distinguish("Yuntai_adjustment_008")[0]
            self.driver.click(self.x, self.y)
            mylog.info(F"设置红外亮度为：{text2}---------出图情况：{photo2}")
            sleep(2)
            return [text1, text2], [photo1, photo2]
        except BaseException as a:
            self.failed_operation()
            raise a

    def Yuntai_adjustment_010(self):
        try:
            self.set_type("红外")
            self.operation_load(1)
            self.driver.click(1307, 790)
            sleep(5)
            text1 = self.driver(resourceId="com.gdu.pro2:id/tv_irda_setting_contrast").get_text()
            photo1 = self.photo_video_distinguish("Yuntai_adjustment_009")[0]
            self.driver.click(0.286, 0.176)
            mylog.info(F"设置红外亮度为：{text1}---------出图情况：{photo1}")
            sleep(2)
            self.operation_load(1)
            self.driver.click(1789, 790)
            sleep(5)
            text2 = self.driver(resourceId="com.gdu.pro2:id/tv_irda_setting_contrast").get_text()
            photo2 = self.photo_video_distinguish("Yuntai_adjustment_009")[0]
            self.driver.click(1500, 790)
            sleep(2)
            self.driver.click(self.x, self.y)
            mylog.info(F"设置红外亮度为：{text2}---------出图情况：{photo2}")
            sleep(2)
            return [text1, text2], [photo1, photo2]
        except BaseException as a:
            self.failed_operation()
            raise a