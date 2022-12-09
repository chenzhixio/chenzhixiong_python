import pytest
from common.loger_handler import mylog
from page_element.page_004_Photograph_and_video import test_Photograph_and_video


@pytest.mark.usefixtures('init_manual_flight')
class Test_Photograph_and_video(object):
    """拍照录像功能"""

    @pytest.mark.debug
    @pytest.mark.debug_photo_video
    def test_photo_video_01(self, get_drivers):
        mylog.info(F"===================================正在测试：可见光，红外，分屏模式分别录像20次==============================")
        self.drivers = test_Photograph_and_video(get_drivers)
        text_list = self.drivers.photo_video_01()
        try:
            assert text_list[0] == "拍照正常"
            assert text_list[1] == "识别失败"
            assert text_list[2] == "拍照正常"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_photo_video
    def test_photo_video_02(self, get_drivers):
        mylog.info(F"===================================正在测试：可见光，红外，分屏模式分别拍照20次==============================")
        self.drivers = test_Photograph_and_video(get_drivers)
        text_list = self.drivers.photo_video_02()
        try:
            assert text_list[0] == "拍照正常"
            assert text_list[1] == "识别失败"
            assert text_list[2] == "拍照正常"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_photo_video
    def test_photo_video_03(self, get_drivers):
        mylog.info(F"===================================正在测试：拍照，录像，轮流使用5次==============================")
        self.drivers = test_Photograph_and_video(get_drivers)
        text_list, distinguish_list = self.drivers.photo_video_03()
        try:
            for i in range(10):
                if i % 2 == 0:
                    assert text_list[0] == "视频"
                else:
                    assert text_list[1] == "照片"
            for i in distinguish_list:
                assert i == "二维码识别成功"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e