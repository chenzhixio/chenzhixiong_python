import os
import re
import xlsxwriter
import shutil
from bs4 import BeautifulSoup
from common.path_handler import Config


def del_files_win(path):
    """删除文件或文件夹"""
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)


def get_stat_time():
    """获取第一条报告年月日"""
    report_list = os.listdir(Config.report_path)
    text = report_list[1][4:14]
    return text


def get_result(path):
    """获取报告关键字"""
    with open(path, 'r+', encoding='utf8') as f:
        filename = os.path.split(path)[1]
        stattime = os.path.splitext(filename)[0][4:]
        bs_xml = BeautifulSoup(f, features="html.parser")
        passed = bs_xml.findAll('span', {"class": "passed"})[0].contents[0].split(' ')[0]
        failed = bs_xml.findAll('span', {"class": "failed"})[0].contents[0].split(' ')[0]
        try:
            errors = bs_xml.findAll('span', {"class": "error"})[0].contents[0].split(' ')[0]
        except Exception:
            errors = "0"
        failedname = ""
        for i in range(int(failed)+int(errors)):
            text = bs_xml.findAll('td', {"class": "col-name"})[i].contents[0]
            text2 = re.findall(r":test_.*\d{1,3}", text)[0][1:]
            failedname = failedname + text2 + ","
        text_json = {"执行时间": stattime, "通过条数": passed, "失败条数": int(failed)+int(errors), "失败编号": failedname[:-1]}
        return text_json


def get_repot_exsl_data(report_path):
    """获取所有报告的结果"""
    report_list = os.listdir(report_path)
    del report_list[0]
    list_json = []
    for name in report_list:
        path = F"{Config.report_path}\\{name}"
        text_json = get_result(path)
        list_json.append(text_json)
    return list_json


def generate_exsl(stattime, list_json, svn_path):
    """将测试报告记录生成xls文件"""
    path = F"{svn_path}\\{stattime}测试记录.xls"
    xl = xlsxwriter.Workbook(path)          # 实例化
    sheet1 = xl.add_worksheet("测试结果")    # 第1 sheet 页

    # 设置表头宽度
    sheet_list = [['A:B', 20], ['B:C', 10], ['C:D', 10], ['D:E', 80]]
    for width in sheet_list:
        sheet1.set_column(width[0], width[1])

    # 设置表头名称
    sheet1_name_list = ["执行时间", "通过条数", "失败条数", "失败编号"]
    for header_name in range(len(sheet1_name_list)):
        sheet1.write_string(0, header_name, sheet1_name_list[header_name])

    # # 将数据按 I行 N列 写入表格
    for i in range(len(list_json)):
        jsontext = list_json[i]
        for n in range(len(jsontext)):
            sheet1.write_string(i + 1, n, str(jsontext[sheet1_name_list[n]]))
    xl.close()


def report_up_svn(svn_path):
    """报告剪切到svn"""
    report_list = os.listdir(Config.report_path)
    del report_list[0]
    for i in report_list:
        shutil.copyfile(F"{Config.report_path}\\{i}", F"{svn_path}\\{i}")


def day_total():
    stattime = get_stat_time()
    svn_path = F"D:\\工作\\1、无人机项目\\S400无人机\\6、自动化测试记录\\{stattime}_双光"
    del_files_win(svn_path)                                 # 删除重复文件
    os.mkdir(svn_path)                                      # SVN创建文件夹
    report_up_svn(svn_path)                                 # 报告上传SVN
    list_json = get_repot_exsl_data(Config.report_path)     # 获取当天全部报告数据
    generate_exsl(stattime, list_json, svn_path)            # 报告数据生成表格


if __name__ == '__main__':
    day_total()