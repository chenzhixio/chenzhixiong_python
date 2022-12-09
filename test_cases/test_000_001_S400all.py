import re
import pytest
from common.loger_handler import mylog
from common.conf_handle import myconf
from page_element.page_001_S400all import test_s400all_test


class Test_Yuntai_setting(object):
    """S400全功能测试用例"""

    @pytest.mark.debug
    @pytest.mark.s400all
    def test_s400all_001(self, get_drivers):
        mylog.info(F"===================================正在测试：设备-云台连接测试============================")
        self.drivers = test_s400all_test(get_drivers)
        text_list = self.drivers.s400all_001()
        try:
            assert text_list[0] == myconf.get("Version", "PTZ_version") + " "
            assert text_list[1] == myconf.get("Version", "visible_light_version") + " "
            assert text_list[2] == myconf.get("Version", "PTZ_ARM_program_version")
            assert text_list[3] == myconf.get("Version", "PTZ_ARM_version")
            assert myconf.get("Version", "PTZ_SN") in text_list[4]
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.s400all
    def test_s400all_005(self, get_drivers):
        mylog.info(F"===================================正在测试：设备-云台连接测试============================")
        self.drivers = test_s400all_test(get_drivers)
        text = self.drivers.s400all_005()
        try:
            assert text == myconf.get("user", "guazai")
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.s400all
    def test_s400all_006(self, get_drivers):
        mylog.info(F"===================================正在测试：媒体库-图片,视频测试============================")
        self.drivers = test_s400all_test(get_drivers)
        text_list, distinguish_list, exists_list = self.drivers.s400all_006()
        try:
            assert text_list[0] == "00:00"
            assert text_list[1] != "00:00"
            assert int(text_list[2][-2:]) > int(text_list[1][-2:])
            assert int(text_list[3][-2:]) > int(text_list[2][-2:])
            assert text_list[4] == "00:00"
            assert exists_list[0] == True
            assert exists_list[1] == False
            assert exists_list[2] == False
            assert exists_list[3] == True
            assert exists_list[4] == False
            assert exists_list[5] == False
            assert distinguish_list[0] == "二维码识别成功"
            assert distinguish_list[1] == "二维码识别成功"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.s400all
    def test_s400all_010(self, get_drivers):
        mylog.info(F"===================================正在测试：我的-关于我们测试============================")
        self.drivers = test_s400all_test(get_drivers)
        text_list = self.drivers.s400all_010()
        try:
            assert myconf.get("Version", "app_version") in text_list[0]
            assert "400-040-0266" == text_list[1]
            assert 'sales@gdu-tech.com' == text_list[2]
            assert 'support@gdu-tech.com' == text_list[3]
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
            assert text_list.count("正常") >= 7
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.s400all
    def test_s400all_019(self, get_drivers):
        mylog.info(F"===========================正在测试：模式显示, 电量显示, 相机存储卡显示, 遥控器主从显示测试=================")
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







