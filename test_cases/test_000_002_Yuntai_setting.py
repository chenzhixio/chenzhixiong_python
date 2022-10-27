import pytest
from common.loger_handler import mylog
from page_element.page_Yuntai_setting import test_Yuntai_setting


@pytest.mark.usefixtures('init_manual_flight')
class Test_Yuntai_setting(object):
    """云台俯仰调节"""

    @pytest.mark.debug
    @pytest.mark.debug_setting
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_setting_000(self, get_drivers):
        mylog.info(F"===================================正在测试：可见光，红外，分屏模式切换测试============================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list = self.drivers.Yuntai_setting_000()
        try:
            for i in text_list:
                assert i == False
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_setting
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_setting_001(self, get_drivers):
        mylog.info(F"===================================正在测试：可见光抗闪烁设置测试============================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list = self.drivers.Yuntai_setting_001()
        try:
            assert text_list[0] == "关闭"
            assert text_list[1] == "50Hz"
            assert text_list[2] == "60Hz"
            assert text_list[3] == "关闭"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_setting
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_setting_002(self, get_drivers):
        mylog.info(F"===================================正在测试：可见光照片分辨率设置测试============================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list = self.drivers.Yuntai_setting_002()
        try:
            assert "8000*6000" in text_list
            assert "5496*3672" in text_list
            assert "5472*3648 3:2" in text_list
            assert "5472*3078 16:9" in text_list
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_setting
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_setting_003(self, get_drivers):
        mylog.info(F"===================================正在测试：红外，分屏分辨率设置测试============================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list = self.drivers.Yuntai_setting_003()
        try:
            assert text_list[0] == "8000*6000"
            assert text_list[1] == "分辨率不可设置"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_setting
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_setting_004(self, get_drivers):
        mylog.info(F"===================================正在测试：可见光设置视频尺寸测试============================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list = self.drivers.Yuntai_setting_004()
        try:
            assert "3840*2160 30fps" in text_list
            assert "1920*1080 60fps" in text_list
            assert "1920*1080 30fps" in text_list
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_setting
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_setting_005(self, get_drivers):
        mylog.info(F"===================================正在测试：可见光，红外，分屏视频尺寸设置测试============================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list = self.drivers.Yuntai_setting_005()
        try:
            assert text_list[0] == "1920*1080 60fps"
            assert text_list[1] == "视频尺寸不可设置"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_setting
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_setting_006(self, get_drivers):
        mylog.info(F"===================================正在测试：红外增益模式测试============================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list = self.drivers.Yuntai_setting_006()
        try:
            assert text_list[0] == "低增益"
            assert text_list[1] == "高增益"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_setting
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_setting_007(self, get_drivers):
        mylog.info(F"===================================正在测试：云台转动速度设置===========================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list = self.drivers.Yuntai_setting_007()
        try:
            assert text_list[0] == "100"
            assert text_list[1] == "5"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e