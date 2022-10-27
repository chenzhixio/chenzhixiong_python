import os
import re
import pytest
from time import sleep
import uiautomator2 as u2
from common.loger_handler import mylog
from common.conf_handle import Config
from common.conf_handle import myconf



@pytest.fixture(scope='session')
def get_drivers():
    """获取driver，初始化界面"""
    global driver, devices, apkname
    devices = myconf.get("user", "devices")
    apkname = myconf.get("user", "apkname")
    os.system(F"adb connect {devices}")
    os.system(F"adb -s {devices} shell rm -rf /sdcard/gdu/flight2")
    os.system(f"adb -s {devices} shell pm clear {apkname}")
    driver = u2.connect(devices)
    driver.app_start(apkname, wait=True)
    sleep(2)
    driver.xpath("//*[contains(@text,'同意并继续')]").click()
    sleep(6)
    # 开启模拟环境
    for i in range(6):
        driver(resourceId="com.gdu.pro2:id/iv_appIcon").click()
    # sleep(4)
    # driver.xpath("//*[contains(@text,'取消')]").click()
    sleep(2)

    # 进入设置页面
    driver(resourceId="com.gdu.pro2:id/tv_taskFlyLabel").click()
    driver.xpath("//*[contains(@text,'航点飞行')]").click()
    driver(resourceId="com.gdu.pro2:id/iv_zorroRealcontrol_set").click()

    # 查看电量
    driver.xpath('//*[@resource-id="com.gdu.pro2:id/rv_left"]/android.view.ViewGroup[2]').click()
    sleep(2)
    text = driver(resourceId="com.gdu.pro2:id/tv_batteryPercent").get_text()
    soc = int(re.findall(r"\d{1,3}", text)[0])
    mylog.info(F"=====当前飞行器电量：{soc}")
    if soc <= int(myconf.get("stat", "soc")):
        os.mkdir(F"{Config.datas_path}\\stat")

    # 关闭返航避障
    driver.xpath('//*[@resource-id="com.gdu.pro2:id/rv_left"]/android.view.ViewGroup[6]').click()
    sleep(1)
    driver.swipe(1251, 1130, 1236, 150)
    sleep(3)
    fhbz = driver(resourceId="com.gdu.pro2:id/iv_goHomeObstacleSwitch")
    if fhbz.info.get('selected'):
        fhbz.click()
        sleep(2)

    # 开启模拟飞行
    driver.xpath('//*[@resource-id="com.gdu.pro2:id/rv_left"]/android.view.ViewGroup[1]').click()
    sleep(3)
    driver.swipe(1261, 950, 1248, 500)
    sleep(2)
    mnfx = driver(resourceId="com.gdu.pro2:id/iv_switch_simulate")
    if not mnfx.info.get('selected'):
        mnfx.click()
    sleep(2)
    driver.click(439, 212)

    # 返回首页
    driver(resourceId="com.gdu.pro2:id/iv_back").click()
    sleep(2)
    driver(resourceId="com.gdu.pro2:id/iv_taskFlyBackBtn").click()
    sleep(1)
    yield driver


@pytest.fixture(scope='class')
def init_manual_flight():
    """进入退出手动飞行"""
    sleep(2)
    driver(resourceId="com.gdu.pro2:id/iv_manualFlyBtn").click()
    sleep(2)
    driver(resourceId="com.gdu.pro2:id/iv_closeBtn").click()
    sleep(4)
    yield
    sleep(2)
    driver.click(599, 268)
    sleep(1)
    driver(resourceId="com.gdu.pro2:id/iv_zorroRealcontrol_back").click()
    sleep(2)


@pytest.fixture(scope='class')
def init_rwfx():
    """任务飞行初始化操作"""
    sleep(2)
    driver(resourceId="com.gdu.pro2:id/tv_taskFlyLabel").click()
    yield
    sleep(5)
    driver(resourceId="com.gdu.pro2:id/iv_taskFlyBackBtn").click()