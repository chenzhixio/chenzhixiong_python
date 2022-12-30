import time
import re
from time import sleep
from common.loger_handler import mylog
from common.path_handler import Config
from common.conf_handle import myconf
from common.ftp_handler import LinkFTP
from page_element.page_key import PageKey


class test_page_load_currency(PageKey):
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
        text2 = re.findall(r"\d{1,3}", text)[0]
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

    def failed_enter_page(self, num):
        """进入任务飞行的子项"""
        if num == 1:
            self.rwfx_one.click()
            sleep(2)
            self.rwfx_map.click()
            sleep(2)
        elif num == 2:
            self.rwfx_two.click()
        elif num == 3:
            self.rwfx_three.click()
        else:
            self.rwfx_hjdr.click()
        sleep(2)
        self.driver.double_click(737, 626, 0.1)
        sleep(2)
        self.driver.double_click(737, 626, 0.1)
        sleep(2)


    def judge_whether_to_end(self):
        """循环判断，当水平与高度都为0时结束"""
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
            if (text1 == "0.0m") and (text2 == 0):
                mylog.info(F'任务结束时间：{time.strftime("%Y-%m-%d %H：%M：%S", time.localtime())}')
                break
            elif (time.time() - locattime) > 1800:
                mylog.info(F'任务结束时间：{time.strftime("%Y-%m-%d %H：%M：%S", time.localtime())}')
                break
            else:
                mylog.info(F"任务飞行中----------高度：{text2}  角度：{text3}   距离：{text1}")
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

    def failed_operation_sdfx(self):
        """手动飞行失败后操作"""
        sleep(1)
        self.driver.click(self.x, self.y)
        sleep(2)
        localtime = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        sleep(1)
        if self.recording_time.exists():
            playtime = self.recording_time.get_text()
            if playtime != "00:00":
                self.start.click()
        text = self.driver(resourceId="com.gdu.pro2:id/tv_layout_head_title").get_text()
        mylog.info(F"**************请确认是否为断连：{text}*************{localtime}*****")
        sleep(1)
        self.driver.screenshot(Config.bugpng_path + F'\\{localtime}_{text}.png')


    def rwfx_001(self):
        try:
            self.failed_enter_page(3)
            sleep(1)
            self.payload_group.click()
            self.payload_name.click()
            sleep(1)
            self.driver.swipe(1255, 520, 1500, 520)
            sleep(2)
            self.driver.swipe(1255, 945, 1280, 945)
            sleep(2)
            yuntai = self.driver(resourceId="com.gdu.pro2:id/et_gdu_seek_bar_value")[0].get_text()
            gaodu = self.driver(resourceId="com.gdu.pro2:id/et_gdu_seek_bar_value")[1].get_text()
            mylog.info(F"云台角度：{yuntai},{type(yuntai)}------航线高度：{gaodu},{type(yuntai)}")
            self.driver.swipe(1547, 892, 1547, 415)
            sleep(2)
            self.driver.swipe(1547, 892, 1547, 415)
            sleep(2)
            self.driver.xpath(
                '//*[@resource-id="com.gdu.pro2:id/gs_finished_action"]/android.view.ViewGroup[1]/android.widget.Spinner[1]').click()
            self.driver(text="自动返航").click()
            sleep(1)
            self.img_select_area.click()
            sleep(1)
            text1 = self.hdsm_number.get_text()
            text2 = self.zpzs_number.get_text()
            mylog.info(F"设置页面：航点数：{text1}-----拍照数：{text2}")
            self.img_begin_fly.click()
            self.driver.xpath("//*[contains(@text,'下一步')]").click()
            sleep(1)
            text3 = self.hdsm_number.get_text()
            text4 = self.zpzs_number.get_text()
            mylog.info(F"上传页面：航点数：{text3}-----拍照数：{text4}")
            self.driver.xpath("//*[contains(@text,'上传航迹')]").click()
            sleep(10)
            self.driver.xpath("//*[contains(@text,'开始飞行')]").click()
            sleep(2)
            self.container.click()
            list_height, list_massge = self.judge_whether_to_end()
            mylog.info(F"航迹过程中：\n高度：{list_height}\n云台角度：{list_massge}")
            sleep(5)
            self.logo.click()
            sleep(5)
            return [gaodu, yuntai], [text1, text2, text3, text4], list_height, list_massge
        except BaseException as e:
            self.failed_operation()
            raise e

    def rwfx_002(self):
        try:
            self.failed_enter_page(2)
            sleep(1)
            self.payload_group.click()
            self.payload_name.click()
            sleep(1)
            self.driver.swipe(1269, 746, 1280, 746)
            sleep(2)
            gaodu = self.driver(resourceId="com.gdu.pro2:id/et_gdu_seek_bar_value")[0].get_text()
            mylog.info(F"航线高度：{gaodu}")
            self.driver.swipe(1547, 892, 1547, 415)
            sleep(2)
            self.driver.swipe(1547, 892, 1547, 415)
            sleep(2)
            self.driver.xpath(
                '//*[@resource-id="com.gdu.pro2:id/gs_finished_action"]/android.view.ViewGroup[1]/android.widget.Spinner[1]').click()
            self.driver(text="自动返航").click()
            self.img_select_area.click()
            sleep(1)
            text1 = self.hdsm_number.get_text()
            text2 = self.zpzs_number.get_text()
            mylog.info(F"设置页面：航点数：{text1}-----拍照数：{text2}")
            self.img_begin_fly.click()
            self.driver.xpath("//*[contains(@text,'下一步')]").click()
            sleep(1)
            text3 = self.hdsm_number.get_text()
            text4 = self.zpzs_number.get_text()
            mylog.info(F"上传页面：航点数：{text3}-----拍照数：{text4}")
            self.driver.xpath("//*[contains(@text,'上传航迹')]").click()
            sleep(10)
            self.driver.xpath("//*[contains(@text,'开始飞行')]").click()
            sleep(2)
            self.container.click()
            list_height, list_massge = self.judge_whether_to_end()
            mylog.info(F"航迹过程中：\n高度：{list_height}\n云台角度：{list_massge}")
            sleep(5)
            self.logo.click()
            sleep(5)
            return [gaodu], [text1, text2, text3, text4], list_height, list_massge
        except BaseException as e:
            self.failed_operation()
            raise e

    def rwfx_003(self):
        try:
            self.failed_enter_page(1)
            sleep(1)
            self.payload_group.click()
            self.payload_name.click()
            sleep(1)
            self.driver(resourceId="com.gdu.pro2:id/img_route_setting").click()
            self.driver.swipe(1269, 544, 1280, 544)
            sleep(2)
            gaodu = self.driver(resourceId="com.gdu.pro2:id/et_gdu_seek_bar_value")[1].get_text()
            mylog.info(F"航线高度：{gaodu}")
            self.driver.swipe(1547, 892, 1547, 415)
            sleep(2)
            self.driver.swipe(1547, 892, 1547, 415)
            sleep(2)
            self.driver.xpath(
                '//*[@resource-id="com.gdu.pro2:id/gs_finished_action"]/android.view.ViewGroup[1]/android.widget.Spinner[1]').click()
            self.driver(text="自动返航").click()
            xy = [300, 400, 500, 600, 700]
            for i in xy:
                for j in xy:
                    self.driver.click(i, j)
                    sleep(0.7)
            sleep(1)
            self.driver(resourceId="com.gdu.pro2:id/img_way_point_setting").click()
            self.driver.swipe(1537, 938, 1528, 452)
            sleep(2)
            for i in range(20):
                self.driver(resourceId="com.gdu.pro2:id/btn_add_point_action").click()
                sleep(0.5)
                self.driver(resourceId="com.gdu.pro2:id/tv_take_photo").click()
                sleep(0.5)
                self.driver.click(1311, 160)
                sleep(0.5)
                self.driver.click(1311, 160)
            text1 = self.hdsm_number.get_text()
            text2 = self.zpzs_number.get_text()
            mylog.info(F"设置页面：航点数：{text1}-----拍照数：{text2}")
            self.img_begin_fly.click()
            self.driver.xpath("//*[contains(@text,'下一步')]").click()
            sleep(1)
            text3 = self.hdsm_number.get_text()
            text4 = self.zpzs_number.get_text()
            mylog.info(F"上传页面：航点数：{text3}-----拍照数：{text4}")
            self.driver.xpath("//*[contains(@text,'上传航迹')]").click()
            sleep(10)
            self.driver.xpath("//*[contains(@text,'开始飞行')]").click()
            sleep(2)
            self.container.click()
            list_height, list_massge = self.judge_whether_to_end()
            mylog.info(F"航迹过程中：\n高度：{list_height}\n云台角度：{list_massge}")
            sleep(5)
            self.logo.click()
            sleep(5)
            return [gaodu], [text1, text2, text3, text4], list_height, list_massge
        except BaseException as e:
            self.failed_operation()
            raise e