import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow

from mainUI import Ui_MainWindow
from administer_login1 import Ui_adLogin1
from QtUI.UI.designer.administer_login2 import Ui_adLogin2
from administer_login3 import Ui_adLogin3

from user_login1 import Ui_userLogin1

from user_firstlogin1 import Ui_userfirstLogin1
from user_firstlogin2 import Ui_userfirstLogin2

from user_oldlogin import Ui_useroldLogin
from user_oldlogin1 import Ui_useroldLogin1
from user_oldlogin2 import Ui_useroldLogin2

from user_register1 import Ui_UserRegister1
from user_register2 import Ui_UserRegister2
from user_register3 import Ui_UserRegister3
from administer_checkmember import Ui_adCheckMember1


# 创建main_window类继承my_main_window.py里面全部内容
# 最初始界面
class main_window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)


# 管理员登陆的第一个界面
class ad_login_window1(Ui_adLogin1, QMainWindow):
    def __init__(self):
        super(Ui_adLogin1, self).__init__()
        self.setupUi(self)


# 管理员登陆的第二个界面
class ad_login_window2(Ui_adLogin2, QMainWindow):
    def __init__(self):
        super(Ui_adLogin2, self).__init__()
        self.setupUi(self)


# 管理员登陆的第三个界面
class ad_login_window3(Ui_adLogin3, QMainWindow):
    def __init__(self):
        super(Ui_adLogin3, self).__init__()
        self.setupUi(self)


# 管理员查看当前人员的信息
class ad_checkmember_window1(Ui_adCheckMember1, QMainWindow):
    def __init__(self):
        super(Ui_adCheckMember1, self).__init__()
        self.setupUi(self)


# 用户登陆的第一个界面
class user_login_window1(Ui_userLogin1, QMainWindow):
    def __init__(self):
        super(Ui_userLogin1, self).__init__()
        self.setupUi(self)


# 用户首次登录登陆的第一个界面
class user_firstLogin_window1(Ui_userfirstLogin1, QMainWindow):
    def __init__(self):
        super(Ui_userfirstLogin1, self).__init__()
        self.setupUi(self)

# 用户首次登录登陆的第二个界面
class user_firstLogin_window2(Ui_userfirstLogin2, QMainWindow):
    def __init__(self):
        super(Ui_userfirstLogin2, self).__init__()
        self.setupUi(self)

# 用户非首次登陆
class user_oldlogin_window1(Ui_useroldLogin, QMainWindow):
    def __init__(self):
        super(Ui_useroldLogin, self).__init__()
        self.setupUi(self)

# 非首次登陆测试虹膜
class user_oldlogin1_window1(Ui_useroldLogin1, QMainWindow):
    def __init__(self):
        super(Ui_useroldLogin1, self).__init__()
        self.setupUi(self)

# 用户非首次登陆通过验证后
class user_oldlogin1_window2(Ui_useroldLogin2, QMainWindow):
    def __init__(self):
        super(Ui_useroldLogin2, self).__init__()
        self.timer = QTimer()
        self.setupUi(self)

# 用户注册的第一个界面
class user_register_window1(Ui_UserRegister1, QMainWindow):
    def __init__(self):
        super(Ui_UserRegister1, self).__init__()
        self.setupUi(self)


# 用户注册第二个界面
class user_register_window2(Ui_UserRegister2, QMainWindow):
    def __init__(self):
        super(Ui_UserRegister2, self).__init__()
        self.setupUi(self)


# 用户注册第三个界面
class user_register_window3(Ui_UserRegister3, QMainWindow):
    def __init__(self):
        super(Ui_UserRegister3, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 为main_window类和login_window类创建对象
    main_window = main_window()

    ad_login_window1 = ad_login_window1()
    ad_login_window2 = ad_login_window2()
    ad_login_window3 = ad_login_window3()
    ad_checkMember1_window = ad_checkmember_window1()

    user_firstlogin_window1 = user_firstLogin_window1()
    user_firstlogin_window2 = user_firstLogin_window2()

    user_oldlogin_window1 = user_oldlogin_window1()
    user_oldlogin1_window1 = user_oldlogin1_window1()
    user_oldlogin1_window2 = user_oldlogin1_window2()




    user_login_window1 = user_login_window1()

    user_register_window1 = user_register_window1()
    user_register_window2 = user_register_window2()
    user_register_window3 = user_register_window3()

    # 显示登陆窗口
    main_window.show()


    # 第一层
    # 当在主界面按下管理员登陆
    def main_pushButton():
        ad_login_window1.show()
        main_window.close()


    # 将显示main_window与单击登录页面按钮绑定
    main_window.pushButton.clicked.connect(main_pushButton)


    # 当在主界面按下用户登陆界面
    def main_pushButton2():
        user_login_window1.show()
        main_window.close()


    main_window.pushButton_2.clicked.connect(main_pushButton2)


    # 当在主界面按下用户注册按钮

    # 管理员登陆第一层
    # 当管理员按下登陆并且成功进入时
    def ad_loginwindow1_pushButton():
        ad_loginwindow1_warning1 = ad_login_window1.informationisNone()
        ad_loginwindow1_warning2 = ad_login_window1.notexistID()
        if ad_loginwindow1_warning2:
            ad_loginwindow1_warning3 = ad_login_window1.Correctpassword()
            if ad_loginwindow1_warning1 == True and ad_loginwindow1_warning2 == True and ad_loginwindow1_warning3 == True:
                ad_account = ad_login_window1.transferParameter()
                ad_login_window2.getadAccount(ad_account)
                ad_login_window2.UpdateInformation()
                ad_login_window2.show()
                ad_login_window1.close()
    ad_login_window1.pushButton.clicked.connect(ad_loginwindow1_pushButton)


    # 当在管理员登陆界面按下返回按钮时
    def ad_loginwindow1_pushButton_2():
        ad_login_window1.close()
        main_window.show()


    ad_login_window1.pushButton_2.clicked.connect(ad_loginwindow1_pushButton_2)


    # 管理员登陆第二层
    # 当管理员按下返回时
    def ad_loginwindow2_pushButton_3():
        ad_login_window2.close()
        ad_login_window1.show()


    ad_login_window2.pushButton_3.clicked.connect(ad_loginwindow2_pushButton_3)


    # 当管理员按下开始比对
    def ad_loginwindow2_pushButton_2():
        ad_login_window2_warning1, ad_name = ad_login_window2.contrast_image()
        if ad_login_window2_warning1:
            ad_login_window2.close()
            ad_login_window3.getad_Name(ad_name)
            ad_login_window3.show()


    ad_login_window2.pushButton_2.clicked.connect(ad_loginwindow2_pushButton_2)


    # 管理员登陆第三层
    # 当管理员按下辅助注册时
    def ad_loginwindow3_pushButton_1():
        ad_login_window3.close()
        user_register_window1.getad_account(ad_login_window3.getADaccount())
        user_register_window1.show()
    ad_login_window3.pushButton.clicked.connect(ad_loginwindow3_pushButton_1)


    # 当管理员按下查看并管理当前人员信息时
    def ad_loginwindow3_pushButton_2():
        ad_login_window3.close()
        ad_checkMember1_window.getad_account(ad_login_window3.getADaccount())
        ad_checkMember1_window.show()


    ad_login_window3.pushButton_2.clicked.connect(ad_loginwindow3_pushButton_2)


    # 管理员查看时按下返回
    def ad_checkMember1_window_pusshButton():
        ad_checkMember1_window.close()
        ad_login_window3.show()


    ad_checkMember1_window.pushButton.clicked.connect(ad_checkMember1_window_pusshButton)


    # 用户登陆第一层

    # 用户按下返回时
    def user_loginwindow1_pushButton():
        user_login_window1.close()
        main_window.show()


    user_login_window1.pushButton.clicked.connect(user_loginwindow1_pushButton)


    # 用户登录界面按下首次登录按钮
    def user_loginwindow1_pushButton_2():
        user_login_window1.close()
        user_firstlogin_window1.show()


    user_login_window1.pushButton_2.clicked.connect(user_loginwindow1_pushButton_2)

    # 用户非首次登陆
    def user_loginwindow1_pushButton_3():
        user_login_window1.close()
        user_oldlogin_window1.show()
    user_login_window1.pushButton_3.clicked.connect(user_loginwindow1_pushButton_3)


    # 用户非首次登陆按下返回
    def user_oldnwindow_pushButton_2():
        user_login_window1.show()
        user_oldlogin_window1.close()
    user_oldlogin_window1.pushButton_2.clicked.connect(user_oldnwindow_pushButton_2)


    # 用户按下登陆
    def user_oldnwindow_pushButton_1():
        user_oldnwindow_warning1 = user_oldlogin_window1.informationisNone()
        user_oldnwindow_warning2 = user_oldlogin_window1.notexistID()
        if user_oldnwindow_warning1:
            user_oldnwindow_warning3 = user_oldlogin_window1.Correctpassword()
            user_oldnwindow_warning4 = user_oldlogin_window1.ExistOrNotIris()
            if user_oldnwindow_warning1 == True and user_oldnwindow_warning2 == True and user_oldnwindow_warning3 == True and user_oldnwindow_warning4 == True:
                ad_account = user_oldlogin_window1.transferParameter()
                user_oldlogin1_window1.getAccount(ad_account)
                user_oldlogin1_window1.show()
                user_oldlogin_window1.close()
    user_oldlogin_window1.pushButton.clicked.connect(user_oldnwindow_pushButton_1)


    def user_oldnwindow1_pushButton_3():
        user_oldlogin1_window1.close()
        user_oldlogin_window1.show()


    user_oldlogin1_window1.pushButton_3.clicked.connect(user_oldnwindow1_pushButton_3)


    # 当用户按下开始比对
    def user_oldnwindow1_pushButton_2():
        user_oldlogin1_window1_warning1, ad_name = user_oldlogin1_window1.contrast_image()
        if user_oldlogin1_window1_warning1:
            user_oldlogin1_window1.close()
            user_oldlogin1_window2.getad_Name(ad_name)
            user_oldlogin1_window2.show()

    user_oldlogin1_window1.pushButton_2.clicked.connect(user_oldnwindow1_pushButton_2)

    # 当用户按下登入/登出
    def user_oldlogin1_window2_pushButton():
        user_oldlogin1_window2.saveCheckInformation()
        user_oldlogin1_window2.close()
        main_window.show()


    user_oldlogin1_window2.pushButton.clicked.connect(user_oldlogin1_window2_pushButton)


    # 用户首次登录

    # 验证账户和密码
    def user_firstloginwindow1_pushButton():
        user_firstlogin_window1_warning1 = user_firstlogin_window1.informationisNone()
        user_firstlogin_window1_warning2 = user_firstlogin_window1.notexistID()

        if user_firstlogin_window1_warning2:
            user_firstlogin_window1_warning3 = user_firstlogin_window1.Correctpassword()
            if user_firstlogin_window1.ExistOrNotIris():
                if user_firstlogin_window1_warning1 == True and user_firstlogin_window1_warning2 == True and user_firstlogin_window1_warning3 == True:
                    user_firstlogin_window1_warning4 = user_firstlogin_window1.updatePassword()
                    if user_firstlogin_window1_warning4 == True:
                        studentID = user_firstlogin_window1.transferParameter()
                        user_firstlogin_window2.getParameter(studentID)
                        user_firstlogin_window2.show()
                        user_firstlogin_window1.close()

    user_firstlogin_window1.pushButton.clicked.connect(user_firstloginwindow1_pushButton)

    # 返回按钮
    def user_firstloginwindow1_pushButton2():
        user_firstlogin_window1.close()
        user_login_window1.show()
    user_firstlogin_window1.pushButton_2.clicked.connect(user_firstloginwindow1_pushButton2)




    # 当用户按下完成注册
    def user_firstlogin_window2_pushButton2():
        if user_firstlogin_window2.enoughPhoto():
            user_firstlogin_window2.close()
            user_register_window3.show()


    user_firstlogin_window2.pushButton_2.clicked.connect(user_firstlogin_window2_pushButton2)


    # 当用户按下返回时
    def user_firstlogin_window2_pushButton3():
        user_firstlogin_window2.close()
        user_firstlogin_window1.show()


    user_firstlogin_window2.pushButton_3.clicked.connect(user_firstlogin_window2_pushButton3)




    # 用户注册第一层  (管理员辅助注册）
    # 用户注册按下返回按钮
    def user_registerwindow1_pushButton():
        user_register_window1.close()
        ad_login_window3.show()
    user_register_window1.pushButton.clicked.connect(user_registerwindow1_pushButton)


    # 用户填好基本信息之后
    def user_registerwindow1_pushButton2():
        user_registerwindow1_warning1 = user_register_window1.informationisNone()
        user_registerwindow1_warning2 = user_register_window1.IDandPhoneisNumber()
        user_registerwindow1_warning3 = user_register_window1.existID()
        user_registerwindow1_warning4 = user_register_window1.PhoneNumberLenth()
        if user_registerwindow1_warning1 == True and user_registerwindow1_warning2 == True and user_registerwindow1_warning3 == True and user_registerwindow1_warning4 == True:
            user_register_window1.saveInformation()
            user_register_window1.close()
            ad_login_window3.show()
    user_register_window1.pushButton_2.clicked.connect(user_registerwindow1_pushButton2)




    # 用户注册第三层
    # 按下确定时
    def user_register3_pushButton():
        user_register_window3.close()
        main_window.show()
    user_register_window3.pushButton.clicked.connect(user_register3_pushButton)

    # 关闭程序，释放资源
    sys.exit(app.exec())
