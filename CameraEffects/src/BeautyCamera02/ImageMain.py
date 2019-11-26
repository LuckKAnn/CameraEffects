import dlib
from PyQt5 import Qt
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QGraphicsRectItem, QGraphicsScene, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QSize, QObject
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PyQt5.QtCore import pyqtSignal
import  ImgUi as window
import  AiMain
import  VideoMain
import window2


class ImageMain(QMainWindow):
    #处理切换屏幕信号
    signal_ChangeAI = pyqtSignal()
    signal_Img = pyqtSignal()
    signal_Video = pyqtSignal()

    def __init__(self):
        super(ImageMain, self).__init__()
        self.raw_image = None
        self.ui = window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.action_connect()


    # 信号槽绑定
    def action_connect(self):
        self.ui.pushButton_3.clicked.connect(self.open_file)
        self.ui.pushButton_4.clicked.connect(self.detect_face)
        # 添加切屏的处理函数
        self.ui.actionAI.triggered.connect(self.slot_btn_changToAi)
        self.ui.action_17.triggered.connect(self.slot_btn_changToImg)
        self.ui.action_18.triggered.connect(self.slot_btn_changToVideo)
        self.signal_ChangeAI.connect(self.signal_ChangToAi_slot)
        self.signal_Img.connect(self.signal_ChangToImg_slot)
        self.signal_Video.connect(self.signal_ChangToVideo_slot)


        # self.ui.action_2.triggered.connect(self.save_file)
        # self.ui.action_5.triggered.connect(self.recover_img)
        #
        # # 打开摄像头
        # self.ui.action_17.triggered.connect(self.new_camera)
        #
        # # 标记人脸位置
        # self.ui.action_18.triggered.connect(self.mark_face)
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
        self.t = ImageMain()
        self.t.show()

    def signal_ChangToVideo_slot(self):
        self.hide()
        self.t = VideoMain.VideoMain()
        self.t.show()

    # 显示图片
    def show_image(self):
        img_cv = cv2.cvtColor(self.current_img, cv2.COLOR_RGB2BGR)
        img_width, img_height, a = img_cv.shape
        ratio_img = img_width/img_height
        ratio_scene = self.ui.graphicsView.width()/self.ui.graphicsView.height()
        if ratio_img > ratio_scene:
            width = int(self.ui.graphicsView.width())
            height = int(self.ui.graphicsView.width() / ratio_img)
        else:
            width = int(self.ui.graphicsView.height() * ratio_img)
            height = int(self.ui.graphicsView.height())
        img_resize = cv2.resize(img_cv, (height-5, width-5), interpolation=cv2.INTER_AREA)
        h, w, c = img_resize.shape
        bytesPerLine = w * 3
        qimg = QImage(img_resize.data, w, h, bytesPerLine, QImage.Format_RGB888)
        self.scene = QGraphicsScene()
        pix = QPixmap(qimg)
        self.scene.addPixmap(pix)
        self.ui.graphicsView.setScene(self.scene)


    # 打开图片
    def open_file(self):
        fname = QFileDialog.getOpenFileName(None, '打开文件', './', ("Images (*.png *.xpm *.jpg)"))
        if fname[0]:
            img_cv = cv2.imdecode(np.fromfile(fname[0], dtype=np.uint8), -1)  # 注意这里读取的是RGB空间的
            self.raw_image = img_cv
            self.last_image = img_cv
            self.current_img = img_cv
            self.show_image()
            self.imgskin = np.zeros(self.raw_image.shape)


    # 凹透镜
    def concave_lens_Filter(self):
        pass
    # PIL滤镜
    def PIL_Filiter(self):
        pass
    # 凸透镜
    def Convex_lens_Filter(self):
        pass
    # 颜色滤镜
    def color_Filter(self):
        pass
    # 天空背景滤镜
    def sky_Filter(self):
        pass
    # 还原
    def reset(self):
        pass

    # 饱和度
    def saturation(self):
        pass
    # 亮度
    def brightness(self):
        pass
    # 磨皮
    def Microdermabrasion(self):
        pass
    # 美白
    def Whitening(self):
        pass
    # 祛痘
    def Acne(self):
        pass

    # 人脸识别
    def detect_face(self):
        pass
