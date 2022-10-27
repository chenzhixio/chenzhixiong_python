import pytest
from common.loger_handler import mylog
from page_element.page_Mission_flight import test_page_load_currency



@pytest.mark.usefixtures('init_rwfx')
class Test_load_currency_fxrw(object):
    """用例类型说明"""

    # @pytest.mark.debug
    # @pytest.mark.debug_rwfx
    # def test_rwfx_001(self, get_drivers):
    #     mylog.info(F"===================================正在测试：云台通用-三维飞行云台拍照测试==============================")
    #     self.drivers = test_page_load_currency(get_drivers)
    #     text_list = self.drivers.rwfx_001()
    #     try:
    #         assert int(text_list[0]) > int(text_list[1])
    #         # assert int(text_list[1]) == int(text_list[2])
    #         assert text_list[5].count(text_list[3]) > 10
    #         assert text_list[6].count(text_list[4]) > 10
    #         mylog.info("测试通过")
    #     except AssertionError as e:
    #         mylog.info("测试不通过")
    #         raise e
    #
    # @pytest.mark.debug
    # @pytest.mark.debug_rwfx
    # def test_rwfx_002(self, get_drivers):
    #     mylog.info(F"===================================正在测试：云台通用-二维飞行云台拍照测试==============================")
    #     self.drivers = test_page_load_currency(get_drivers)
    #     text_list = self.drivers.rwfx_002()
    #     try:
    #         assert int(text_list[0]) > int(text_list[1])
    #         # assert int(text_list[1]) == int(text_list[2])
    #         assert text_list[5].count(text_list[3]) > 5
    #         assert text_list[6].count(text_list[4]) > 5
    #         mylog.info("测试通过")
    #     except AssertionError as e:
    #         mylog.info("测试不通过")
    #         raise e
    #
    # @pytest.mark.debug
    # @pytest.mark.debug_rwfx
    # def test_rwfx_003(self, get_drivers):
    #     mylog.info(F"===================================正在测试：云台通用-一维航点飞行云台动作测试==============================")
    #     self.drivers = test_page_load_currency(get_drivers)
    #     text_list = self.drivers.rwfx_003()
    #     try:
    #         assert text_list[0] == 1
    #         assert text_list[1] == 1
    #         assert text_list[4].count(text_list[2]) > 5
    #         assert text_list[5].count(text_list[3]) > 5
    #         mylog.info("测试通过")
    #     except AssertionError as e:
    #         mylog.info("测试不通过")
    #         raise e

    @pytest.mark.debug
    @pytest.mark.debug_rwfx
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_rwfx_004(self, get_drivers):
        mylog.info(F"===================================正在测试：云台通用-任务飞行云台俯仰角测试==============================")
        self.drivers = test_page_load_currency(get_drivers)
        test_list = self.drivers.rwfx_004()
        try:
            assert test_list[0] == "-90°"
            assert test_list[1] == "-90°"
            assert test_list[2] == "10°"
            assert test_list[3] == "10°"
            assert test_list[4] == "10°"
            assert test_list[5] == "-90°"
            assert test_list[6] == "-90°"
            assert test_list[7] == "-90°"
            assert test_list[8] == "10°"
            assert test_list[9] == "-45°"
            assert test_list[10] == "-90°"
            assert test_list[11] == "10°"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e
