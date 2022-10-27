import pytest
import os
import shutil
import time
import requests
from common.path_handler import Config
from common.loger_handler import mylog


def del_files_win(path):
    """删除文件或文件夹"""
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)


def run(keys):
    """启动pytest"""
    local_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    pytest.main(["-m", keys,
                 r"--html=test_report/test{}.html".format(local_time),
                 "--self-contained-html",
                 "--capture=sys"])


def run_ci():
    """接口CI启动服务"""
    res = requests.get("http://127.0.0.1:5566/runtest")
    mylog.info(F"===={res}====")


if __name__ == '__main__':
    path = F"{Config.datas_path}\\stat"
    del_files_win(path)
    for i in range(1):
        if os.path.exists(path):
            break
        else:
            run("s400all")
            # run_ci()