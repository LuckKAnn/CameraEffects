# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imgUi.ui'
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
        MainWindow.resize(1145, 872)
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
        self._2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self._2.setContentsMargins(20, 20, 20, 20)
        self._2.setSpacing(10)
        self._2.setObjectName("_2")
        self.QWidgetLeft = QtWidgets.QWidget(self.centralwidget)
        self.QWidgetLeft.setStyleSheet("* {\n"
"background:#e6e2c3;\n"
"\n"
"\n"
"}")
        self.QWidgetLeft.setObjectName("QWidgetLeft")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.QWidgetLeft)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.QWidgetLeft)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QtCore.QSize(256, 600))
        self.tabWidget.setMaximumSize(QtCore.QSize(256, 600))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("*{\n"
"background-color:#99CCFF;\n"
"}")
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.tab_3.setFont(font)
        self.tab_3.setStyleSheet("QPushButton{\n"
"background-color: #acf6ef;\n"
"}")
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_16.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout_16.setSpacing(2)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_6.setStyleSheet("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_16.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_16.addWidget(self.pushButton_5)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_16.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_16.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_16.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_16.addWidget(self.pushButton_10)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_4.sizePolicy().hasHeightForWidth())
        self.tab_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.tab_4.setFont(font)
        self.tab_4.setStyleSheet("QPushButton{\n"
"background-color: #acf6ef;\n"
"}")
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setLineWidth(10)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider.setMinimum(-100)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_6.addWidget(self.horizontalSlider)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setLineWidth(10)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_4.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.horizontalSlider_4.setFont(font)
        self.horizontalSlider_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_4.setMouseTracking(False)
        self.horizontalSlider_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horizontalSlider_4.setMinimum(-100)
        self.horizontalSlider_4.setMaximum(100)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_4.setTickInterval(1)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.verticalLayout_4.addWidget(self.horizontalSlider_4)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_13.setObjectName("groupBox_13")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.groupBox_13)
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_16 = QtWidgets.QLabel(self.groupBox_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setTextFormat(QtCore.Qt.AutoText)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_17.addWidget(self.label_16)
        self.horizontalSlider_11 = QtWidgets.QSlider(self.groupBox_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_11.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.horizontalSlider_11.setFont(font)
        self.horizontalSlider_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_11.setMouseTracking(False)
        self.horizontalSlider_11.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horizontalSlider_11.setMaximum(10)
        self.horizontalSlider_11.setPageStep(10)
        self.horizontalSlider_11.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_11.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_11.setTickInterval(1)
        self.horizontalSlider_11.setObjectName("horizontalSlider_11")
        self.verticalLayout_17.addWidget(self.horizontalSlider_11)
        self.verticalLayout_2.addWidget(self.groupBox_13)
        self.groupBox_15 = QtWidgets.QGroupBox(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_15.sizePolicy().hasHeightForWidth())
        self.groupBox_15.setSizePolicy(sizePolicy)
        self.groupBox_15.setStyleSheet("")
        self.groupBox_15.setObjectName("groupBox_15")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.groupBox_15)
        self.verticalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_18 = QtWidgets.QLabel(self.groupBox_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setLineWidth(10)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_20.addWidget(self.label_18)
        self.horizontalSlider_13 = QtWidgets.QSlider(self.groupBox_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_13.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.horizontalSlider_13.setFont(font)
        self.horizontalSlider_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_13.setMouseTracking(False)
        self.horizontalSlider_13.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horizontalSlider_13.setMinimum(0)
        self.horizontalSlider_13.setMaximum(50)
        self.horizontalSlider_13.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_13.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_13.setTickInterval(10)
        self.horizontalSlider_13.setObjectName("horizontalSlider_13")
        self.verticalLayout_20.addWidget(self.horizontalSlider_13)
        self.verticalLayout_2.addWidget(self.groupBox_15)
        self.pushButton = QtWidgets.QPushButton(self.tab_4)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 204, 23))
        self.label.setMinimumSize(QtCore.QSize(10, 10))
        self.label.setLineWidth(10)
        self.label.setObjectName("label")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(10, 60, 204, 27))
        self.horizontalSlider_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_2.setMaximum(5)
        self.horizontalSlider_2.setPageStep(1)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_2.setTickInterval(1)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.tab.setFont(font)
        self.tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab.setStyleSheet("QPushButton{\n"
"background-color: #acf6ef;\n"
"}")
        self.tab.setObjectName("tab")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_18.addWidget(self.pushButton_12)

        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.pushButton_4 = QtWidgets.QPushButton(self.QWidgetLeft)
        self.pushButton_4.setStyleSheet("background-color: #fe6673;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.QWidgetLeft)
        self.pushButton_3.setStyleSheet("background-color: #fe6673;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.QWidgetLeft)
        self.pushButton_2.setStyleSheet("background-color: #fe6673;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self._2.addWidget(self.QWidgetLeft)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 500))
        self.graphicsView.setStyleSheet("border: 2px solid #CC0033;")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.graphicsView.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicsView.setRenderHints(QtGui.QPainter.SmoothPixmapTransform)
        self.graphicsView.setResizeAnchor(QtWidgets.QGraphicsView.NoAnchor)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.verticalLayout.setStretch(0, 100)
        self._2.addLayout(self.verticalLayout)
        self._2.setStretch(1, 13)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1145, 26))
        font = QtGui.QFont()
        font.setKerning(True)
        self.menubar.setFont(font)
        self.menubar.setMouseTracking(True)
        self.menubar.setTabletTracking(False)
        self.menubar.setAcceptDrops(True)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
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
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu_5.addAction(self.action_5)
        self.menu_2.addAction(self.actionAI)
        self.menu_2.addAction(self.action_17)
        self.menu_2.addAction(self.action_18)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.graphicsView, self.horizontalSlider)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "美颜相机"))
        self.pushButton_6.setText(_translate("MainWindow", "怀旧滤镜"))
        self.pushButton_5.setText(_translate("MainWindow", "PIL滤镜"))
        self.pushButton_7.setText(_translate("MainWindow", "凸透镜"))
        self.pushButton_8.setText(_translate("MainWindow", "颜色滤镜"))
        self.pushButton_9.setText(_translate("MainWindow", "天空背景滤镜"))
        self.pushButton_10.setText(_translate("MainWindow", "还原"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "滤镜"))
        self.groupBox_3.setTitle(_translate("MainWindow", "饱和度"))
        self.label_9.setText(_translate("MainWindow", "-100                           100"))
        self.groupBox.setTitle(_translate("MainWindow", "整体亮度"))
        self.label_6.setText(_translate("MainWindow", "-100                           100"))
        self.groupBox_13.setTitle(_translate("MainWindow", "磨皮程度"))
        self.label_16.setText(_translate("MainWindow", "0                                   10"))
        self.groupBox_15.setTitle(_translate("MainWindow", "美白度（皮肤识别）"))
        self.label_18.setText(_translate("MainWindow", "0                                    5"))
        self.pushButton.setText(_translate("MainWindow", "祛痘除斑魔法棒"))
        self.groupBox_2.setTitle(_translate("MainWindow", "魔法棒大小"))
        self.label.setText(_translate("MainWindow", "0                       5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "处理"))
        self.pushButton_12.setText(_translate("MainWindow", "贴一个兔耳朵"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "贴纸"))
        self.pushButton_4.setText(_translate("MainWindow", "人脸检测"))
        self.pushButton_3.setText(_translate("MainWindow", "从本地载入图片"))
        self.pushButton_2.setText(_translate("MainWindow", "从摄像头获取图片"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_5.setTitle(_translate("MainWindow", "关于"))
        self.menu_2.setTitle(_translate("MainWindow", "功能"))
        self.action.setText(_translate("MainWindow", "保存图片"))
        self.action.setStatusTip(_translate("MainWindow", "打开图片"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_2.setText(_translate("MainWindow", "图片另存为"))
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
