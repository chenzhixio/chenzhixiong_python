import os
import re
import time
from time import sleep
from common.opencv_handle import erweima_function
from common.loger_handler import mylog
from common.conf_handle import Config
from page_element.page_init import InitStart


class test_s400all_test(InitStart):
    """云台拍照录像"""

    def s400all_001(self):
        self.open_manualflybtn()
        self.operation_set_load(8)
        self.fxqxx1.click()
        sleep(1)
        self.driver.swipe(1200, 900, 1200, 300)
        sleep(3)
        text1 = self.driver(resourceId="com.gdu.pro2:id/tv_current_version")[2].get_text()
        text2 = self.driver(resourceId="com.gdu.pro2:id/tv_current_version")[3].get_text()
        text5 = self.driver(resourceId="com.gdu.pro2:id/tv_gimbal_sn").get_text()
        self.driver.swipe(1200, 900, 1200, 300)
        sleep(3)
        self.driver.swipe(1200, 900, 1200, 300)
        sleep(3)
        text3 = self.driver(resourceId="com.gdu.pro2:id/tv_ptzArmSystemVersion").get_text()
        text4 = self.driver(resourceId="com.gdu.pro2:id/tv_ptzArmVersion").get_text()
        mylog.info(F"\n云台版本：{text1}\n可见光版本：{text2}\n云台Arm系统版本：{text3}\n云台Arm版本：{text4}\nSN:{text5}")
        sleep(2)
        self.open_homepage()
        return [text1, text2, text3, text4, text5]

    def s400all_005(self):
        sleep(2)
        name = self.cloudName_1.get_text()
        mylog.info(F"挂载云台识别名称：{name}")
        return name

    def s400all_006(self):
        self.open_manualflybtn()
        self.set_type("可见光")
        for i in range(4):
            self.set_Video_or_picture("拍照")
        self.set_Video_or_picture("视频", 60)
        for i in range(3):
            self.set_Video_or_picture("视频", 10)
        self.open_homepage()
        self.albumLayout.click()
        sleep(1)
        # 视频播放测试
        self.driver(resourceId="com.gdu.pro2:id/iv_video_gallery").click()
        sleep(2)
        video4 = self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/gr_item"]/android.widget.RelativeLayout[4]/android.widget.ImageView[1]')
        video_exists_1 = video4.exists     # 判断视频是否有4条--True
        if video_exists_1:
            mylog.info("视频断言：没有漏拍")
        else:
            mylog.info("视频断言：存在漏拍")
        video4.click()
        sleep(1)
        time1 = self.playtime.get_text()
        sleep(1)
        mylog.info(F"视频播放：初始时间--{time1}")
        self.videoDetail_play.click()
        sleep(5)
        self.driver.click(956, 579)
        self.driver.click(956, 579)
        sleep(2)
        time2 = self.playtime.get_text()
        mylog.info(F"视频播放：播放几秒--{time2}")
        self.driver.click(921, 1029)      # 托进度条
        sleep(1)
        time3 = self.playtime.get_text()
        mylog.info(F"视频播放：托进度条--{time3}")
        self.videoDetail_play.click()
        sleep(5)
        self.driver.click(956, 579)
        self.driver.click(956, 579)
        sleep(1)
        time4 = self.playtime.get_text()
        mylog.info(F"视频播放：继续播放--{time4}")
        self.videoDetail_play.click()
        sleep(15)
        photo = self.driver(resourceId="com.gdu.pro2:id/fl_videoDetail")
        photo_path = F"{Config.screenshot_path}\\s400all_006_video.png"
        photo.screenshot().save(photo_path)
        distinguish1 = erweima_function(photo_path)
        mylog.info(F"播放过程中视觉识别：{distinguish1}")
        sleep(15)
        time5 = self.playtime.get_text()
        mylog.info(F"视频播放：结束播放--{time5}")

        # 删除单条视频
        self.driver.click(1835, 1132)
        self.queding.click()
        self.rwfx_return.click()
        sleep(1)
        video_exists_2 = video4.exists    # 判断视频第4条是否被删除--False
        if video_exists_2:
            mylog.info("单条视频删除：失败")
        else:
            mylog.info("单条视频删除：成功")

        # 删除多条视频
        sleep(2)
        self.xuanzhe.click()
        sleep(1)
        self.driver.click(1841, 177)
        sleep(1)
        self.driver.click(1835, 1132)
        self.queding.click()
        sleep(2)
        video_exists_3 = self.driver(resourceId="com.gdu.pro2:id/iv_cover").exists()  # 判断视频是否被删除完--False
        if video_exists_3:
            mylog.info("批量视频删除：失败")
            self.rwfx_return.click()
        else:
            mylog.info("批量视频删除：成功")
            self.driver.click(1835, 1132)
            self.queding.click()

        # 查看照片
        sleep(2)
        self.driver(resourceId="com.gdu.pro2:id/iv_cover").click()
        photo4 = self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/gr_item"]/android.widget.RelativeLayout[4]/android.widget.ImageView[1]')
        sleep(2)
        photo_exists_1 = photo4.exists    # 判断照片是否有4条--True
        if photo_exists_1:
            mylog.info("拍照断言：没有漏拍")
        else:
            mylog.info("拍照断言：存在漏拍")
        sleep(1)
        photo4.click()
        sleep(1)
        photo = self.driver.xpath('//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]')
        photo_path = F"{Config.screenshot_path}\\s400all_006_photo.png"
        photo.screenshot().save(photo_path)
        distinguish2 = erweima_function(photo_path)
        mylog.info(F"播放过程中视觉识别：{distinguish2}")

        # 删除单张照片
        self.driver.click(1835, 1132)
        self.queding.click()
        self.rwfx_return.click()
        photo4 = self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/gr_item"]/android.widget.RelativeLayout[4]/android.widget.ImageView[1]')
        photo_exists_2 = photo4.exists     # 判断照片第4张是否被删除--False
        sleep(2)
        if photo_exists_2:
            mylog.info("单张照片删除：失败")
        else:
            mylog.info("单张照片删除：成功")

        # 删除多张照片
        sleep(2)
        self.xuanzhe.click()
        sleep(1)
        self.driver.click(1841, 177)
        sleep(1)
        self.driver.click(1835, 1132)
        self.queding.click()
        sleep(2)
        photo_exists_3 = self.driver(resourceId="com.gdu.pro2:id/iv_cover").exists()   # 判断照片是否被删除完--False
        if photo_exists_3:
            mylog.info("批量照片删除：失败")
            self.rwfx_return.click()
        else:
            mylog.info("批量照片删除：成功")
            self.driver.click(1835, 1132)
            self.queding.click()
        sleep(1)
        self.rwfx_return.click()
        return [time1, time2, time3, time4, time5], \
               [distinguish1, distinguish2], \
               [video_exists_1, video_exists_2, video_exists_3 , photo_exists_1, photo_exists_2, photo_exists_3]

    def s400all_010(self):
        sleep(2)
        self.selfBtn.click()
        sleep(2)
        self.driver.xpath("//*[contains(@text,'关于我们')]").click()
        text1 = self.driver(resourceId="com.gdu.pro2:id/tv_aboutMe_AppVersion").get_text()
        mylog.info(F"版本信息：{text1}")
        self.driver.xpath("//*[contains(@text,'联系我们')]").click()
        sleep(1)
        text3 = self.driver(resourceId="com.gdu.pro2:id/tv_ItemMenu_Value", text="400-040-0266").get_text()
        text4 = self.driver(resourceId="com.gdu.pro2:id/tv_ItemMenu_Value", text="sales@gdu-tech.com").get_text()
        text5 = self.driver(resourceId="com.gdu.pro2:id/tv_ItemMenu_Value", text="support@gdu-tech.com").get_text()
        mylog.info(F"产品咨询热线：{text3}")
        mylog.info(F"销售：{text4}")
        mylog.info(F"服务：{text5}")
        sleep(1)
        self.rwfx_return.click()
        sleep(1)
        self.rwfx_return.click()
        sleep(1)
        self.rwfx_return.click()
        sleep(1)
        return [text1, text3, text4, text5]

    def s400all_012(self):
        self.selfBtn.click()
        sleep(1)
        self.driver(resourceId="com.gdu.pro2:id/tv_typeName", text="设置").click()
        sleep(1)
        self.driver.xpath("//*[contains(@text,'清除缓存')]").click()
        sleep(2)
        self.driver(resourceId="com.gdu.pro2:id/tv_photo_cache_clean").click()
        sleep(2)
        self.driver(resourceId="com.gdu.pro2:id/tv_firmware_clean").click()
        sleep(2)
        self.driver(resourceId="com.gdu.pro2:id/tv_app_clean").click()
        sleep(2)
        self.driver(resourceId="com.gdu.pro2:id/tv_log_clean").click()
        sleep(2)
        text1 = self.driver(resourceId="com.gdu.pro2:id/tv_all_size").get_text()
        mylog.info(F"清除缓存后：{text1}")
        self.rwfx_return.click()
        text2 = self.driver(resourceId="com.gdu.pro2:id/tv_appset_appVersion").get_text()
        mylog.info(F"当前版本号为：{text2}")
        sleep(1)
        self.driver.xpath("//*[contains(@text,'隐私政策')]").click()
        sleep(1)
        text3 = self.driver(text="GDU隐私政策").get_text()
        mylog.info(F"隐私政策页面内容包含：{text3}")
        self.rwfx_return.click()
        sleep(1)
        self.rwfx_return.click()
        sleep(1)
        self.rwfx_return.click()
        return [text1, text2, text3]

    def s400all_013(self):
        sleep(2)
        self.taskFlyBtn.click()
        sleep(1)
        text1 = self.rwfx_one.exists
        text2 = self.rwfx_two.exists
        text3 = self.rwfx_three.exists
        text4 = self.rwfx_hjdr.exists
        mylog.info(F"成功进入任务飞行页面：{text1}，{text2}，{text3}， {text4}")
        sleep(2)
        self.rwfx_close.click()
        sleep(2)
        self.open_manualflybtn()
        sleep(5)
        text5 = self.album.exists()
        text6 = self.start.exists()
        mylog.info(F"成功进入手动飞行页面：{text5}, {text6}")
        sleep(1)
        self.logo.click()
        return [text1, text2, text3, text4, text5, text6]

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
        self.manualFlyBtn.click()
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
        self.sdfx_close.click()
        sleep(4)
        self.driver(resourceId="com.gdu.pro2:id/video1_container").click()
        sleep(2)
        text6 = self.driver(resourceId="com.gdu.pro2:id/tv_currentIsSportModel").get_text()
        text7 = self.driver(resourceId="com.gdu.pro2:id/tv_aircraft").get_text()
        text8 = self.driver(resourceId="com.gdu.pro2:id/tv_electricity_control").get_text()
        mylog.info(F"手动飞行页面，挡位为：{text6}")
        mylog.info(F"手动飞行页面，飞行器电量为：{text7}")
        mylog.info(F"手动飞行页面，遥控器电量为：{text8}")
        sleep(2)
        self.logo.click()
        sleep(3)
        return [text1, text2, text3, text4, text5, text6, text7, text8]


























