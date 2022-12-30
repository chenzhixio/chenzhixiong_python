import os
import time
import pytest
import json
from flask import Flask, render_template, request, send_file
from common.conf_handle import myconf
from common.path_handler import Config
from common.loger_handler import mylog
from bs4 import BeautifulSoup
from common.noticed_handler import newnotice


app = Flask(__name__)
host = myconf.get("flask", "host")
port = int(myconf.get("flask", "port"))



def get_result(local_time):
    """读取通过率"""
    with open(F'{Config.report_path}\\test{local_time}.html', 'r+', encoding='utf8') as f:
        bs_xml = BeautifulSoup(f, features="html.parser")
        passed = bs_xml.findAll('span', {"class": "passed"})[0].contents[0].split(' ')[0]
        failed = bs_xml.findAll('span', {"class": "failed"})[0].contents[0].split(' ')[0]
        try:
            res = int(passed) / (int(passed) + int(failed))
        except Exception:
            return 0
        else:
            return res


@app.route('/runtest', methods=["GET", "POST"])
def runtest2():
    local_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    mylog.info(F'测试时间为{local_time}')
    download_api = F'http://{host}:{port}/download?name={local_time}'
    pytest.main(["-m", "debug", r"--html=test_report/test{}.html".format(local_time), "--self-contained-html",
                 "--capture=sys"])
    if float(get_result(local_time)) == 1.0:
        return {"code": "1", "msg": "测试成功", "report_url": download_api}
    else:
        text = {"code": "0", "msg": "测试失败", "report_url": download_api}
        newnotice(str(text))
        return text


@app.route('/download', methods=['GET', 'POST'])
def download():
    name = request.args.get('name')
    return send_file(F'{Config.report_path}/test{name}.html', as_attachment=True)


@app.route('/get_name', methods=['GET', 'POST'])
def get_report_namelist():
    text = os.listdir(Config.report_path)
    del text[0]
    locallist = []
    for filename in text:
        localtime = filename[4:-5]
        locallist.append(localtime)
        print(localtime)
    return {"code": "0", "msg": locallist}


if __name__ == '__main__':
    app.run(host=host, port=port, debug=False)

