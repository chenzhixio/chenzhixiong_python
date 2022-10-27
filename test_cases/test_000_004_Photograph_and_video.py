import pytest
from common.loger_handler import mylog
from page_element.page_Photograph_and_video import test_Photograph_and_video


@pytest.mark.usefixtures('init_manual_flight')
class Test_Photograph_and_video(object):
    """拍照录像功能"""

    # @pytest.mark.debug
    # @pytest.mark.debug_photo_video
    # def test_photo_video_01(self, get_drivers):
    #     mylog.info(F"===================================正在测试：可见光，红外，分屏模式分别录像==============================")
    #     self.drivers = test_Photograph_and_video(get_drivers)
    #     text_list = self.drivers.photo_video_01()
    #     try:
    #         assert text_list[0] == "视频录像，播放正常"
    #         assert text_list[1] == "视频录像，播放正常"
    #         assert text_list[2] == "视频录像，播放正常"
    #         mylog.info("测试通过")
    #     except AssertionError as e:
    #         mylog.info("测试不通过")
    #         raise e

    @pytest.mark.debug
    @pytest.mark.debug_photo_video
    def test_photo_video_02(self, get_drivers):
        mylog.info(F"===================================正在测试：可见光，红外，分屏模式分别拍照==============================")
        self.drivers = test_Photograph_and_video(get_drivers)
        text_list = self.drivers.photo_video_02()
        try:
            assert text_list[0] == "拍照成功，4张照片"
            assert text_list[1] == "拍照成功，4张照片"
            assert text_list[2] == "拍照成功，4张照片"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_photo_video
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_photo_video_03(self, get_drivers):
        mylog.info(F"===================================正在测试：拍照，录像，轮流使用==============================")
        self.drivers = test_Photograph_and_video(get_drivers)
        text_list = self.drivers.photo_video_03()
        try:
            assert text_list[0] == "视频"
            assert text_list[1] == "照片"
            assert text_list[2] == "视频"
            assert text_list[3] == "照片"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_photo_video
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_photo_video_04(self, get_drivers):
        mylog.info(F"===================================正在测试：拍照，录像模式切换==============================")
        self.drivers = test_Photograph_and_video(get_drivers)
        text_list = self.drivers.photo_video_04()
        try:
            assert text_list[0] == False
            assert text_list[1] == True
            assert text_list[2] == True
            assert text_list[3] == False
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_photo_video
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_photo_video_05(self, get_drivers):
        mylog.info(F"===================================正在测试：连续拍照20张==============================")
        self.drivers = test_Photograph_and_video(get_drivers)
        text_list = self.drivers.photo_video_05()
        try:
            assert text_list == True
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_photo_video
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_photo_video_06(self, get_drivers):
        mylog.info(F"===================================正在测试：FTP连接文件在线读取及下载测试==============================")
        self.drivers = test_Photograph_and_video(get_drivers)
        text = self.drivers.photo_video_06()
        try:
            assert text == 2
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_photo_video
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_photo_video_07(self, get_drivers):
        mylog.info(F"===================================正在测试：FTP连接SD卡储存容量测试==============================")
        self.drivers = test_Photograph_and_video(get_drivers)
        text = self.drivers.photo_video_07()
        try:
            assert text[:4] != '0.0G'
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_photo_video
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_photo_video_08(self, get_drivers):
        mylog.info(F"===================================正在测试：红外伪彩切换测试==============================")
        self.drivers = test_Photograph_and_video(get_drivers)
        text_list = self.drivers.photo_video_08()
        try:
            for i in text_list:
                assert i == "视频录制成功，拍照成功"
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_photo_video
    def test_photo_video_09(self, get_drivers):
        mylog.info(F"===================================正在测试：拍照，录像后在媒体中查看，播放，删除==============================")
        self.drivers = test_Photograph_and_video(get_drivers)
        text_list = self.drivers.photo_video_09()
        try:
            assert text_list[0] == "00:00"
            assert text_list[1] != text_list[0]
            assert int(text_list[2][-2:]) > int(text_list[1][-2:])
            assert int(text_list[3][-2:]) > int(text_list[2][-2:])
            assert text_list[4] == False
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e

    @pytest.mark.debug
    @pytest.mark.debug_photo_video
    @pytest.mark.flaky(reruns=2, reruns_delay=4)
    def test_photo_video_10(self, get_drivers):
        mylog.info(F"===================================正在测试：APP录像测试==============================")
        self.drivers = test_Photograph_and_video(get_drivers)
        text_list = self.drivers.photo_video_10()
        try:
            assert text_list[0] == "2秒录像失败"
            assert text_list[1] == "录像过程中切换拍照失败"
            assert text_list[2] == "录像过程中可以查看飞行设置"
            assert text_list[3] == "录像过程中可以设置云台"
            assert text_list[4] == -90
            assert text_list[5] == 0
            assert len(text_list[6]) == 1
            mylog.info("测试通过")
        except AssertionError as e:
            mylog.info("测试不通过")
            raise e