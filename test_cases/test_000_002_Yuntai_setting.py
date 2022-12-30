import pytest
from common.loger_handler import mylog
from page_element.page_002_Yuntai_setting import test_Yuntai_setting


@pytest.mark.usefixtures('init_manual_flight')
class Test_Yuntai_setting(object):
    """云台俯仰调节"""

    @pytest.mark.debug
    @pytest.mark.debug_setting
    def test_setting_001(self, get_drivers):
        mylog.info(F"===================================正在测试：可见光设置视频尺寸设置============================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list, distinguish_list = self.drivers.Yuntai_setting_001()
        try:
            assert "3840*2160 30fps" == text_list[0]
            assert "1920*1080 60fps" == text_list[1]
            assert "1920*1080 30fps" == text_list[2]
            assert "3840*2160 30fps" == text_list[3]
            for i in distinguish_list:
                assert i == "二维码识别成功"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_setting
    def test_setting_002(self, get_drivers):
        mylog.info(F"===================================正在测试：可见光照片分辨率设置============================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list, distinguish_list = self.drivers.Yuntai_setting_002()
        try:
            assert "8000*6000" == text_list[0]
            assert "5496*3672" == text_list[1]
            assert "5472*3648 3:2" == text_list[2]
            assert "5472*3078 16:9" == text_list[3]
            assert "8000*6000" == text_list[4]
            for i in distinguish_list:
                assert i == "二维码识别成功"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_setting
    def test_setting_003(self, get_drivers):
        mylog.info(F"===================================正在测试：可见光抗闪烁设置============================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list, distinguish_list = self.drivers.Yuntai_setting_003()
        try:
            assert text_list[0] == "关闭"
            assert text_list[1] == "50Hz"
            assert text_list[2] == "60Hz"
            assert text_list[3] == "关闭"
            for i in distinguish_list:
                assert i == "二维码识别成功"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_setting
    def test_setting_004(self, get_drivers):
        mylog.info(F"===================================正在测试：红外增益模式设置============================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list = self.drivers.Yuntai_setting_004()
        try:
            assert text_list[0] == "低增益"
            assert text_list[1] == "高增益"
            assert text_list[2] != "照片存在漏拍"
            assert text_list[3] != "照片存在漏拍"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_setting
    def test_setting_005(self, get_drivers):
        mylog.info(F"===================================正在测试：分屏可见光视频尺寸设置============================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list, distinguish_list = self.drivers.Yuntai_setting_005()
        try:
            assert "3840*2160 30fps" == text_list[0]
            assert "1920*1080 60fps" == text_list[1]
            assert "1920*1080 30fps" == text_list[2]
            assert "3840*2160 30fps" == text_list[3]
            for i in distinguish_list:
                assert i == "二维码识别成功"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_setting
    def test_setting_006(self, get_drivers):
        mylog.info(F"===================================正在测试：分屏可见光照片分辨率设置============================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list, distinguish_list = self.drivers.Yuntai_setting_006()
        try:
            assert "8000*6000" == text_list[0]
            assert "5496*3672" == text_list[1]
            assert "5472*3648 3:2" == text_list[2]
            assert "5472*3078 16:9" == text_list[3]
            assert "8000*6000" == text_list[4]
            for i in distinguish_list:
                assert i == "二维码识别成功"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_setting
    def test_setting_007(self, get_drivers):
        mylog.info(F"===================================正在测试：分屏可见光抗闪烁设置============================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list, distinguish_list = self.drivers.Yuntai_setting_007()
        try:
            assert text_list[0] == "关闭"
            assert text_list[1] == "50Hz"
            assert text_list[2] == "60Hz"
            assert text_list[3] == "关闭"
            for i in distinguish_list:
                assert i == "二维码识别成功"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_setting
    def test_setting_008(self, get_drivers):
        mylog.info(F"===================================正在测试：云台转动速度设置===========================")
        self.drivers = test_Yuntai_setting(get_drivers)
        text_list = self.drivers.Yuntai_setting_008()
        try:
            assert text_list[0] == "5"
            assert text_list[1] == "100"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e