# Form implementation generated from reading ui file 'user_oldlogin2.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt6 import QtGui, QtCore, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from Database.testconnection import getDatabase
from test import preprocess_iris_image


class Ui_useroldLogin2(object):
    def __init__(self):
        super(Ui_useroldLogin2, self).__init__()
        self.timer = QTimer()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 70, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 160, 450, 100))
        self.label_3.setObjectName("label_3")
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 360, 231, 101))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
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

        self.timer.timeout.connect(self.showtime)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.label.setText(_translate("MainWindow", "欢迎您，xxx："))
        self.label_2.setText(_translate("MainWindow", "当前时间"))
        self.showtime()
        self.pushButton.setText(_translate("MainWindow", "登入/登出"))




    def showtime(self):
        self.timer.start(1000)
        self.time=QDateTime.currentDateTime()#获取当前时间
        self.timedisplay= self.time.toString("yyyy-MM-dd hh:mm:ss")#格式化一下时间
        self.label_3.setText(self.timedisplay)

    # 获取会员姓名
    def getad_Name(self, StudentID):
        self.studentID = StudentID
        self.user_name = self.Findad_Name(StudentID)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "欢迎您，" + self.user_name + "："))

    # 寻找会员姓名
    def Findad_Name(self, StudentID):
        db = getDatabase()
        cursor = db.cursor()
        sql = "select Name from user where StudentID = " + StudentID + ""
        cursor.execute(sql)
        result = cursor.fetchall()
        # 修改
        db.commit()
        # 关闭游标
        cursor.close()
        return result[0][0]

    # 更新user表的状态和time表
    def saveCheckInformation(self):

        db = getDatabase()
        cursor = db.cursor()
        sql = "select Status from user where StudentID = " + self.studentID + ""
        cursor.execute(sql)
        result = cursor.fetchall()

        if result[0][0] == '1':
            newStatus = '0'
        else:
            newStatus = '1'

        sql = "UPDATE user SET Status = "+repr(newStatus)+", LastTime = "+ repr(self.timedisplay) +" where StudentID = " + self.studentID + ""
        cursor.execute(sql)

        sql2 = "insert into Time(StudentID, Name, Time, InorOut) values("+repr(self.studentID)+","+repr(self.user_name)+","+repr(self.timedisplay)+","+repr(newStatus)+")"

        cursor.execute(sql2)
        # 修改
        db.commit()
        # 关闭游标
        cursor.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_useroldLogin2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
