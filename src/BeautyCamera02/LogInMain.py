"""
    登录主功能类
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QMessageBox

import about
from ImageMain import ImageMain
from LogInUi import LogInUi
from LogUpMain import LogUpMain
from LogUpUi import LogUpUi
import pymysql
import  logup


class LoginInMain(QMainWindow):
    # 处理切换屏幕信号
    signal_LogIn = pyqtSignal()
    signal_LogUp = pyqtSignal()

    def __init__(self):
        super(LoginInMain, self).__init__()
        self.ui =LogInUi()
        self.ui.setupUi(self)
        self.action_connect()
        # self.writeUser()
        self.getLocalUser()

    def writeUser(self,userName,password):
        file = "./user.txt"
        userFile = open(file, mode="w+")
        # userName = 'lkk'
        userFile.write(userName+"\n")
        # password = "123456"
        userFile.write(password)


    # 获取保存在本地的用户信息
    def getLocalUser(self):
        file = "./user.txt"
        userFile = open(file,mode="r")
        self.ui.lineEdit.setText(userFile.readline().strip().replace("\n",""))
        self.ui.lineEdit_2.setText(userFile.readline())



    def action_connect(self):
        # 绑定切屏事件
        self.signal_LogIn.connect(self.LogInSuccess)
        #绑定切屏事件的点击事件
        self.ui.pushButton_2.clicked.connect(self.LogIn)
        self.ui.pushButton.clicked.connect(self.LogUp)
        #绑定功能未注册不能使用
        self.ui.action.triggered.connect(self.canNotUse)
        self.ui.action_2.triggered.connect(self.canNotUse)
        self.ui.action_17.triggered.connect(self.canNotUse)
        self.ui.action_18.triggered.connect(self.canNotUse)
        self.ui.actionAI.triggered.connect(self.canNotUse)
        # 关于我们
        self.ui.action_5.triggered.connect(self.aboutUs)

    def aboutUs(self):
        try:
            Dialog = QtWidgets.QMainWindow()
            self.dialog = Dialog
            self.ui_5 = about.Ui_MainWindow()
            self.ui_5.setupUi(Dialog)
            Dialog.show()
        except Exception as e:
            print(e)

    def canNotUse(self):
        QMessageBox().information(self, "提示", "请先登录!", QMessageBox.Yes)
        return 0

    def out_signal_LogIn(self):
        self.signal_LogIn.emit()

    def out_signal_LogUp(self):
        self.signal_LogUp.emit()

    def LogIn(self):
        # 先校验输入
        try:
            self.userName = self.ui.lineEdit.text()
            self.password  = self.ui.lineEdit_2.text()
            if self.userName=="" or  self.password  =="":
                QMessageBox().information(self, "提示", "用户名或密码错误!", QMessageBox.Yes)
                return 0
            rightPassword = self.selectUser(self.userName)
            if(rightPassword == self.password):
                if (self.ui.radioButton.isChecked()):
                    self.writeUser(self.userName, self.password)
                self.signal_LogIn.emit()
            else:
                QMessageBox().information(self, "提示", "用户名或密码错误!", QMessageBox.Yes)
                return  0
        except Exception as e:
            print(e)

    def LogInSuccess(self):
        self.hide()
        self.t = ImageMain()
        self.t.show()

    def LogUp(self):
        try:
            # self.hide()
            self.Dialog = QtWidgets.QMainWindow()
            # self.dialog = self.Dialog
            self.ui_3 = LogUpUi()
            self.ui_3.setupUi(self.Dialog)
            # self.ui_3.signal_close.connect(self.show)
            self.Dialog.show()
            self.logUpConnect()
            # self.Dialog.exec_()
            # print("已经关闭")
        except Exception as e:
            print(e)


    def logUpConnect(self):
        # 绑定功能未注册不能使用
        self.ui_3.pushButton.clicked.connect(self.clear)
        self.ui_3.pushButton_2.clicked.connect(self.validation)
        self.ui_3.action.triggered.connect(self.canNotUse)
        self.ui_3.action_2.triggered.connect(self.canNotUse)
        self.ui_3.action_17.triggered.connect(self.canNotUse)
        self.ui_3.action_18.triggered.connect(self.canNotUse)
        self.ui_3.actionAI.triggered.connect(self.canNotUse)
        # 关于我们
        self.ui_3.action_5.triggered.connect(self.aboutUs)

    def clear(self):
        self.ui_3.lineEdit.clear()
        self.ui_3.lineEdit_2.clear()
        self.ui_3.lineEdit_3.clear()
        self.ui_3.lineEdit_4.clear()
        self.ui_3.textEdit.clear()

    def validation(self):
        # 先校验输入
        try:
            self.userName = self.ui_3.lineEdit.text()
            self.password = self.ui_3.lineEdit_2.text()
            self.passwordAgain = self.ui_3.lineEdit_3.text()
            self.phone = self.ui_3.lineEdit_4.text()
            self.secretCode = self.ui_3.textEdit.toPlainText()
            self.ilegal = False
            ilegal = ['%','^','&','(',')','!','@','#']
            # 逐个校验
            for i in range(len(ilegal)):
                if ilegal[i] in self.userName:
                    self.ilegal = True
                    print("yes")
                    break

            if(len(self.userName)>=2 and len(self.userName)<=10):
                self.userFlag = True
                self.ui_3.label_9.setText("")
            else:
                self.userFlag = False
                self.ui_3.label_9.setText("用户名须为2-10位")
                self.ui_3.label_9.setStyleSheet("color: red;")

            if self.userFlag  and self.selectUser(self.userName)!=0:
                print()
                self.userFlag = False
                self.ui_3.label_9.setText("用户名已经存在")
                self.ui_3.label_9.setStyleSheet("color: red;")
            else:
                self.userFlag = True
                self.ui_3.label_9.setText("")

            if self.ilegal:
                self.userFlag = False
                self.ui_3.label_9.setText("用户名含有非法字符")
                self.ui_3.label_9.setStyleSheet("color: red;")
            else:
                self.userFlag = True
                print("enen")
                self.ui_3.label_9.setText("")


            # 验证密码
            if (len(self.password) >= 3 and len(self.password) <= 10):
                self.pwdFlag = True
                self.ui_3.label_10.setText("")
            else:
                self.pwdFlag = False
                self.ui_3.label_10.setText("密码至少有3位,最长为10位")
                self.ui_3.label_10.setStyleSheet("color: red;")

            # 验证再次输入密码
            if self.password == self.passwordAgain and self.passwordAgain!="":
                self.pwdAgainFlag = True
                self.ui_3.label_11.setText("")
            else:
                self.pwdAgainFlag = False
                self.ui_3.label_11.setText("两次输入的密码不同")
                self.ui_3.label_11.setStyleSheet("color: red;")
            # 验证电话
            if len(self.phone)==11:
                self.phoneFlag =True
                self.ui_3.label_12.setText("")
            else:
                self.phoneFlag = False
                self.ui_3.label_12.setText("电话长度应该为11位")
                self.ui_3.label_12.setStyleSheet("color: red;")

            # 验证注册码
            if self.secretCode =="LKKCJ":
                self.secretFlag = True
                self.ui_3.label_13.setText("")
            else:
                self.secretFlag = False
                self.ui_3.label_13.setText("注册码不正确，请联系管理员获取注册码")
                self.ui_3.label_13.setStyleSheet("color: red;")


            if self.userFlag and self.secretFlag and self.pwdFlag and self.pwdAgainFlag and self.phoneFlag:
                # print("成功")
                self.insertUser(self.userName,self.password,self.phone)

                QMessageBox().information(self, "提示", "注册成功!", QMessageBox.Yes)

                self.Dialog.close()
                self.show()
            else:
                QMessageBox().information(self, "提示", "注册失败，请检查填入内容!", QMessageBox.Yes)
                self.Dialog.show()
                return 0
        except Exception as e:
            print(e)


    # 查询user
    def selectUser(self,username):
        # 连接database
        conn = pymysql.connect(host="localhost", user="root", password="076523", database="cameraeffects")
        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()
        # 查询密码拼串
        sql = "select password from user where username = '" + username+"'"
        print(sql)
        password = 0
        try:
            cursor.execute(sql)  # 执行sql语句

            results = cursor.fetchall()  # 获取查询的所有记录
            print("name", "password", "phone")
            # 遍历结果
            for row in results:
                password = row[0]

            # print(password)
        except Exception as e:
            raise e
        finally:
            conn.close()  # 关闭连接
            return password

    # 插入新用户
    def insertUser(self,username,password,phone):
        # 连接database
        conn = pymysql.connect(host="localhost", user="root", password="076523", database="cameraeffects")
        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()
        # 查询密码拼串
        sql = "insert into user (username,password,phone) values ('" + username + "','" + password + "','" + phone + "')"
        print(sql)
        try:
            cursor.execute(sql)  # 执行sql语句
            conn.commit()
        except Exception as e:
            raise e
        finally:
            conn.close()  # 关闭连接


