import pytest
from common.loger_handler import mylog
from page_element.page_Yuntai_adjustment import test_Yuntai_adjustment


@pytest.mark.usefixtures('init_manual_flight')
class Test_Yuntai_adjustment(object):
    """云台俯仰调节"""

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
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
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_yuntai_002(self, get_drivers):
        mylog.info(F"===================================正在测试：任意角度回中============================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text1, text2 = self.drivers.Yuntai_adjustment_002()
        try:
            assert text1 == 0
            assert text2 == 0
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_yuntai_003(self, get_drivers):
        mylog.info(F"===================================正在测试：控制俯仰方位角测试===========================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list = self.drivers.Yuntai_adjustment_003()
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
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_yuntai_004(self, get_drivers):
        mylog.info(F"===================================正在测试：APP端可见光模式下，EV值调节测试===========================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list = self.drivers.Yuntai_adjustment_004()
        try:
            for text in text_list:
                assert text == True
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_yuntai_005(self, get_drivers):
        mylog.info(F"===================================正在测试：APP端可见光模式下，放大值调节测试===========================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list = self.drivers.Yuntai_adjustment_005()
        try:
            for text in text_list:
                assert text == True
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_yuntai_006(self, get_drivers):
        mylog.info(F"===================================正在测试：APP端红外模式下，放大值调节测试===========================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list = self.drivers.Yuntai_adjustment_006()
        try:
            for text in text_list:
                assert text == True
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_yuntai_007(self, get_drivers):
        mylog.info(F"===================================正在测试：APP端红外模式下，伪彩模式切换测试===========================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list = self.drivers.Yuntai_adjustment_007()
        try:
            for text in text_list:
                assert text == True
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_yuntai_008(self, get_drivers):
        mylog.info(F"===================================正在测试：APP检查到云台型号测试===========================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text = self.drivers.Yuntai_adjustment_008()
        try:
            assert text == "PDL"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    def test_yuntai_09(self, get_drivers):
        mylog.info(F"===================================正在测试：红外亮度0~16测试==============================")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list = self.drivers.Yuntai_adjustment_009()
        try:
            assert text_list[0] == '0'
            assert text_list[1] == '16'
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_yuntai
    def test_yuntai_010(self, get_drivers):
        mylog.info(F"===================================正在测试：红外对比度0~255测试==============")
        self.drivers = test_Yuntai_adjustment(get_drivers)
        text_list = self.drivers.Yuntai_adjustment_010()
        try:
            assert text_list[0] == '0'
            assert text_list[1] == '255'
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e