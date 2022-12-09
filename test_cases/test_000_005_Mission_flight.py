import pytest
from common.loger_handler import mylog
from page_element.page_005_Mission_flight import test_page_load_currency


@pytest.mark.usefixtures('init_rwfx')
class Test_load_currency_fxrw(object):
    """用例类型说明"""

    @pytest.mark.debug
    @pytest.mark.debug_rwfx
    def test_rwfx_003(self, get_drivers):
        mylog.info(F"===================================正在测试：云台通用-航点飞行云台动作测试==============================")
        self.drivers = test_page_load_currency(get_drivers)
        text_list, number_list, list_height, list_massge = self.drivers.rwfx_003()
        try:
            assert int(number_list[0]) == int(number_list[2])
            assert int(number_list[1]) == int(number_list[3])
            assert int(number_list[0]) > int(number_list[1])
            assert list_height.count(int(text_list[0])) > 20
            assert list_massge.count("-90°") > 20
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_rwfx
    def test_rwfx_002(self, get_drivers):
        mylog.info(F"===================================正在测试：云台通用-二维飞行云台拍照测试==============================")
        self.drivers = test_page_load_currency(get_drivers)
        text_list, number_list, list_height, list_massge = self.drivers.rwfx_002()
        try:
            # assert int(number_list[0]) == int(number_list[2])
            # assert int(number_list[1]) == int(number_list[3])
            # assert int(number_list[0]) > int(number_list[1])
            assert list_height.count(int(text_list[0])) > 20
            assert list_massge.count("-90°") > 20
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_rwfx
    def test_rwfx_001(self, get_drivers):
        mylog.info(F"===================================正在测试：云台通用-三维飞行云台拍照测试==============================")
        self.drivers = test_page_load_currency(get_drivers)
        text_list, number_list, list_height, list_massge = self.drivers.rwfx_001()
        try:
            # assert int(number_list[0]) == int(number_list[2])
            # assert int(number_list[1]) == int(number_list[3])
            # assert int(number_list[0]) > int(number_list[1])
            assert list_height.count(int(text_list[0])) > 20
            assert list_massge.count(F"{text_list[1]}°") > 20
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e


