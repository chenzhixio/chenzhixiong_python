import os
import pytest
import shutil
from time import sleep
import uiautomator2 as u2
from common.conf_handle import myconf, Config
from page_element.page_init import InitStart


def del_files_win(path):
    """删除文件或文件夹"""
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)


@pytest.fixture(scope='session')
def get_drivers():
    """获取driver，初始化界面"""
    global driver, devices, apkname
    devices = myconf.get("user", "devices")
    apkname = myconf.get("user", "apkname")
    os.system(F"adb connect {devices}")
    del_files_win(Config.screenshot_path)
    os.mkdir(Config.screenshot_path)
    os.system(F"adb -s {devices} shell rm -rf /sdcard/gdu/flight2")
    os.system(f"adb -s {devices} shell pm clear {apkname}")
    driver = u2.connect(devices)
    driver.app_start(apkname, wait=True)
    I = InitStart(driver)
    I.init_start_operation()
    sleep(1)
    yield driver


@pytest.fixture(scope='class')
def init_manual_flight():
    """进入退出手动飞行"""
    I = InitStart(driver)
    I.open_manualflybtn()
    yield
    I.open_homepage()


@pytest.fixture(scope='class')
def init_rwfx():
    """任务飞行初始化操作"""
    I = InitStart(driver)
    I.open_taskflybtn()
    yield
    sleep(2)
    driver(resourceId="com.gdu.pro2:id/img_task_close").click()