"""
 -----*--------------*-------
__author__ :  chenzhixiong
__time__ :  2022.11.11
-*- coding: utf-8 -*-
 -----*--------------*-------
"""
from ftplib import FTP
from common.conf_handle import myconf
from common.loger_handler import mylog

class LinkFTP:
    """
    连接 FTP 服务器
    """

    def __init__(self):

        host = myconf.get("sdcard", "host")
        port = int(myconf.get("sdcard", "port"))
        username = myconf.get("sdcard", "username")
        password = myconf.get("sdcard", "password")
        ftp_ = FTP()
        ftp_.connect(host, port)   # 连接
        ftp_.login(username, password)  # 登录
        mylog.info(f"{host} {port} {username} {password} 连接成功")
        self.ftp = ftp_
        self.buffer_size = 2048

    def download_file(self, remote_path: str, local_path: str) -> None:
        """
        从 ftp 下载文件
        :param remote_path: 远程服务器的目录绝对路径
        :param local_path:
        :return:
        """
        with open(local_path, 'wb') as fp:
            self.ftp.retrbinary('RETR ' + remote_path, fp.write, self.buffer_size)
            self.ftp.set_debuglevel(0)

    def upload_file(self, remote_path: str, local_path: str) -> None:
        """
        从本地上传文件到 ftp
        :param remote_path: 远程服务器的目录绝对路径
        :param local_path:
        :return:
        """
        with open(local_path, 'rb') as fp:
            self.ftp.storbinary('STOR ' + remote_path, fp, self.buffer_size)
            self.ftp.set_debuglevel(0)

    def path_list(self, path):
        """返回目录下所有文件名"""
        self.ftp.cwd(path)
        dri_list: list = self.ftp.nlst()
        dri_list.sort()
        return dri_list

    def delete_all_photo(self, path):
        text_list = self.path_list(path)
        for i in text_list:
            try:
                self.ftp.delete(F"{path}{i}")
            except Exception:
                pass


if __name__ == "__main__":
    P = LinkFTP()
    path = myconf.get("sdcard", "photo_path")
    video_list = P.path_list(path)
    print(F"==={len(video_list)}======{video_list}=========")

    # path = myconf.get("sdcard", "video_path")
    # video_list = P.path_list(path)
    # print(F"==={len(video_list)}======{video_list}=========")


