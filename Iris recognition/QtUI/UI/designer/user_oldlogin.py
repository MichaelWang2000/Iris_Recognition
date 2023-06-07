import re

from PyQt6 import QtCore, QtGui, QtWidgets
from Database.testconnection import getDatabase

class Ui_useroldLogin(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(544, 440)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 320, 121, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 320, 121, 61))
        self.pushButton_2.setObjectName("pushButton_2")

        self.textEdit = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit.setGeometry(QtCore.QRect(210, 80, 231, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(210, 170, 231, 51))

        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(70, 80, 58, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 180, 58, 41))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 250, 58, 41))
        self.label_3.setObjectName("label_2")

        self.textEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "登陆"))
        self.pushButton_2.setText(_translate("Dialog", "返回"))
        self.label.setText(_translate("Dialog", "学号"))
        self.label_2.setText(_translate("Dialog", "密码"))


    # 信息填写不完整时的弹窗提示
    def incompleteInformation(self):
        box = QtWidgets.QMessageBox()
        box.warning(self, "提示", "你的信息填写不完整，请填写完再进行下一步")

    #  判断信息是否填写完整
    def informationisNone(self):
        if (self.textEdit.toPlainText() == "" or self.textEdit_2.text() == "" ):
                self.incompleteInformation()
        else:
            return True

    # 当没有当前会员账户时
    def notExistID(self):
        box = QtWidgets.QMessageBox()
        box.warning(self, "提示", "当前学号未在管理员处注册")

    # 判断是否存在当前会员账号
    def notexistID(self):
        db = getDatabase()
        cursor = db.cursor()
        sql = "select * from user where StudentID = "+repr(self.textEdit.toPlainText())+""
        cursor.execute(sql)
        result = cursor.fetchall()
        # 修改
        db.commit()
        # 关闭游标
        cursor.close()
        if result == ():
            self.notExistID()
            return False
        else:
            return True

    # 当没有当前管理员账户时
    def wrongPassword(self):
        box = QtWidgets.QMessageBox()
        box.warning(self, "提示", "密码错误")

    # 判断当前账号的密码是否正确
    def Correctpassword(self):
        db = getDatabase()
        cursor = db.cursor()
        sql = "select Password from user where StudentID = " + repr(self.textEdit.toPlainText()) + ""
        cursor.execute(sql)
        result = cursor.fetchall()
        # 修改
        db.commit()
        # 关闭游标
        cursor.close()
        if self.textEdit_2.text() == result[0][0]:
            return True
        else:
            self.wrongPassword()
            return False

    # 给会员注册第二界面传递参数
    def transferParameter(self):
        return self.textEdit.toPlainText()

    #  不是第一次注册弹窗
    def ExistIris(self):
        box = QtWidgets.QMessageBox()
        box.warning(self, "提示", "请先完成首次注册")

    #  测试是否为第一次注册
    def ExistOrNotIris(self):
        db = getDatabase()
        cursor = db.cursor()
        sql = "select IrisPhoto from user where StudentID = " + repr(self.textEdit.toPlainText()) + ""
        cursor.execute(sql)
        result = cursor.fetchall()
        # 修改
        db.commit()
        # 关闭游标
        cursor.close()
        if result[0][0] != None:
            return True
        else:
            self.ExistIris()
            return False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_useroldLogin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())