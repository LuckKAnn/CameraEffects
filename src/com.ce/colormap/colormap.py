# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colormap.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(902, 773)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(".QLabel{\n"
" background-color: #000;\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: #acf6ef;\n"
"}"
)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 40, 200, 200))
        self.label.setStyleSheet(" width:220px;\n"
" height:220px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setScaledContents(True)
        self.label.setPixmap(QPixmap("color_img/AUTUMN.png"))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 40, 200, 200))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setScaledContents(True)
        self.label_2.setPixmap(QPixmap("color_img/BONE.png"))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 40, 200, 200))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.setScaledContents(True)
        self.label_3.setPixmap(QPixmap("color_img/HOT.png"))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 270, 200, 200))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.setScaledContents(True)
        self.label_4.setPixmap(QPixmap("color_img/JET.png"))
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 270, 200, 200))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_5.setScaledContents(True)
        self.label_5.setPixmap(QPixmap("color_img/OCEAN.png"))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(640, 270, 200, 200))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_6.setScaledContents(True)
        self.label_6.setPixmap(QPixmap("color_img/RAINBOW .png"))
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 500, 200, 200))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_7.setScaledContents(True)
        self.label_7.setPixmap(QPixmap("color_img/SPRING.png"))
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(390, 500, 200, 200))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_8.setScaledContents(True)
        self.label_8.setPixmap(QPixmap("color_img/SUMMER.png"))
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(640, 500, 200, 200))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_9.setScaledContents(True)
        self.label_9.setPixmap(QPixmap("color_img/WINTER.png"))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 210, 200, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 210, 200, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 210, 200, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 440, 200, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 440, 200, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 440, 200, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(120, 670, 200, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(390, 670, 200, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(640, 670, 200, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "秋色正浓"))
        self.pushButton_2.setText(_translate("MainWindow", "萧瑟"))
        self.pushButton_3.setText(_translate("MainWindow", "热情似火"))
        self.pushButton_4.setText(_translate("MainWindow", "色彩喷射"))
        self.pushButton_5.setText(_translate("MainWindow", "寒冷海洋"))
        self.pushButton_6.setText(_translate("MainWindow", "彩虹"))
        self.pushButton_7.setText(_translate("MainWindow", "春意盎然"))
        self.pushButton_8.setText(_translate("MainWindow", "夏季"))
        self.pushButton_9.setText(_translate("MainWindow", "冷若冬日"))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui .setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())