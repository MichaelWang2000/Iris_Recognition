# Form implementation generated from reading ui file 'user_login1.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import time

import cv2
# Form implementation generated from reading ui file 'user_login1.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from Database.testconnection import getDatabase
from util.innerCircle import innerCircle
from util.outerCircle import outerCircle
from util.visualization import displayCircle


class Ui_UserRegister2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        #self.pushButton.setGeometry(QtCore.QRect(630, 370, 121, 101))
        #self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 60, 571, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 410, 161, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 410, 161, 91))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 140, 291, 201))
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 0, 121, 111))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(630, 120, 121, 101))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(630, 240, 121, 101))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 添加按钮的信号槽
        self.pushButton_4.clicked.connect(self.start_camera)
        self.pushButton_5.clicked.connect(self.stop_camera)
        self.pushButton_6.clicked.connect(self.save_image)

        self.camera_active = False  # 标志位，表示摄像头是否正在运行

        self.photoNumber = 1
        self.parameter = None
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.pushButton.setText(_translate("MainWindow", "重拍"))
        self.label.setText(_translate("MainWindow", "请保证整个眼睛被摄像头准确捕捉"))
        self.label_2.setText(_translate("MainWindow", "虹膜识别"))
        self.pushButton_2.setText(_translate("MainWindow", "完成注册"))
        self.pushButton_3.setText(_translate("MainWindow", "返回"))
        self.label_3.setText(_translate("MainWindow", "图像"))
        self.pushButton_4.setText(_translate("MainWindow", "打开摄像头"))
        self.pushButton_5.setText(_translate("MainWindow", "关闭摄像头"))
        self.pushButton_6.setText(_translate("MainWindow", "拍摄"))

    def start_camera(self):
        if not self.camera_active:
            self.cap = cv2.VideoCapture(0)  # 打开默认摄像头，如果有多个摄像头可以使用相应的编号
            self.camera_active = True
            while self.camera_active:
                ret, frame = self.cap.read()  # 读取一帧画面
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.flip(frame, 1)
                try:
                    inner = innerCircle(frame)
                    outer_x, outer_y, outer_r = inner
                    inner_x, inner_y, inner_r = outerCircle(frame, inner)
                    frame_show = displayCircle(frame, outer_x, outer_y, outer_r, inner_x, inner_y, inner_r)
                except:
                    frame = frame
                else:
                    frame = frame_show
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 将BGR格式转换为RGB格式
                    # 裁剪中心区域
                    height, width, channels = frame.shape
                    max_dim = max(height, width)
                    scale = 300 / max_dim
                    frame = cv2.resize(frame, (int(width * scale), int(height * scale)))
                    img = QtGui.QImage(frame, frame.shape[1], frame.shape[0],
                                       QtGui.QImage.Format.Format_RGB888)  # 创建QImage对象
                    pix = QtGui.QPixmap.fromImage(img)  # 创建QPixmap对象
                    self.label_3.setPixmap(pix)  # 在label_3中显示画面
                    QtWidgets.QApplication.processEvents()  # 允许CPU处理其他任务
                    time.sleep(0.03)  # 延时30ms，相当于每秒更新30帧
                else:
                    break

            self.cap.release()  # 释放摄像头资源
            self.label_3.clear()  # 清除label中的内容

    def stop_camera(self):
        self.camera_active = False

    def save_image(self):
        QMessageBox = QtWidgets.QMessageBox()
        if self.camera_active:
            image_path = '/Users/michealwang/MyCoding/pythonProject/Iris recognition/photo/'+self.parameter+'/R/'+str(self.photoNumber)+'.jpg'
            self.save_path = '/Users/michealwang/MyCoding/pythonProject/Iris recognition/photo/'+self.parameter+'/R'
            if os.path.exists(self.save_path) != True:
                os.makedirs(self.save_path)
            ret, frame = self.cap.read()
            if ret:
                self.stop_camera()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 将BGR格式转换为RGB格式
                frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(image_path, frame_gray)
                # 裁剪中心区域
                height, width, channels = frame.shape
                max_dim = max(height, width)
                scale = 300 / max_dim
                frame = cv2.resize(frame, (int(width * scale), int(height * scale)))
                img = QtGui.QImage(frame, frame.shape[1], frame.shape[0],
                                   QtGui.QImage.Format.Format_RGB888)  # 创建QImage对象
                pix = QtGui.QPixmap.fromImage(img)  # 创建QPixmap对象
                self.captured_image = pix.toImage()  # 存储拍摄的图片
                self.label_3.setPixmap(pix)  # 在label_3中显示画面
                QtWidgets.QApplication.processEvents()  # 允许CPU处理其他任务
                QMessageBox.information(self.centralwidget, "Saved", "成功拍摄当前图片")
                if self.photoNumber == 1:
                    self.saveIrisInformation()
                self.photoNumber += 1
                _translate = QtCore.QCoreApplication.translate
                self.pushButton_6.setText(_translate("MainWindow", "继续拍"))
            else:
                QMessageBox.warning(self.centralwidget, "Error", "无法保存当前图片")
        else:
            QMessageBox.warning(self.centralwidget, "Error", "未打开摄像头")

    # 获取注册界面1中的学生学号
    def getParameter(self, parameter):
        self.parameter = parameter

    # 保存当前的虹膜图像地址
    def saveIrisInformation(self):
        db = getDatabase()
        cursor = db.cursor()
        sql = "UPDATE user SET IrisPhoto= '"+self.save_path+"' WHERE studentID ="+self.parameter+";"
        # print(sql)
        cursor.execute(sql)
        # 修改
        db.commit()
        # 关闭游标
        cursor.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_UserRegister2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
