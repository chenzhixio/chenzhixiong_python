import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Config:
    dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    root_path = os.path.realpath(__file__)

    log_path = os.path.join(dir_path, "logs")

    datas_path = os.path.join(dir_path, "datas")

    screenshot_path = os.path.join(dir_path, "datas", "screenshot")

    data_ftp_path = os.path.join(dir_path, "datas", "ftpdown")

    ini_path = os.path.join(dir_path, "datas", "normal.ini")

    bugpng_path = os.path.join(dir_path, "datas", "bugpng")

    report_path = os.path.join(dir_path, "test_report")


if __name__ == "__main__":
    print(F"{Config.screenshot_path}\\stat")