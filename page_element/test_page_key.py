import re
import time
import os
from time import sleep
from common.loger_handler import mylog
from common.conf_handle import myconf
from common.path_handler import Config
from common.ui_handler import Browser
from common.noticed_handler import newnotice


class test_page_load(Browser):
    """云台挂载测试用例"""

    def __init__(self, driver):
        """重新父类的初始化"""

        # 实例化
        self.driver = driver

        # 常用
        self.xuanzhe = self.driver.xpath("//*[contains(@text,'选择')]")
        self.queding = self.driver.xpath("//*[contains(@text,'确定')]")
        self.rwfx_return = self.driver(resourceId="com.gdu.pro2:id/iv_back")  # 返回按钮

        # 首页按钮
        self.logo = self.driver(resourceId="com.gdu.pro2:id/iv_zorroRealcontrol_back")  # 内层log
        self.mission_flight = self.driver(resourceId="com.gdu.pro2:id/iv_taskFlyBtn")  # 任务飞行
        self.manualFlightBg = self.driver(resourceId="com.gdu.pro2:id/iv_manualFlyBtn")  # 手动飞行
        self.cloudName_1 = self.driver(resourceId="com.gdu.pro2:id/tv_cloudName_1")  # 云台名称
        self.albumLayout = self.driver(resourceId="com.gdu.pro2:id/cl_albumLayout")  # 相册
        self.set_set = self.driver(resourceId="com.gdu.pro2:id/iv_selfBtn")    # 设置
        self.subLayout3 = self.driver(resourceId="com.gdu.pro2:id/cl_subLayout3")   # 健康管理

        # 媒体相册
        self.videoDetail_play = driver(resourceId="com.gdu.pro2:id/checkbox_videoDetail_play")  # 播放按钮
        # 相册图1
        self.photo1 = self.driver.xpath(
            '//*[@resource-id="com.gdu.pro2:id/gr_item"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]')
        self.photo2 = self.driver.xpath(
            '//*[@resource-id="com.gdu.pro2:id/gr_item"]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]')

        # 任务飞行
        self.rwfx_one = self.driver.xpath("//*[contains(@text,'航点飞行')]")
        self.rwfx_two = self.driver.xpath("//*[contains(@text,'二维飞行')]")
        self.rwfx_three = self.driver.xpath("//*[contains(@text,'三维飞行')]")
        self.rwfx_dlxj = self.driver(resourceId="com.gdu.pro2:id/iv_elec_flight")
        self.rwfx_close = self.driver(resourceId="com.gdu.pro2:id/iv_closeBtn")         # 关闭
        self.taskFlyBackBtn = self.driver(resourceId="com.gdu.pro2:id/iv_taskFlyBackBtn")  # 大退
        self.rwfx_new = self.driver.xpath("//*[contains(@text,'新建任务')]")
        self.rwfx_map = self.driver.xpath("//*[contains(@text,'地图选点')]")

        self.hdsm_number = self.driver(resourceId="com.gdu.pro2:id/tv_flight_number")  # 航点数目
        self.zpzs_number = self.driver(resourceId="com.gdu.pro2:id/tv_allPhotoNumContent")  # 总拍照数
        self.load_number = self.driver(resourceId="com.gdu.pro2:id/tv_angle_current_set")  # 云台俯仰边界值
        self.start_fly = self.driver(resourceId="com.gdu.pro2:id/iv_start_fly")  # 开始飞行

        # 全局设置
        self.all_set = self.driver(resourceId="com.gdu.pro2:id/iv_zorroRealcontrol_set")
        self.flight_set = self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/rv_left"]/android.view.ViewGroup[1]')
        self.soc_set = self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/rv_left"]/android.view.ViewGroup[2]')
        self.graphic_set = self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/rv_left"]/android.view.ViewGroup[3]')
        self.rtk_set = self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/rv_left"]/android.view.ViewGroup[4]')
        self.remote_control_set = self.driver.xpath(
            '//*[@resource-id="com.gdu.pro2:id/rv_left"]/android.view.ViewGroup[5]')
        self.perception_set = self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/rv_left"]/android.view.ViewGroup[6]')
        self.load_set = self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/rv_left"]/android.view.ViewGroup[7]')
        self.currency_set = self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/rv_left"]/android.view.ViewGroup[8]')

        # 相机设置
        self.anti_flicker = self.driver(resourceId="com.gdu.pro2:id/ov_anti_flicker")  # 抗闪烁
        self.video_quality = self.driver(resourceId="com.gdu.pro2:id/ov_video_quality")  # 视频尺寸
        self.photo_size = self.driver(resourceId="com.gdu.pro2:id/ov_photo_size_click")  # 照片分辨率
        self.pitch_speed = self.driver(resourceId="com.gdu.pro2:id/tv_pitch_speed")
        self.enhance_mode = self.driver(resourceId="com.gdu.pro2:id/ov_enhance_mode")  # 增益模式

        # 遥控器设置----自定义按键
        self.customize_keys = self.driver.xpath("//*[contains(@text,'遥控器自定义按键')]")
        self.keys_c1 = self.driver(resourceId="com.gdu.pro2:id/tv_c1")
        self.keys_c2 = self.driver(resourceId="com.gdu.pro2:id/tv_c2")

        self.set_type_yuntai = self.driver.xpath(
            '//*[@resource-id="com.gdu.pro2:id/rv_title"]/android.view.ViewGroup[2]/android.widget.ImageView[1]')  # 云台
        self.set_type_yuntai_huizhong = self.driver.xpath("//*[contains(@text,'云台回中')]")
        self.set_type_yuntai_xiashi = self.driver.xpath("//*[contains(@text,'云台朝下')]")

        self.angle = self.driver(resourceId="com.gdu.pro2:id/icon_camera")  # 云台设置按钮
        self.angle_1 = self.driver(resourceId="com.gdu.pro2:id/iv_gt")  # 云台设置选项1
        self.angle_2 = self.driver(resourceId="com.gdu.pro2:id/iv_live")  # 云台设置选项2


        # 飞行器版本信息
        self.fxqxx1 = self.driver.xpath("//*[contains(@text,'飞行器信息')]")
        self.fxqxx2 = self.driver(resourceId="com.gdu.pro2:id/tv_currentVersion_fly")   # 飞控版本
        self.fxqxx3 = self.driver(resourceId="com.gdu.pro2:id/tv_currentVersion_batter")  # 智能电池版本
        self.fxqxx4 = self.driver(resourceId="com.gdu.pro2:id/tv_currentVersion_ota")     # 系统版本


        # EV滑动
        self.EV_f3 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="-3")  # EV_____-3
        self.EV_f2 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="-2")  # EV_____-2
        self.EV_f1 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="-1")  # EV_____-1
        self.EV_0 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="0")  # EV_____0
        self.EV_1 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="1")  # EV_____1
        self.EV_2 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="2")  # EV_____2
        self.EV_3 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="3")  # EV_____3

        self.light_x0 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="x0")  # 可见光---x0
        self.light_x1 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="x1")  # 可见光---x1
        self.light_x2 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="x2")  # 可见光---x2
        self.light_x4 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="x4")  # 可见光---x4
        self.light_x8 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="x8")  # 可见光---x8
        self.light_x16 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="x32")  # 可见光---x16
        self.light_x32 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="x32")  # 可见光---x32

        self.baire = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="白热")
        self.rongyan = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="熔岩")
        self.tiehong = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="铁红")
        self.retie = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="热铁")
        self.yiliao = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="医疗")
        self.beiji = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="北极")
        self.caihong1 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="彩虹1")
        self.caihong2 = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="彩虹2")
        self.miaohong = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="描红")
        self.heire = self.driver(resourceId="com.gdu.pro2:id/tv_content", text="黑热")

        # 微调
        self.iv_roll_plus = self.driver(resourceId="com.gdu.pro2:id/iv_roll_plus")
        self.iv_roll_minus = self.driver(resourceId="com.gdu.pro2:id/iv_roll_minus")
        # 回中，下视
        self.hui_zhong = self.driver.xpath("//*[contains(@text,'回中')]")
        self.look_down = self.driver.xpath("//*[contains(@text,'下视')]")
        # 内层角度
        self.tv_roll_value = self.driver(resourceId="com.gdu.pro2:id/tv_roll_value")
        # 外层角度
        self.tv_angle = self.driver(resourceId="com.gdu.pro2:id/tv_angle")
        # 报文字幕
        self.message1 = self.driver(resourceId="com.gdu.pro2:id/tv_arlink")
        # 切换按钮
        self.switch = self.driver(resourceId="com.gdu.pro2:id/icon_switch")
        # 开始录像/拍照
        self.start = self.driver(resourceId="com.gdu.pro2:id/iv_video")
        # 录像时间
        self.recording_time = self.driver(resourceId="com.gdu.pro2:id/chronometer")

        # 相册
        self.album = self.driver(resourceId="com.gdu.pro2:id/icon_gallery")  # 相册
        self.iv_paly = self.driver(resourceId="com.gdu.pro2:id/iv_paly")  # 播放按钮
        self.iv_delete = driver(resourceId="com.gdu.pro2:id/iv_delete")  # 删除按钮
        self.playtime = self.driver(resourceId="com.gdu.pro2:id/tv_videoDetail_playTime")  # 视频开始时间
        self.playendtime = self.driver(resourceId="com.gdu.pro2:id/tv_videoDetail_allTime")  # 视频结束时间

        self.distance = self.driver(resourceId="com.gdu.pro2:id/tv_dis")  # 水平距离
        self.height = self.driver(resourceId="com.gdu.pro2:id/tv_height")  # 垂直高度

        self.visible_light = self.driver.xpath("//*[contains(@text,'可见光')]")  # 可见光
        self.infra_red = self.driver.xpath("//*[contains(@text,'红外')]")        # 红外
        self.split_screen = self.driver.xpath("//*[contains(@text,'分屏')]")     # 分屏

    def get_message_value(self):
        """获取报文对于数据"""
        text = re.findall(r"云台俯仰角度：-?\d{1,2}", self.message1.get_text())
        text2 = text[0][7:]
        text3 = F"{text2}°"
        return text3

    def get_value_int(self, value):
        """获取度数并转换为int类型"""
        text = re.findall(r"-?\d{1,2}", value)
        text2 = int(text[0])
        return text2

    def get_value(self):
        """
        获取当前：内层角度，外层角度, 报文角度
        前提：在设置页面使用
        """
        try:
            text1 = self.tv_roll_value.get_text()   # 先获取内层角度
            self.driver.click(0.286, 0.176)
            sleep(2)
            text2 = self.tv_angle.get_text()        # 后获取外层角度
            sleep(2)
            text3 = self.get_message_value()        # 屏幕文字角度
            assert text1 == text2
            assert text1 == text3
            text = self.get_value_int(text1)
            return text
        except AssertionError:
            mylog.info(F"问题：设置页面角度与外层角度不一致")
            return ""

    def operation_load_1(self):
        """进入云台俯仰页面"""
        sleep(1)
        self.driver.click(336, 276)
        sleep(1)
        self.angle.click()
        sleep(1)
        self.angle_1.click()
        sleep(2)

    def operation_load_2(self):
        """进入云台俯仰页面"""
        self.driver.click(336, 276)
        sleep(1)
        self.angle.click()
        sleep(1)
        self.angle_2.click()
        sleep(2)

    def operation_set_load(self):
        """进入设置----相机设置"""
        self.driver.click(336, 276)
        sleep(1)
        self.all_set.click()
        sleep(1)
        self.load_set.click()
        sleep(3)

    def del_picture(self):
        """删除相册相片"""
        try:
            sleep(2)
            self.iv_delete.click()
            sleep(1)
            self.queding.click()
            sleep(1)
        except Exception:
            pass

    def set_type(self, name):
        """设置拍照模式"""
        sleep(2)
        if name == "可见光":
            if self.visible_light.exists:
                self.visible_light.click()
        elif name == "红外":
            if self.infra_red.exists:
                self.infra_red.click()
        elif name == "分屏":
            if self.split_screen.exists:
                self.split_screen.click()
        sleep(2)

    def set_photo_video(self, name):
        """切换到拍照或录像"""
        sleep(2)
        text = self.recording_time.exists()
        if name == "拍照":
            if text:
                self.switch.click()
        else:
            if not text:
                self.switch.click()
        sleep(2)

    def set_Video_or_picture(self, name, outtime=10):
        """进行拍照或录像"""
        if name == "视频":
            if not self.recording_time.exists():
                self.switch.click()
                sleep(2)
            sleep(3)
            self.start.click()
            sleep(outtime)
            self.start.click()
        else:
            if self.recording_time.exists():
                self.switch.click()
                sleep(5)
            self.start.click()
        sleep(5)

    def set_clear_sdcard(self):
        """清除飞机SD卡内存"""
        self.driver.click(336, 276)
        sleep(1)
        self.all_set.click()
        sleep(1)
        self.load_set.click()
        sleep(1)
        self.driver.swipe(1261, 900, 1261, 500)
        sleep(3)
        self.driver(resourceId="com.gdu.pro2:id/tv_clear_data_ir").click()
        sleep(1)
        self.driver(resourceId="com.gdu.pro2:id/dialog_btn_sure").click()
        sleep(4)
        self.driver(resourceId="com.gdu.pro2:id/tv_clear_data").click()
        sleep(1)
        self.driver(resourceId="com.gdu.pro2:id/dialog_btn_sure").click()
        sleep(4)
        text = self.driver(resourceId="com.gdu.pro2:id/SD_size").get_text()
        mylog.info(F"完成SD卡内存清空, 可见光存储容量：{text}")
        self.driver.click(336, 276)
        sleep(2)

    def set_clear_album(self):
        """清除遥控器相册"""
        devices = myconf.get("user", "devices")
        os.system(F"adb -s {devices} shell rm -rf /sdcard/gdu/flight2")
        sleep(3)

    def failed_operation_sdfx(self):
        """手动飞行失败后操作"""
        sleep(1)
        self.driver.click(291, 326)
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


