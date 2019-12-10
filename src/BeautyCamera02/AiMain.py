from PyQt5 import Qt
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QGraphicsRectItem, QGraphicsScene, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QSize, QObject, pyqtSignal
import cv2
import numpy as np
from matplotlib import pyplot as plt

import ImageMain
import VideoMain
import  AiUi as window

class AiMain(QMainWindow):
    # 处理切换屏幕信号
    signal_ChangeAI = pyqtSignal()
    signal_Img = pyqtSignal()
    signal_Video = pyqtSignal()

    def __init__(self):
        super(AiMain, self).__init__()
        self.raw_image = None
        self.ui = window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.TopbarAction_connect()
        self.action_connect()

    # 信号槽绑定
    def TopbarAction_connect(self):
        # 添加切屏的处理函数
        self.ui.actionAI.triggered.connect(self.slot_btn_changToAi)
        self.ui.action_17.triggered.connect(self.slot_btn_changToImg)
        self.ui.action_18.triggered.connect(self.slot_btn_changToVideo)
        self.signal_ChangeAI.connect(self.signal_ChangToAi_slot)
        self.signal_Img.connect(self.signal_ChangToImg_slot)
        self.signal_Video.connect(self.signal_ChangToVideo_slot)

    # 信号槽绑定
    def action_connect(self):
        # 绑定相应按钮事件
        self.ui.pushButton.clicked.connect(lambda :self.open_file(2))
        self.ui.pushButton_3.clicked.connect(lambda : self.open_file(1))
        self.ui.pushButton_5.clicked.connect(self.change_face)


    # 以下为切换操作界面的函数
    def slot_btn_changToAi(self):
        self.signal_ChangeAI.emit()

    def slot_btn_changToImg(self):
        self.signal_Img.emit()

    def slot_btn_changToVideo(self):
        self.signal_Video.emit()

    def signal_ChangToAi_slot(self):
        self.hide()
        self.t = AiMain.AiMain()
        self.t.show()

    def signal_ChangToImg_slot(self):
        self.hide()
        self.t = ImageMain.ImageMain()
        self.t.show()

    def signal_ChangToVideo_slot(self):
        self.hide()
        self.t = VideoMain.VideoMain()
        self.t.show()


    # 打开图片功能函数
    def open_file(self,buttonNumb):
        fname = QFileDialog.getOpenFileName(None, '打开文件', './', ("Images (*.png *.xpm *.jpg)"))
        if fname[0]:
            img_cv = cv2.imdecode(np.fromfile(fname[0], dtype=np.uint8), -1)  # 注意这里读取的是RGB空间的
            self.raw_image = img_cv
            self.last_image = img_cv
            self.current_img = img_cv
            if(buttonNumb==1): self.show_image_first()
            if (buttonNumb == 2): self.show_image_second()
            if (buttonNumb == 3): self.show_image_third()
            self.imgskin = np.zeros(self.raw_image.shape)

    # 在第一个选框中现实载入的图片
    def show_image_first(self):
        img_cv = cv2.cvtColor(self.current_img, cv2.COLOR_RGB2BGR)
        img_width, img_height, a = img_cv.shape
        ratio_img = img_width / img_height
        ratio_scene = self.ui.graphicsView.width() / self.ui.graphicsView.height()
        if ratio_img > ratio_scene:
            width = int(self.ui.graphicsView.width())
            height = int(self.ui.graphicsView.width() / ratio_img)
        else:
            width = int(self.ui.graphicsView.height() * ratio_img)
            height = int(self.ui.graphicsView.height())
        img_resize = cv2.resize(img_cv, (height - 5, width - 5), interpolation=cv2.INTER_AREA)
        h, w, c = img_resize.shape
        bytesPerLine = w * 3
        qimg = QImage(img_resize.data, w, h, bytesPerLine, QImage.Format_RGB888)
        self.scene = QGraphicsScene()
        pix = QPixmap(qimg)
        self.scene.addPixmap(pix)
        self.ui.graphicsView.setScene(self.scene)

    # 在第二个选框中现实载入的图片
    def show_image_second(self):
        img_cv = cv2.cvtColor(self.current_img, cv2.COLOR_RGB2BGR)
        img_width, img_height, a = img_cv.shape
        ratio_img = img_width / img_height
        ratio_scene = self.ui.graphicsView_2.width() / self.ui.graphicsView_2.height()
        if ratio_img > ratio_scene:
            width = int(self.ui.graphicsView_2.width())
            height = int(self.ui.graphicsView_2.width() / ratio_img)
        else:
            width = int(self.ui.graphicsView_2.height() * ratio_img)
            height = int(self.ui.graphicsView_2.height())
        img_resize = cv2.resize(img_cv, (height - 5, width - 5), interpolation=cv2.INTER_AREA)
        h, w, c = img_resize.shape
        bytesPerLine = w * 3
        qimg = QImage(img_resize.data, w, h, bytesPerLine, QImage.Format_RGB888)
        self.scene = QGraphicsScene()
        pix = QPixmap(qimg)
        self.scene.addPixmap(pix)
        self.ui.graphicsView_2.setScene(self.scene)

    # 显示换脸以后的图片
    def show_image_third(self,img):
        img_cv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img_width, img_height, a = img_cv.shape
        ratio_img = img_width / img_height
        ratio_scene = self.ui.graphicsView_3.width() / self.ui.graphicsView_3.height()
        if ratio_img > ratio_scene:
            width = int(self.ui.graphicsView_3.width())
            height = int(self.ui.graphicsView_3.width() / ratio_img)
        else:
            width = int(self.ui.graphicsView_3.height() * ratio_img)
            height = int(self.ui.graphicsView_3.height())
        img_resize = cv2.resize(img_cv, (height - 5, width - 5), interpolation=cv2.INTER_AREA)
        h, w, c = img_resize.shape
        bytesPerLine = w * 3
        qimg = QImage(img_resize.data, w, h, bytesPerLine, QImage.Format_RGB888)
        self.scene = QGraphicsScene()
        pix = QPixmap(qimg)
        self.scene.addPixmap(pix)
        self.ui.graphicsView_3.setScene(self.scene)


    # 换脸功能函数
    # TODO: 书写换脸功能核心代码
    def change_face(self):
        """核心代码编辑之后，调用show_image_third()显示即可"""
        self.show_image_third() #填入结果图片
        pass

