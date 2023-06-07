import re

import numpy
import numpy as np
import time
import cv2
import pylab
from matplotlib import pyplot as plt

from Database.testconnection import getDatabase

glasses = 0

def findeyes(path):
    import cv2

    # 选择加载无眼镜分类器或戴眼镜分类器

    eye_cascade = cv2.CascadeClassifier(
        '/Users/michealwang/MyCoding/pythonProject/Iris recognition/Classifier/haarcascade_eye.xml')

    if glasses == '1':
        eye_cascade = cv2.CascadeClassifier(
            '/Users/michealwang/MyCoding/pythonProject/Iris recognition/Classifier/haarcascade_eye_tree_eyeglasses.xml')

    # 读取图像
    img = cv2.imread(path)

    # 将图像转换为灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 检测眼睛
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # 获取眼睛的左右位置
    for (x, y, w, h) in eyes:
        # 确定眼睛的中心点
        center = (x + w // 2, y + h // 2)
        # 根据中心点将眼睛分为左右两半
        if center[0] < img.shape[1] / 2:  # 眼睛在图像的左边
            eye_region = img[y:y + h, x:x + w]
            cv2.imwrite('left_eye.jpg', eye_region)
        else:  # 眼睛在图像的右边
            eye_region = img[y:y + h, x:x + w]
            cv2.imwrite('right_eye.jpg', eye_region)

def takephoto():

    # 开启默认摄像头
    cap = cv2.VideoCapture(0)

    # 增加停止时间
    cv2.waitKey(1)
    # capture a frame
    ret, frame = cap.read()


    print(type(frame))
    # 将捕获的帧另存为JPG文件
    cv2.imwrite('captured_image.jpg', frame)

    # 关闭摄像头
    cap.release()


import cv2
import matplotlib.pyplot as plt
from util.innerCircle import innerCircle
from util.outerCircle import outerCircle
from util.visualization import displayCircle
from datetime import datetime

def preprocess_iris_image(image_path):

    # 确定好瞳孔的内外圆的位置，并将其标注出来，方便之后进行处理
    img = cv2.imread(image_path, 0)
    inner = innerCircle(img)
    outer = outerCircle(img, inner)
    cimg = displayCircle(img, outer[0], outer[1], outer[2], inner[0], inner[1], inner[2])
    plt.imshow(cimg)


    # 调节为40*512的矩形图片
    from util.normalize import normalize

    # 成比例调节
    height = 40
    width = 512

    img = cv2.imread(image_path, 0)
    polar_array, polar_noise = normalize(img, outer[0], outer[1], outer[2], inner[0], inner[1], inner[2], height, width)
    plt.imshow(polar_array, cmap='gray')

    from util.feature import getFeatureMap

    feature = getFeatureMap(cv2.imread(image_path, 0), 'swt')
    plt.imshow(feature, cmap='gray')


    from util.contrast import contrast

    test_img = cv2.imread(image_path, 0)
    name, side, scores = contrast(test_img)
    # print(name)
   # print(side)
    # print(scores)
    return name


def generate():
    from util.feature import generateFeatureDataset
    dp = r'/Users/michealwang/MyCoding/pythonProject/Iris recognition/photo'
    fdp = r'/Users/michealwang/MyCoding/pythonProject/Iris recognition/feature'

    generateFeatureDataset(feature_dataset_path=fdp, dataset_path=dp, mode='swt')
    print('已完成')
    return True

if __name__ == "__main__":

    # takephoto()
    path = '/Users/michealwang/MyCoding/pythonProject/Iris recognition/QtUI/UI/designer/captured_image.jpg'

    # print("请问您是否佩戴眼镜? 有请输入1，无请输入0")
    # glasses = input()

    # 找到眼睛的位置并进行保存
    # findeyes(path)
    generate()
    # preprocess_iris_image(path)

    # print(datetime.now())

