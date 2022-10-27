import os
import re
import time
from time import sleep
from common.loger_handler import mylog
from common.conf_handle import Config
from common.ftp_handler import LinkFTP
from page_element.test_page_key import test_page_load


class test_s400all_test(test_page_load):
    """云台拍照录像"""

    def s400all_005(self):
        sleep(2)
        text1 = self.cloudName_1.get_text()
        mylog.info(F"挂载云台识别名称：{text1}")
        self.manualFlightBg.click()
        sleep(1)
        self.rwfx_close.click()
        sleep(4)
        self.operation_load_2()
        self.hui_zhong.click()
        sleep(3)
        text2 = self.get_value()
        mylog.info(F"控制云台回中后角度为：{text2}")
        self.operation_load_2()
        self.look_down.click()
        sleep(3)
        text3 = self.get_value()
        mylog.info(F"控制云台下视后角度为：{text3}")
        sleep(2)
        return [text1, text2, text3]

    def s400all_006(self):
        self.set_clear_sdcard()
        self.set_clear_album()
        self.set_type("可见光")
        self.set_Video_or_picture("拍照")
        self.set_Video_or_picture("拍照")
        self.set_Video_or_picture("拍照")
        self.set_Video_or_picture("视频", 60)
        self.logo.click()
        sleep(1)
        self.albumLayout.click()
        sleep(1)
        self.driver.xpath(
            '//*[@resource-id="com.gdu.pro2:id/rc_gallery"]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        sleep(1)
        self.driver(resourceId="com.gdu.pro2:id/iv_video_icon").click()
        sleep(1)
        text1 = self.playtime.get_text()
        sleep(1)
        mylog.info(F"============={text1}")
        self.videoDetail_play.click()
        sleep(5)
        self.driver.click(956, 579)
        sleep(1)
        self.driver.click(956, 579)
        sleep(2)
        text2 = self.playtime.get_text()
        mylog.info(F"============={text2}")
        self.driver.click(921, 1029)
        sleep(1)
        text3 = self.playtime.get_text()
        mylog.info(F"============={text3}")
        self.videoDetail_play.click()
        sleep(5)
        self.driver.click(956, 579)
        sleep(1)
        self.driver.click(956, 579)
        sleep(1)
        text4 = self.playtime.get_text()
        sleep(1)
        mylog.info(F"============={text4}")
        self.rwfx_return.click()
        sleep(1)
        self.xuanzhe.click()
        sleep(1)
        self.driver(resourceId="com.gdu.pro2:id/iv_cover").click()
        sleep(1)
        self.driver.click(1843, 1130)
        sleep(1)
        self.queding.click()
        sleep(1)
        self.driver.click(1843, 1130)
        sleep(1)
        self.queding.click()
        sleep(1)
        self.driver(resourceId="com.gdu.pro2:id/iv_cover").click()
        sleep(1)
        self.photo1.click()
        sleep(1)
        self.driver.click(1843, 1130)
        sleep(1)
        self.queding.click()
        sleep(1)
        self.rwfx_return.click()
        sleep(1)
        self.xuanzhe.click()
        sleep(1)
        self.photo1.click()
        sleep(1)
        self.photo2.click()
        sleep(1)
        self.driver.click(1843, 1130)
        sleep(1)
        self.queding.click()
        sleep(1)
        self.driver.click(1843, 1130)
        sleep(1)
        self.queding.click()
        sleep(2)
        text5 = self.photo1.exists
        self.rwfx_return.click()
        mylog.info(F"视频，图片删除完成：{not text5}")
        return [text1, text2, text3, text4, text5]

    def s400all_010(self):
        sleep(2)
        self.set_set.click()
        sleep(2)
        self.driver.xpath("//*[contains(@text,'关于我们')]").click()
        text1 = self.driver(resourceId="com.gdu.pro2:id/tv_aboutMe_AppVersion").get_text()
        mylog.info(F"关于我们页面版本号正常显示：{text1}")
        self.driver.xpath("//*[contains(@text,'关于普宙')]").click()
        sleep(1)
        text2 = self.driver(className="android.widget.TextView")[1].get_text()
        mylog.info(F"关于普宙页面加载正常，显示内容：{text2}")
        self.rwfx_return.click()
        sleep(1)
        self.driver.xpath("//*[contains(@text,'意见反馈')]").click()
        sleep(2)
        self.driver(resourceId="com.gdu.pro2:id/edit_feedback").send_keys("测试意见反馈")
        sleep(1)
        self.driver.click(1856, 692)
        self.driver.click(1856, 692)
        sleep(1)
        self.driver(resourceId="com.gdu.pro2:id/edit_email").send_keys("747206339@qq.com")
        sleep(1)
        self.driver.click(1856, 692)
        self.driver.click(1856, 692)
        sleep(1)
        self.driver.xpath("//*[contains(@text,'提交')]").click()
        sleep(15)
        self.driver.click(51, 58)
        sleep(1)
        self.driver.xpath("//*[contains(@text,'联系我们')]").click()
        sleep(1)
        text3 = self.driver(resourceId="com.gdu.pro2:id/tv_ItemMenu_Value", text="400-040-0266").get_text()
        mylog.info(F"联系我们页面加载正常，正确显示电话：{text3}")
        sleep(1)
        self.rwfx_return.click()
        sleep(1)
        self.rwfx_return.click()
        sleep(1)
        self.rwfx_return.click()
        sleep(1)
        return [text1, text2, text3]

    def s400all_012(self):
        self.set_set.click()
        sleep(1)
        self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/ll_my_head_set"]/android.widget.TextView[1]').click()
        sleep(1)
        self.driver.xpath("//*[contains(@text,'清除缓存')]").click()
        self.driver(resourceId="com.gdu.pro2:id/dialog_btn_sure").click()
        sleep(2)
        text1 = self.driver(resourceId="com.gdu.pro2:id/tv_cacheSize").get_text()
        mylog.info(F"清除缓存后：{text1}")
        text2 = self.driver(resourceId="com.gdu.pro2:id/tv_appset_appVersion").get_text()
        mylog.info(F"：当前版本号为：{text2}")
        self.driver.xpath("//*[contains(@text,'隐私政策')]").click()
        sleep(1)
        text3 = self.driver(text="GDU隐私政策").get_text()
        mylog.info(F"：隐私政策页面内容包含：{text3}")
        self.rwfx_return.click()
        sleep(1)
        self.rwfx_return.click()
        sleep(1)
        self.rwfx_return.click()
        return [text1, text2, text3]

    def s400all_013(self):
        sleep(2)
        self.mission_flight.click()
        sleep(1)
        text1 = self.rwfx_one.exists
        text2 = self.rwfx_two.exists
        text3 = self.rwfx_three.exists
        text4 = self.rwfx_dlxj.exists()
        mylog.info(F"成功进入任务飞行页面：{text1}，{text2}，{text3}， {text4}")
        sleep(2)
        self.taskFlyBackBtn.click()
        sleep(1)
        self.manualFlightBg.click()
        sleep(1)
        self.rwfx_close.click()
        sleep(5)
        text5 = self.album.exists()
        text6 = self.start.exists()
        mylog.info(F"成功进入手动飞行页面：{text5}, {text6}")
        sleep(1)
        self.logo.click()
        return [text1, text2, text3, text4, text5]

    def s400all_015(self):
        sleep(2)
        self.subLayout3.click()
        sleep(1)
        text1 = self.driver(resourceId="com.gdu.pro2:id/tv_flightConnectStatus").get_text()
        mylog.info(F"连接状态：{text1}")
        text_list = []
        for i in range(8):
            text = self.driver.xpath(F'//*[@resource-id="com.gdu.pro2:id/rv_statusContent"]/android.view.ViewGroup[{i+1}]/android.widget.TextView[2]').get_text()
            text_list.append(text)
        mylog.info(F"有用设备状态：{text_list}")
        sleep(2)
        self.driver(resourceId="com.gdu.pro2:id/iv_backBtn").click()
        return text1, text_list

    def s400all_019(self):
        sleep(2)
        self.manualFlightBg.click()
        sleep(1)
        text1 = self.driver(resourceId="com.gdu.pro2:id/tv_type_name")[0].get_text()
        text2 = self.driver(resourceId="com.gdu.pro2:id/tv_type_name")[1].get_text()
        text3 = self.driver(resourceId="com.gdu.pro2:id/tv_type_name")[2].get_text()
        text4 = self.driver(resourceId="com.gdu.pro2:id/tv_type_name")[5].get_text()
        text5 = self.driver(resourceId="com.gdu.pro2:id/tv_type_name")[6].get_text()
        mylog.info(F"飞行前检查，飞行模式为：{text1}")
        mylog.info(F"飞行前检查，飞行器电量为：{text2}")
        mylog.info(F"飞行前检查，遥控器电量为：{text3}")
        mylog.info(F"飞行前检查，存储卡为：{text4}")
        mylog.info(F"飞行前检查，遥控控制为：{text5}")
        self.rwfx_close.click()
        sleep(5)
        text6 = self.driver(resourceId="com.gdu.pro2:id/tv_currentIsSportModel").get_text()
        text7 = self.driver(resourceId="com.gdu.pro2:id/tv_aircraft").get_text()
        text8 = self.driver(resourceId="com.gdu.pro2:id/tv_electricity_control").get_text()
        mylog.info(F"手动飞行页面，挡位为：{text6}")
        mylog.info(F"手动飞行页面，飞行器电量为：{text7}")
        mylog.info(F"手动飞行页面，遥控器电量为：{text8}")
        sleep(2)
        self.logo.click()
        return [text1, text2, text3, text4, text5, text6, text7, text8]


























