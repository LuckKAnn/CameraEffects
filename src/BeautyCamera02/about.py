# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(537, 252)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/kunkun/.designer/backup/cam.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStatusTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 230);\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 371, 51))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 40, 369, 59))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 140, 221, 31))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setPriority(QtWidgets.QAction.HighPriority)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setWhatsThis("")
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.actionLaplacian = QtWidgets.QAction(MainWindow)
        self.actionLaplacian.setObjectName("actionLaplacian")
        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionPrewitt = QtWidgets.QAction(MainWindow)
        self.actionPrewitt.setObjectName("actionPrewitt")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.action_11 = QtWidgets.QAction(MainWindow)
        self.action_11.setObjectName("action_11")
        self.action_12 = QtWidgets.QAction(MainWindow)
        self.action_12.setObjectName("action_12")
        self.action_13 = QtWidgets.QAction(MainWindow)
        self.action_13.setObjectName("action_13")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_8.setObjectName("action_8")
        self.action_14 = QtWidgets.QAction(MainWindow)
        self.action_14.setIconVisibleInMenu(True)
        self.action_14.setObjectName("action_14")
        self.action_15 = QtWidgets.QAction(MainWindow)
        self.action_15.setObjectName("action_15")
        self.action_16 = QtWidgets.QAction(MainWindow)
        self.action_16.setObjectName("action_16")
        self.actionwo = QtWidgets.QAction(MainWindow)
        self.actionwo.setObjectName("actionwo")
        self.actionGamma = QtWidgets.QAction(MainWindow)
        self.actionGamma.setObjectName("actionGamma")
        self.actionAI = QtWidgets.QAction(MainWindow)
        self.actionAI.setObjectName("actionAI")
        self.action_17 = QtWidgets.QAction(MainWindow)
        self.action_17.setObjectName("action_17")
        self.action_18 = QtWidgets.QAction(MainWindow)
        self.action_18.setObjectName("action_18")
        self.action_19 = QtWidgets.QAction(MainWindow)
        self.action_19.setObjectName("action_19")
        self.action_20 = QtWidgets.QAction(MainWindow)
        self.action_20.setObjectName("action_20")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "美颜相机"))
        self.label_2.setText(_translate("MainWindow", "联系方式: 1546165200@qq.com"))
        self.label.setText(_translate("MainWindow", "作者:   LKK & CJ"))
        self.label_3.setText(_translate("MainWindow", "版本信息: 1.0"))
        self.action.setText(_translate("MainWindow", "保存"))
        self.action.setStatusTip(_translate("MainWindow", "打开图片"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_2.setText(_translate("MainWindow", "另存为"))
        self.action_2.setStatusTip(_translate("MainWindow", "保存图片"))
        self.action_2.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_3.setText(_translate("MainWindow", "高斯滤波"))
        self.action_4.setText(_translate("MainWindow", "图像清晰"))
        self.action_4.setStatusTip(_translate("MainWindow", "图像清晰"))
        self.action_6.setText(_translate("MainWindow", "高斯滤波"))
        self.action_6.setStatusTip(_translate("MainWindow", "高斯滤波"))
        self.action_7.setText(_translate("MainWindow", "均值滤波"))
        self.action_7.setStatusTip(_translate("MainWindow", "均值滤波"))
        self.actionLaplacian.setText(_translate("MainWindow", "Laplacian"))
        self.actionLaplacian.setStatusTip(_translate("MainWindow", "Laplacian"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionSobel.setStatusTip(_translate("MainWindow", "Sobel"))
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt"))
        self.actionPrewitt.setStatusTip(_translate("MainWindow", "Prewitt"))
        self.action_9.setText(_translate("MainWindow", "频域平滑"))
        self.action_9.setStatusTip(_translate("MainWindow", "频域平滑"))
        self.action_10.setText(_translate("MainWindow", "频域锐化"))
        self.action_10.setStatusTip(_translate("MainWindow", "频域锐化"))
        self.action_11.setText(_translate("MainWindow", "中值滤波"))
        self.action_11.setStatusTip(_translate("MainWindow", "中值滤波"))
        self.action_12.setText(_translate("MainWindow", "美白度选择"))
        self.action_12.setStatusTip(_translate("MainWindow", "美白度选择"))
        self.action_13.setText(_translate("MainWindow", "平滑度选择"))
        self.action_13.setStatusTip(_translate("MainWindow", "平滑度选择"))
        self.action_5.setText(_translate("MainWindow", "关于我们"))
        self.action_5.setStatusTip(_translate("MainWindow", "还原"))
        self.action_8.setText(_translate("MainWindow", "撤销"))
        self.action_8.setStatusTip(_translate("MainWindow", "撤销"))
        self.action_8.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.action_14.setText(_translate("MainWindow", "放大"))
        self.action_14.setStatusTip(_translate("MainWindow", "放大"))
        self.action_14.setShortcut(_translate("MainWindow", "+"))
        self.action_15.setText(_translate("MainWindow", "缩小"))
        self.action_15.setStatusTip(_translate("MainWindow", "缩小"))
        self.action_15.setShortcut(_translate("MainWindow", "-"))
        self.action_16.setText(_translate("MainWindow", "截图"))
        self.action_16.setStatusTip(_translate("MainWindow", "截图"))
        self.actionwo.setText(_translate("MainWindow", "wo"))
        self.actionGamma.setText(_translate("MainWindow", "Gamma变换"))
        self.actionAI.setText(_translate("MainWindow", "AI换脸功能"))
        self.action_17.setText(_translate("MainWindow", "图像处理功能"))
        self.action_18.setText(_translate("MainWindow", "视频处理功能"))
        self.action_19.setText(_translate("MainWindow", "检查更新"))
        self.action_20.setText(_translate("MainWindow", "重新下载"))
