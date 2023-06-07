import numpy as np
import time
import cv2
from matplotlib import pyplot as plt


def findeyes(path):
    face_cascade = cv2.CascadeClassifier('/Users/michealwang/MyCoding/pythonProject/Iris recognition/Classifier/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('/Users/michealwang/MyCoding/pythonProject/Iris recognition/Classifier/haarcascade_eye.xml')


    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度处理
    # 人脸识别
    face = face_cascade.detectMultiScale(gray, 2, 2)  # 参数：1、灰度图片， 2、缩放比例， 3、阈值
    print(face)
    print("这张图片中有%d张人脸" % len(face))
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)  # 绘制人脸方框

        face_gray = gray[y:y + h, x:x + w]  # 在人脸的基础上识别眼睛
        face_color = img[y:y + h, x:x + w]
        # 眼睛识别
        eyes = eye_cascade.detectMultiScale(face_gray)
        print("在这张脸上有%d个眼睛" % len(eyes))
        for (e_x, e_y, e_w, e_h) in eyes:
            cv2.rectangle(face_color, (e_x, e_y), (e_x + e_w, e_y + e_h), (0, 255, 0), 2)  # 绘制眼睛方框
            roi_color = face_color[e_y:e_y + e_h, e_x:e_x + e_w]  # 裁剪眼睛框图
            # getCircle(roi_color)
    plt.figure(figsize=(10, 10))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
    # cv2.imshow('dst', img)
    # cv2.waitKey(0)

def takephoto():

    # access the default camera
    cap = cv2.VideoCapture(0)

    cv2.waitKey(1)
    # capture a frame
    ret, frame = cap.read()


    # save the captured frame as a JPEG file
    cv2.imwrite('captured_image.jpg', frame)

    # release the camera
    cap.release()


if __name__ == "__main__":

    takephoto()
    path = 'useless/captured_image.jpg'
    findeyes(path)

