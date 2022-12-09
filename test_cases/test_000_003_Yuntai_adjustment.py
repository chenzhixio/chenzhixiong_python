import pytest
from common.loger_handler import mylog
from page_element.page_003_Yuntai_adjustment import test_Yuntai_adjustment


@pytest.mark.usefixtures('init_manual_flight')
class Test_Yuntai_adjustment(object):
    """云台俯仰调节"""

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    def test_yuntai_001(self, get_drivers):
        mylog.info(F"===================================正在测试：俯仰角极限角度测试===========================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text1, text2 = self.drivers.Yuntai_adjustment_001()
        try:
            assert text1 == -90
            assert text2 == 30
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    def test_yuntai_002(self, get_drivers):
        mylog.info(F"===================================正在测试：上下左右极限角度下视============================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list = self.drivers.Yuntai_adjustment_002()
        try:
            assert text_list[0] == -90
            assert text_list[1] == -90
            assert text_list[2] == -90
            assert text_list[3] == -90
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    def test_yuntai_003(self, get_drivers):
        mylog.info(F"===================================正在测试：上下左右极限角度回中============================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list = self.drivers.Yuntai_adjustment_003()
        try:
            assert text_list[0] == 0
            assert text_list[1] == 0
            assert text_list[2] == 0
            assert text_list[3] == 0
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    def test_yuntai_004(self, get_drivers):
        mylog.info(F"===================================正在测试：控制俯仰方位角测试===========================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list = self.drivers.Yuntai_adjustment_004()
        try:
            assert text_list[0] > 0
            assert text_list[1] < text_list[0]
            assert (text_list[2] - text_list[1]) == 1
            assert (text_list[2] - text_list[3]) == 1
            assert text_list[4] == -90
            assert text_list[5] == 0
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    def test_yuntai_005(self, get_drivers):
        mylog.info(F"===================================正在测试：可见光模式下，EV值调节测试===========================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list, distinguish_list = self.drivers.Yuntai_adjustment_005()
        try:
            for text in text_list:
                assert text == True
            for i in distinguish_list:
                assert i == "二维码识别成功"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    def test_yuntai_006(self, get_drivers):
        mylog.info(F"===================================正在测试：可见光模式下，放大值调节测试===========================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list, distinguish_list = self.drivers.Yuntai_adjustment_006()
        try:
            for text in text_list:
                assert text == True
            for i in distinguish_list:
                assert i != "照片存在漏拍"
            assert distinguish_list[0] == "二维码识别成功"
            assert distinguish_list[1] == "二维码识别成功"
            assert distinguish_list[-1] == "二维码识别成功"
            assert distinguish_list[-2] == "二维码识别成功"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    def test_yuntai_007(self, get_drivers):
        mylog.info(F"===================================正在测试：红外模式下，伪彩模式切换测试===========================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list, distinguish_list = self.drivers.Yuntai_adjustment_007()
        try:
            for text in text_list:
                assert text == True
            for i in distinguish_list:
                assert i != "照片存在漏拍"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    def test_yuntai_008(self, get_drivers):
        mylog.info(F"===================================正在测试：红外模式下，放大值调节测试===========================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list, distinguish_list = self.drivers.Yuntai_adjustment_008()
        try:
            for text in text_list:
                assert text == True
            for i in distinguish_list:
                assert i != "照片存在漏拍"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    def test_yuntai_009(self, get_drivers):
        mylog.info(F"===================================正在测试：红外亮度0~16测试==============================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list, photo_list = self.drivers.Yuntai_adjustment_009()
        try:
            assert text_list[0] == '0'
            assert text_list[1] == '16'
            assert photo_list[0] != "照片存在漏拍"
            assert photo_list[1] != "照片存在漏拍"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    def test_yuntai_010(self, get_drivers):
        mylog.info(F"===================================正在测试：红外对比度0~255测试==============")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list, photo_list = self.drivers.Yuntai_adjustment_010()
        try:
            assert text_list[0] == '0'
            assert text_list[1] == '255'
            assert photo_list[0] != "照片存在漏拍"
            assert photo_list[1] != "照片存在漏拍"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e