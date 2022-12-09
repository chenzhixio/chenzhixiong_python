from time import sleep
from common.loger_handler import mylog
from common.conf_handle import Config, myconf
from common.opencv_handle import erweima_function, screenshot_png
from page_element.page_key import PageKey


class test_Photograph_and_video(PageKey):
    """云台拍照录像"""

    def Judge_as_photo(self, name, type, num):
        """3种模式分别拍照"""
        try:
            self.set_type(name)
            self.set_clear_album()
            for i in range(num):
                self.set_Video_or_picture(type)
            self.album.click()
            distinguish_list = []
            for i in range(num):
                sleep(1)
                if type == "视频":
                    self.iv_paly.click()
                    sleep(2)
                photo = self.driver(resourceId="com.gdu.pro2:id/btn_PauseVideo")
                photo.screenshot().save(F"{Config.screenshot_path}\\test_005.png")
                if name == "分屏":
                    screenshot_png(F"{Config.screenshot_path}\\test_005.png")
                distinguish = erweima_function(F"{Config.screenshot_path}\\test_005.png")
                distinguish_list.append(distinguish)
                mylog.info(F"第{i+1}张照片图像识别结果：{distinguish}")
                self.del_picture()
            sleep(3)
            if (len(distinguish_list) == num) and ("二维码识别失败" not in distinguish_list):
                return "拍照正常"
            else:
                return "识别失败"
        except BaseException:
            return "存在漏拍"

    def judge_Video_or_picture(self):
        """判断相册的图片是照片还是视频"""
        sleep(2)
        if self.iv_paly.exists():
            text1 = "视频"
            self.iv_paly.click()
            sleep(2)
        else:
            text1 = "照片"
        self.driver.screenshot(F"{Config.screenshot_path}\\test_006.png")
        text2 = erweima_function(F"{Config.screenshot_path}\\test_006.png")
        return text1, text2

    def photo_video_01(self):
        try:
            text1 = self.Judge_as_photo("可见光", "视频", 20)
            mylog.info(F"可见光拍照20张：{text1}")
            sleep(5)
            text2 = self.Judge_as_photo("红外", "视频", 20)
            mylog.info(F"红外拍照20张：{text2}")
            sleep(5)
            text3 = self.Judge_as_photo("分屏", "视频", 20)
            mylog.info(F"分屏拍照20张：{text3}")
            sleep(5)
            return [text1, text2, text3]
        except BaseException as a:
            self.failed_operation()
            raise a

    def photo_video_02(self):
        try:
            text1 = self.Judge_as_photo("可见光", "拍照", 20)
            mylog.info(F"可见光拍照20张：{text1}")
            sleep(5)
            text2 = self.Judge_as_photo("红外", "拍照", 20)
            mylog.info(F"红外拍照20张：{text2}")
            sleep(5)
            text3 = self.Judge_as_photo("分屏", "拍照", 20)
            mylog.info(F"分屏拍照20张：{text3}")
            sleep(5)
            return [text1, text2, text3]
        except BaseException as a:
            self.failed_operation()
            raise a

    def photo_video_03(self):
        try:
            self.set_clear_album()
            self.set_type("可见光")
            sleep(3)
            for i in range(5):
                self.set_Video_or_picture("拍照")
                self.set_Video_or_picture("视频", 10)
            self.album.click()
            sleep(2)
            text_list = []
            distinguish_list = []
            for i in range(10):
                text, distinguish = self.judge_Video_or_picture()
                mylog.info(F"当前图片为：{text}, 图像识别：{distinguish}")
                self.del_picture()
                text_list.append(text)
                distinguish_list.append(distinguish)
            return text_list, distinguish_list
        except BaseException as a:
            self.failed_operation()
            raise a
