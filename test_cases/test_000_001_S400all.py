import re

import pytest
from common.loger_handler import mylog
from common.conf_handle import myconf
from page_element.page_S400all import test_s400all_test



class Test_Yuntai_setting(object):
    """S400全功能测试用例"""

    # @pytest.mark.debug
    # @pytest.mark.s400all
    # def test_s400all_005(self, get_drivers):
    #     mylog.info(F"===================================正在测试：设备-云台连接测试============================")
    #     self.drivers = test_s400all_test(get_drivers)
    #     text_list = self.drivers.s400all_005()
    #     try:
    #         assert text_list[0] == myconf.get("user", "guazai")
    #         assert text_list[1] == 0
    #         assert text_list[2] == -90
    #         mylog.info("测试通过")
    #     except AssertionError as e:
    #         mylog.info("测试不通过")
    #         raise e

    # @pytest.mark.debug
    # @pytest.mark.s400all
    # def test_s400all_006(self, get_drivers):
    #     mylog.info(F"===================================正在测试：媒体库-图片,视频测试============================")
    #     self.drivers = test_s400all_test(get_drivers)
    #     text_list = self.drivers.s400all_006()
    #     try:
    #         assert text_list[0] == "00:00"
    #         assert text_list[1] != text_list[0]
    #         assert int(text_list[2][-2:]) > int(text_list[1][-2:])
    #         assert int(text_list[3][-2:]) > int(text_list[2][-2:])
    #         assert text_list[4] == False
    #         mylog.info("测试通过")
    #     except AssertionError as e:
    #         mylog.info("测试不通过")
    #         raise e

    @pytest.mark.debug
    @pytest.mark.s400all
    def test_s400all_010(self, get_drivers):
        mylog.info(F"===================================正在测试：我的-关于我们测试============================")
        self.drivers = test_s400all_test(get_drivers)
        text_list = self.drivers.s400all_010()
        try:
            assert myconf.get("Version", "app_version") in text_list[0]
            assert "定制化的系统解决方案" in text_list[1]
            assert "400-040-0266" in text_list[2]
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.s400all
    def test_s400all_012(self, get_drivers):
        mylog.info(F"===================================正在测试：我的-设置测试============================")
        self.drivers = test_s400all_test(get_drivers)
        text_list = self.drivers.s400all_012()
        try:
            assert "0.0M" == text_list[0]
            assert myconf.get("Version", "app_version") in text_list[1]
            assert "GDU隐私政策" == text_list[2]
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.s400all
    def test_s400all_013(self, get_drivers):
        mylog.info(F"===================================正在测试：手动飞行按钮,任务飞行按钮测试============================")
        self.drivers = test_s400all_test(get_drivers)
        text_list = self.drivers.s400all_013()
        try:
            for i in text_list:
                assert i == True
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.s400all
    def test_s400all_015(self, get_drivers):
        mylog.info(F"===================================正在测试：健康管理系统测试============================")
        self.drivers = test_s400all_test(get_drivers)
        text, text_list = self.drivers.s400all_015()
        try:
            assert text == "S400已连接"
            for i in range(len(text_list)):
                if i == 4:
                    assert text_list[i] == "异常"
                else:
                    assert text_list[i] == "正常"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.s400all
    def test_s400all_019(self, get_drivers):
        mylog.info(F"===================================正在测试：模式显示, 电量显示, 相机存储卡显示, 遥控器主从显示测试============================")
        self.drivers = test_s400all_test(get_drivers)
        text_list = self.drivers.s400all_019()
        try:
            assert text_list[0] == "P档"
            assert int(re.findall(r"\d{1,3}", text_list[1])[0]) > 5
            assert int(re.findall(r"\d{1,3}", text_list[2])[0]) > 5
            assert text_list[3] == "已插卡"
            assert text_list[4] == "主遥控"
            assert text_list[5] == "P"
            assert int(re.findall(r"\d{1,3}", text_list[6])[0]) > 5
            assert int(re.findall(r"\d{1,3}", text_list[7])[0]) > 5
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e



