from time import sleep
from common.loger_handler import mylog
from page_element.page_key import PageKey


class InitStart(PageKey):
    """初始化操作"""

    def login_operation(self):
        """登录操作"""
        user_element = self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/email_layout"]/android.widget.FrameLayout[1]')
        user_element.click()
        user_element.set_text("18186466491")
        sleep(1)
        password_element = self.driver.xpath('//*[@resource-id="com.gdu.pro2:id/ll_subLayout1"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]')
        password_element.click()
        password_element.set_text("Ab123456")
        sleep(2)
        self.driver.click(1866, 702)
        self.driver(resourceId="com.gdu.pro2:id/Tv_Login2Register_Button").click()
        sleep(2)

    def init_start_operation(self, test=True):
        """初始化前置操作"""
        sleep(2)
        self.driver.xpath("//*[contains(@text,'同意并继续')]").click()
        sleep(4)

        # 登录操作
        self.login_operation()
        try:
            self.quxiao.click()
        except BaseException:
            pass

        # 开启模拟环境
        for i in range(5):
            self.appIcon.click()
        sleep(1)
        self.driver(resourceId="com.gdu.pro2:id/et_inputContent").click()
        self.driver(resourceId="com.gdu.pro2:id/et_inputContent").set_text("gdu1235")
        sleep(1)
        self.driver.click(1852, 679)
        self.queding.click()
        mylog.info(F"*****初始化*****调试模式已开启")
        sleep(3)

        if test:
            # 进入设置页面
            self.open_manualflybtn()
            self.set_type("可见光")
            self.all_set.click()

            # 设置信道模式
            self.all_set_003.click()
            self.driver(resourceId="com.gdu.pro2:id/ov_switch_img_channel").click()
            self.driver.xpath('//android.widget.ListView/android.widget.LinearLayout[2]').click()
            sleep(2)
            xindao = self.driver(resourceId="com.gdu.pro2:id/ov_switch_img_channel").get_text()
            mylog.info(F"*****初始化*****信道设置结果：{xindao}")

            # 关闭返航避障
            self.all_set_006.click()
            sleep(1)
            self.driver.swipe(1251, 1130, 1236, 150)
            sleep(3)
            fhbz = self.driver(resourceId="com.gdu.pro2:id/iv_goHomeObstacleSwitch")
            if fhbz.info.get('selected'):
                fhbz.click()
                sleep(2)
            mylog.info(F"*****初始化*****关闭返航避障结果：{fhbz.info.get('selected')}")

            # 开启模拟飞行
            self.all_set_001.click()
            sleep(1)
            self.driver.swipe(1261, 950, 1248, 500)
            sleep(3)
            mnfx = self.driver(resourceId="com.gdu.pro2:id/iv_switch_simulate")
            if not mnfx.info.get('selected'):
                mnfx.click()
                sleep(2)
            mylog.info(F"*****初始化*****模拟飞行设置结果：{mnfx.info.get('selected')}")

            # 关闭音效
            self.all_set_008.click()
            sleep(1)
            self.driver(resourceId="com.gdu.pro2:id/iv_voice_tip").click()

            # 初始化SD卡
            self.set_clear_sdcard()

            # 回到主页
            self.open_homepage()
            mylog.info(F"*****初始化*****设置完成回到首页")

    def open_taskflybtn(self):
        """打开任务飞行"""
        self.taskFlyBtn.click()
        sleep(1)

    def open_manualflybtn(self):
        """打开手动飞行"""
        self.manualFlyBtn.click()
        sleep(2)
        self.sdfx_close.click()
        sleep(4)
        self.driver(resourceId="com.gdu.pro2:id/video1_container").click()
        sleep(2)

    def open_homepage(self):
        sleep(1)
        self.driver.click(self.x, self.y)
        self.logo.click()
        sleep(1)




