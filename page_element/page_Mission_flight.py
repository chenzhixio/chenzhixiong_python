import time
import re
from time import sleep
from common.loger_handler import mylog
from common.path_handler import Config
from common.ftp_handler import LinkFTP
from page_element.test_page_key import test_page_load


class test_page_load_currency(test_page_load):
    """任务飞行"""

    def set_Flight_speed(self):
        """获取新建页面飞行速度"""
        sleep(2)
        for i in range(13):
            sleep(0.1)
            self.driver(resourceId="com.gdu.pro2:id/iv_speed_add").click()

    def set_Mission_height(self):
        """设置新建页面任务高度"""
        self.driver(resourceId="com.gdu.pro2:id/iv_height_add").click()
        sleep(1)
        text = self.driver(resourceId="com.gdu.pro2:id/tv_height_current_set").get_text()
        text2 = re.findall(r"\d{1,2}", text)[0]
        text3 = int(text2)
        mylog.info(F"设置任务高度：{text3}")
        return text3

    def set_Angle_current(self):
        """设置新建页面云台俯仰角度"""
        self.driver(resourceId="com.gdu.pro2:id/iv_clound_add").click()
        sleep(1)
        text = self.driver(resourceId="com.gdu.pro2:id/tv_angle_current_set").get_text()
        mylog.info(F"设置云台俯仰角度：{text}")
        return text

    def get_Mission_height(self):
        """获取飞行高度"""
        text = self.height.get_text()
        text2 = re.findall(r"\d{1,2}", text)[0]
        text3 = int(text2)
        return text3

    def operation_rwfx_one(self, type):
        self.driver.swipe(1497, 872, 1497, 600)
        sleep(1)
        self.driver.swipe(1497, 872, 1497, 600)
        self.driver(resourceId="com.gdu.pro2:id/tv_flight_point_action").click()
        sleep(1)
        self.driver.xpath("//*[contains(@text,'添加动作')]").click()
        if type == "结束录像":
            self.driver.swipe(1438, 861, 1438, 717)
        elif type == "变倍":
            self.driver.swipe(1438, 861, 1438, 717)
            sleep(1)
            self.driver.swipe(1438, 861, 1438, 717)
            sleep(1)
            self.driver.swipe(1438, 861, 1438, 717)
        self.driver.xpath(F"//*[contains(@text,'{type}')]").click()
        self.driver.xpath("//*[contains(@text,'完成')]").click()
        self.driver(resourceId="com.gdu.pro2:id/iv_flight_action_back").click()
        self.driver.swipe(1497, 600, 1497, 890)
        sleep(1)
        self.driver.swipe(1497, 600, 1497, 890)

    def failed_operation(self):
        """执行失败是返回到任务飞行页面"""
        self.driver.screenshot(Config.bugpng_path + F'\\{time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())}.png')
        self.rwfx_return.click()
        text = self.rwfx_one.exists
        if text == False:
            self.rwfx_return.click()

    def failed_enter_page(self, num, clear=True):
        """进入任务飞行的子项"""
        if num == 4:
            self.rwfx_dlxj.click()
        else:
            if num == 1:
                self.rwfx_one.click()
            elif num == 2:
                self.rwfx_two.click()
            elif num == 3:
                self.rwfx_three.click()
            sleep(1)
            if clear:
                self.set_clear_sdcard()
            self.rwfx_new.click()
            self.rwfx_map.click()
            sleep(2)
            self.driver.double_click(576, 416, 0.1)
            sleep(2)


    def judge_whether_to_end(self):
        """循环判断，当水平与高度都为0时结束"""
        self.start_fly.click()
        sleep(15)
        self.driver.xpath("//*[contains(@text,'开始飞行')]").click()
        mylog.info(F'任务开始时间：{time.strftime("%Y-%m-%d %H：%M：%S", time.localtime())}')
        locattime = time.time()
        list_height = []
        list_massge = []
        sleep(15)
        while True:
            sleep(5)
            text1 = self.distance.get_text()
            text2 = self.get_Mission_height()
            text3 = self.get_message_value()
            list_height.append(text2)
            list_massge.append(text3)
            if (text1 == "0.0m") and (text2 == 0.0):
                mylog.info(F'任务结束时间：{time.strftime("%Y-%m-%d %H：%M：%S", time.localtime())}')
                break
            elif (time.time() - locattime) > 1000:
                mylog.info(F'任务结束时间：{time.strftime("%Y-%m-%d %H：%M：%S", time.localtime())}')
                break
        return list_height, list_massge

    def get_load_number(self, x1, y1, x2, y2):
        sleep(2)
        text1 = self.load_number.get_text()
        self.driver.click(x1, y1)
        sleep(2)
        text2 = self.load_number.get_text()
        self.driver.swipe(x1, y1, x2, y2)
        sleep(3)
        text3 = self.load_number.get_text()
        return text1, text2, text3

    def get_number(self, element):
        self.angle.click()
        self.angle_2.click()
        sleep(2)
        element.click()
        sleep(2)
        text = self.get_value()
        return text


    def rwfx_001(self):
        try:
            self.failed_enter_page(3)
            sleep(1)
            self.driver.click(919, 562)
            sleep(1)
            self.driver.click(892, 596)
            sleep(1)
            self.driver.click(956, 584)
            sleep(5)
            self.driver.swipe(1522, 589, 1522, 950)
            sleep(2)
            self.driver.swipe(1522, 589, 1522, 950)
            sleep(2)
            self.set_Flight_speed()                    # 设置飞行速度
            height_text = self.set_Mission_height()    # 设置飞行高度
            current_text = self.set_Angle_current()    # 设置云台角度
            number1 = self.hdsm_number.get_text()
            number2 = self.zpzs_number.get_text()
            mylog.info(F"航点数目：{number1}    拍照总数：{number2}")
            self.driver.swipe(1497, 872, 1497, 600)
            self.driver.swipe(1497, 872, 1497, 600)
            self.driver(resourceId="com.gdu.pro2:id/tv_flight_point_action").click()                # 悬停时间
            self.driver.xpath('//android.widget.ListView/android.widget.LinearLayout[1]').click()   # 悬停时间选择1S
            self.queding.click()
            list_height, list_massge = self.judge_whether_to_end()
            mylog.info(F"任务飞行过程中连续获取飞行高度为：{list_height}")
            mylog.info(F"任务飞行过程中连续获取云台角度为：{list_massge}")
            P = LinkFTP(host="145.192.1.20", port=21, username="gdu", password="123456")
            number3 = len(P.path_list("PHOTO"))
            mylog.info(F"总计拍照张数为：{number3}")
            sleep(2)
            self.logo.click()
            sleep(1)
            self.mission_flight.click()
            return [number1, number2, number3, height_text, current_text, list_height, list_massge]
        except BaseException as e:
            self.failed_operation()
            raise e

    def rwfx_002(self):
        try:
            self.failed_enter_page(2)
            self.driver.click(0.394, 0.483)
            sleep(1)
            self.driver.click(0.358, 0.57)
            sleep(1)
            self.driver.click(0.436, 0.57)
            sleep(2)
            self.driver.swipe(1522, 589, 1522, 950)
            sleep(2)
            self.driver.swipe(1522, 589, 1522, 950)
            sleep(2)
            self.set_Flight_speed()                    # 设置飞行速度
            height_text = self.set_Mission_height()    # 设置飞行高度
            current_text = self.set_Angle_current()    # 设置云台角度
            number1 = self.hdsm_number.get_text()
            number2 = self.zpzs_number.get_text()
            mylog.info(F"航点数目：{number1}    拍照总数：{number2}")
            self.driver.swipe(1505, 806, 1499, 677)
            sleep(1)
            self.driver.swipe(1497, 872, 1497, 600)
            self.driver(resourceId="com.gdu.pro2:id/tv_flight_point_action").click()  # 悬停时间
            self.driver.xpath('//android.widget.ListView/android.widget.LinearLayout[1]').click()  # 悬停时间选择1S
            self.queding.click()
            list_height, list_massge = self.judge_whether_to_end()
            mylog.info(F"任务飞行过程中连续获取飞行高度为：{list_height}")
            mylog.info(F"任务飞行过程中连续获取云台角度为：{list_massge}")
            P = LinkFTP(host="145.192.1.20", port=21, username="gdu", password="123456")
            number3 = len(P.path_list("PHOTO"))
            mylog.info(F"总计拍照张数为：{number3}")
            sleep(2)
            self.logo.click()
            sleep(1)
            self.mission_flight.click()
            return [number1, number2, number3, height_text, current_text, list_height, list_massge]
        except BaseException as e:
            self.failed_operation()
            raise e

    def rwfx_003(self):
        try:
            self.failed_enter_page(1)
            self.driver.click(0.394, 0.483)
            sleep(1)
            self.driver.click(0.358, 0.57)
            sleep(1)
            self.driver.click(0.436, 0.57)
            sleep(1)
            self.driver.click(0.455, 0.428)
            sleep(2)
            self.driver.swipe(1522, 589, 1522, 950)
            sleep(2)
            self.driver.swipe(1522, 589, 1522, 950)
            sleep(2)
            self.set_Flight_speed()                  # 设置飞行速度
            height_text = self.set_Mission_height()  # 设置飞行高度
            current_text = self.set_Angle_current()  # 设置云台角度
            self.driver.xpath("//*[contains(@text,'航点设置')]").click()
            self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/dr_listview"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
            self.operation_rwfx_one("拍照")
            self.driver(resourceId="com.gdu.pro2:id/iv_flight_next_point").click()
            self.operation_rwfx_one("开始录像")
            self.driver(resourceId="com.gdu.pro2:id/iv_flight_next_point").click()
            self.operation_rwfx_one("结束录像")
            self.driver(resourceId="com.gdu.pro2:id/iv_flight_next_point").click()
            self.operation_rwfx_one("变倍")
            list_height, list_massge = self.judge_whether_to_end()
            mylog.info(F"任务飞行过程中连续获取飞行高度为：{list_height}")
            mylog.info(F"任务飞行过程中连续获取云台角度为：{list_massge}")
            P = LinkFTP(host="145.192.1.20", port=21, username="gdu", password="123456")
            number1 = len(P.path_list("PHOTO"))
            number2 = len(P.path_list("VIDEO"))
            mylog.info(F"总计拍照张数为：{number1}")
            mylog.info(F"总计录像条数为：{number2}")
            sleep(2)
            self.logo.click()
            sleep(1)
            self.mission_flight.click()
            return [number1, number2, height_text, current_text, list_height, list_massge]
        except BaseException as e:
            self.failed_operation()
            raise e

    def rwfx_004(self):
        try:
            self.set_clear_album()
            self.failed_enter_page(1, False)
            text1, text2, text3 = self.get_load_number(1335, 951, 1777, 951)
            mylog.info(F"航点飞行-任务的通用设置-云台俯仰角设置-------默认值：{text1} 最小值：{text2} 最大值：{text3}")
            self.driver.click(0.394, 0.483)
            sleep(2)
            self.driver.click(0.358, 0.57)
            sleep(2)
            self.driver.xpath("//*[contains(@text,'航点设置')]").click()
            self.driver.xpath(
                '//*[@resource-id="com.gdu.pro2:id/dr_listview"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
            sleep(2)
            self.driver.swipe(1497, 872, 1497, 500)
            sleep(1)
            self.driver.xpath("//*[contains(@text,'自定义')]").click()

            text4, text5, text6 = self.get_load_number(1777, 639, 1335, 639)
            mylog.info(F"航点飞行-任务的航点设置-航点动作的云台俯仰角度自定义-------默认值：{text4} 最小值：{text6} 最大值：{text5}")
            self.rwfx_return.click()
            self.rwfx_return.click()
            self.failed_enter_page(2, False)
            sleep(4)
            text7, text8, text9 = self.get_load_number(1335, 576, 1777, 576)
            mylog.info(F"二维飞行-任务的常规设置-云台俯仰角设置-------默认值：{text7} 最小值：{text8} 最大值：{text9}")
            self.rwfx_return.click()
            self.rwfx_return.click()
            self.failed_enter_page(3, False)
            sleep(4)
            text10, text11, text12 = self.get_load_number(1335, 588, 1777, 588)
            mylog.info(F"三维飞行-任务的常规设置-云台俯仰角设置-------默认值：{text10} 最小值：{text11} 最大值：{text12}")
            self.rwfx_return.click()
            self.rwfx_return.click()
            return [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12]
        except BaseException as e:
            self.failed_operation()
            raise e