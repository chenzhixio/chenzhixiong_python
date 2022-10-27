import os
import re
import time
from time import sleep
from common.loger_handler import mylog
from common.conf_handle import Config
from common.ftp_handler import LinkFTP
from page_element.test_page_key import test_page_load


class test_Photograph_and_video(test_page_load):
    """云台拍照录像"""

    def Judge_as_video(self, name):
        """4种模式分别录像"""
        self.set_type(name)
        if not self.recording_time.exists():
            self.switch.click()
        sleep(2)
        self.start.click()
        sleep(55)
        text0 = self.recording_time.get_text()
        text00 = int(text0[-2:])
        sleep(1)
        self.start.click()
        sleep(2)
        self.album.click()
        sleep(1)
        if self.iv_paly.exists():
            self.iv_paly.click()
            sleep(5)
            self.driver.click(1367, 567)
            sleep(1)
            text1 = self.playtime.get_text()
            self.driver.click(1380, 914)
            sleep(1)
            text2 = self.playtime.get_text()
            self.iv_paly.click()
            sleep(60)
            text3 = self.playtime.get_text()
            text4 = self.playendtime.get_text()
            if int(text4[:2]) == 1:
                text5 = int(text4[-2:]) + 60
            else:
                text5 = int(text4[-2:])
            self.del_picture()
            mylog.info(F"播放5秒后视频时间为：{text1}")
            mylog.info(F"滑动进度条后时间为：{text2}")
            mylog.info(F"播放完成后时间为：{text3}")
            mylog.info(F"录像总时长为：{text00}")
            mylog.info(F"视频总时长为：{text5}")
            if text5 < text00:
                text = "视频时长 < 录像时长（BUG）"
            elif (text1 != "00:00") and (text2 != text1) and (text3 == "00:00"):
                text = "视频录像，播放正常"
            else:
                text = "视频录像，播放有误"
        else:
            text = "视频有误"
        mylog.info(F"{name}模式播放：{text}")
        self.driver.click(503, 270)
        return text

    def Judge_as_photo(self, name):
        """4种模式分别拍照"""
        self.set_type(name)
        if self.recording_time.exists():
            self.switch.click()
        for i in range(4):
            sleep(6)
            self.start.click()
        sleep(3)
        self.album.click()
        sleep(3)
        photo_4 = self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/hl_cover"]/android.widget.RelativeLayout[4]/android.widget.ImageView[1]').exists
        if photo_4:
            text = "拍照成功，4张照片"
            for i in range(4):
                sleep(2)
                self.del_picture()
        else:
            text = "拍照失败，不足4张照片"
        sleep(3)
        while self.iv_delete.exists():
            self.del_picture()
            sleep(2)
        mylog.info(F"{name}模式，连续拍照4张：{text}")
        return text

    def Pseudo_color_operation(self, name, elemet):
        self.operation_load_1()
        sleep(2)
        elemet.click()
        sleep(2)
        self.driver.click(336, 276)
        self.set_Video_or_picture("拍照")
        self.set_Video_or_picture("视频")
        self.album.click()
        sleep(2)
        if self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/hl_cover"]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]').exists:
            if self.iv_paly.exists():
                text = "视频录制成功，拍照成功"
            else:
                text = "视频录制失败，2张均为照片"
            self.del_picture()
            self.del_picture()
        else:
            if self.iv_paly.exists():
                text = "视频录制成功，拍照失败"
            else:
                text = "视频录制失败，拍照成功"
            self.del_picture()
        mylog.info(F"伪彩{name}模式，{text}")
        self.driver.click(0.286, 0.176)
        return text

    def judge_Video_or_picture(self):
        """判断相册的图片是照片还是视频"""
        if self.driver(resourceId="com.gdu.pro2:id/iv_paly").exists():
            text = "视频"
        else:
            text = "照片"
        return text

    def photo_video_01(self):
        try:
            self.set_clear_album()
            sleep(3)
            text1 = self.Judge_as_video("可见光")
            sleep(3)
            text2 = self.Judge_as_video("红外")
            sleep(3)
            text3 = self.Judge_as_video("分屏")
            sleep(3)
            return [text1, text2, text3]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def photo_video_02(self):
        try:
            self.set_clear_album()
            sleep(5)
            text1 = self.Judge_as_photo("可见光")
            sleep(5)
            text2 = self.Judge_as_photo("红外")
            sleep(5)
            text3 = self.Judge_as_photo("分屏")
            sleep(5)
            return [text1, text2, text3]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def photo_video_03(self):
        try:
            self.set_clear_album()
            self.set_type("可见光")
            sleep(3)
            self.set_Video_or_picture("拍照")
            self.set_Video_or_picture("视频")
            self.set_Video_or_picture("拍照")
            self.set_Video_or_picture("视频")
            self.album.click()
            sleep(2)
            text1 = self.judge_Video_or_picture()
            mylog.info(F"当前图片为：{text1}")
            self.del_picture()
            text2 = self.judge_Video_or_picture()
            mylog.info(F"当前图片为：{text2}")
            self.del_picture()
            text3 = self.judge_Video_or_picture()
            mylog.info(F"当前图片为：{text3}")
            self.del_picture()
            text4 = self.judge_Video_or_picture()
            mylog.info(F"当前图片为：{text4}")
            self.del_picture()
            return [text1, text2, text3, text4]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def photo_video_04(self):
        try:
            self.set_clear_album()
            self.set_type("可见光")
            sleep(2)
            if self.recording_time.exists():
                self.switch.click()
            sleep(3)
            text1 = self.recording_time.exists()
            mylog.info(F"拍照模式，无录像时间控件：{text1}")
            self.switch.click()
            sleep(5)
            text2 = self.recording_time.exists()
            mylog.info(F"切换模式为录像，有录像时间控件：{text2}")
            self.start.click()
            sleep(5)
            self.switch.click()
            sleep(5)
            text3 = self.recording_time.exists()
            mylog.info(F"录像过程中无法切换，有录像时间控件：{text3}")
            self.start.click()
            sleep(5)
            self.switch.click()
            sleep(5)
            text4 = self.recording_time.exists()
            mylog.info(F"录像结束后可以正常切换，无录像时间控件：{text4}")
            self.album.click()
            sleep(3)
            self.del_picture()
            self.driver.click(524, 205)
            sleep(3)
            return [text1, text2, text3, text4]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def photo_video_05(self):
        try:
            self.set_clear_album()
            sleep(2)
            if self.recording_time.exists():
                self.switch.click()
            sleep(5)
            for i in range(20):
                self.start.click()
                mylog.info(F"连续拍照第{i+1}张")
                sleep(4)
            self.album.click()
            sleep(2)
            for i in range(19):
                self.del_picture()
                mylog.info(F"连续删除第{i + 1}张")
            text = self.iv_delete.exists()
            self.del_picture()
            self.driver.click(524, 205)
            return text
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def photo_video_06(self):
        try:
            self.set_clear_sdcard()
            self.set_clear_album()
            self.set_type("可见光")
            self.set_Video_or_picture("拍照")
            self.set_Video_or_picture("视频")
            P = LinkFTP(host="145.192.1.20", port=21, username="gdu", password="123456")
            photo_list = P.path_list("PHOTO")
            video_list = P.path_list("VIDEO")
            mylog.info(F"SD卡照片：{photo_list}")
            mylog.info(F"SD卡视频：{video_list}")
            photo_local_path = Config.data_ftp_path + F"\\{photo_list[0]}"
            video_local_path = Config.data_ftp_path + F"\\{video_list[0]}"
            photo_ftp_path = F"/mmcblk1p1/IR/PHOTO/{photo_list[0]}"
            video_ftp_path = F"/mmcblk1p1/IR/VIDEO/{video_list[0]}"
            P.download_file(photo_ftp_path, photo_local_path)
            P.download_file(video_ftp_path, video_local_path)
            sleep(3)
            text = os.listdir(Config.data_ftp_path)
            mylog.info(F"下载后的文件：{text}")
            for i in text:
                os.remove(Config.data_ftp_path + F"\\{i}")
            return len(text)
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def photo_video_07(self):
        try:
            self.set_clear_sdcard()
            self.set_type("可见光")
            self.set_Video_or_picture("视频", outtime=200)
            self.operation_set_load()
            self.driver.swipe(1261, 900, 1261, 500)
            sleep(3)
            text = self.driver(resourceId="com.gdu.pro2:id/SD_size").get_text()
            mylog.info(F"拍摄视频200s后，可见光存储容量为：{text}")
            self.driver.click(0.286, 0.176)
            return text
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def photo_video_08(self):
        try:
            self.set_clear_sdcard()
            self.set_clear_album()
            self.set_type("红外")
            self.driver.click(336, 276)
            self.operation_load_1()
            for i in range(3):
                self.driver.swipe(1338, 284, 1776, 284)
                sleep(3)
            list1 = ["白热", "熔岩", "铁红", "热铁", "医疗", "北极", "彩虹1", "彩虹2", "描红", "黑热"]
            list2 = []
            for i in list1:
                n = self.driver(resourceId="com.gdu.pro2:id/tv_content", text=i)
                text = self.Pseudo_color_operation(i, n)
                list2.append(text)
            self.driver.click(336, 276)
            self.operation_load_1()
            for i in range(3):
                self.driver.swipe(1338, 284, 1776, 284)
                sleep(3)
            mylog.info(F"========{list2}=======")
            return list2
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def photo_video_09(self):
        try:
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
            self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/rc_gallery"]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
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
            self.xuanzhe .click()
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
            self.xuanzhe .click()
            sleep(1)
            self.photo1.click()
            sleep(1)
            self.photo2.click()
            sleep(1)
            self.driver.click(1843, 1130)
            sleep(1)
            self.queding.click()
            sleep(2)
            text5 = self.photo1.exists
            mylog.info(F"视频，图片删除完成：{not text5}")
            sleep(1)
            self.driver.click(1843, 1130)
            sleep(1)
            self.queding.click()
            sleep(1)
            self.rwfx_return.click()
            sleep(1)
            self.manualFlightBg.click()
            sleep(2)
            self.rwfx_close.click()
            sleep(4)
            return [text1, text2, text3, text4, text5]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a

    def photo_video_10(self):
        try:
            self.set_clear_sdcard()
            self.set_clear_album()
            self.set_type("可见光")
            self.set_Video_or_picture("视频", 2)
            self.album.click()
            sleep(2)
            if self.iv_delete.exists():
                text1 = "2秒录像成功"
                self.del_picture()
            else:
                text1 = "2秒录像失败"
            mylog.info(F"========{text1}")
            self.start.click()
            sleep(2)
            self.switch.click()
            sleep(5)
            if self.recording_time.exists():
                text2 = "录像过程中切换拍照失败"
            else:
                text2 = "录像过程中切换拍照成功"
            mylog.info(F"========{text2}")
            sleep(3)
            self.all_set.click()
            sleep(2)
            if self.driver.xpath("//*[contains(@text,'飞行设置')]").exists:
                text3 = "录像过程中可以查看飞行设置"
                self.driver.click(368, 273)
            else:
                text3 = "录像过程中不可以查看飞行设置"
            mylog.info(F"========{text3}")
            sleep(3)
            self.angle.click()
            sleep(2)
            if self.driver(resourceId="com.gdu.pro2:id/tv_title", text="可见光电子放大").exists():
                text4 = "录像过程中可以设置云台"
                self.driver.click(368, 273)
            else:
                text4 = "录像过程中不可以查看飞行设置"
            mylog.info(F"========{text4}")
            sleep(2)
            self.operation_load_2()
            self.look_down.click()
            sleep(3)
            text5 = self.get_value()
            mylog.info(F"录像过程中设置云台向下角度：{text5}")
            self.operation_load_2()
            self.hui_zhong.click()
            sleep(3)
            text6 = self.get_value()
            mylog.info(F"录像过程中设置云台回中角度：{text6}")
            sleep(60)
            self.start.click()
            sleep(5)
            P = LinkFTP(host="145.192.1.20", port=21, username="gdu", password="123456")
            video_list = P.path_list("VIDEO")
            mylog.info(F"录像10分钟后，SD卡视频条数：{video_list}")
            return [text1, text2, text3, text4, text5, text6, video_list]
        except BaseException as a:
            self.failed_operation_sdfx()
            raise a






































