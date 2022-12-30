"""
 -----*--------------*-------
__author__ :  chenzhixiong
__time__ :  2022.11.11
-*- coding: utf-8 -*-
 -----*--------------*-------
"""
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image




def erweima_function(path):
    """二维码识别结果"""
    qrcode_image = cv.imread(path)
    qrCodeDetector = cv.QRCodeDetector()
    data, bbox, straight_qrcode = qrCodeDetector.detectAndDecode(qrcode_image)
    if data == "普宙武汉":
        text = F"二维码识别成功"
    else:
        text = "二维码识别失败"
    return text


def erweima_function2(path):
    """二维码识别结果"""
    qrcode_image = cv.imread(path)
    qrCodeDetector = cv.QRCodeDetector()
    data, bbox, straight_qrcode = qrCodeDetector.detectAndDecode(qrcode_image)
    return data


def screenshot_png(path):
    cat_img = Image.open(path)
    face_crop_img = cat_img.crop((550, 0, 1050, 400))
    face_crop_img.save(path)



if __name__ == "__main__":
    print(erweima_function(r"D:\test_python\Remote_control_test\datas\screenshot\test5.png"))


