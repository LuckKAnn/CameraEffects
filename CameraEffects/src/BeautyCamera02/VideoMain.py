from PyQt5 import Qt
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QGraphicsRectItem, QGraphicsScene, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QSize, pyqtSignal
import cv2
import numpy as np
from matplotlib import pyplot as plt

import AiMain
import ImageMain
import  VideoUi as window
import window2


class VideoMain(QMainWindow):
    # 处理切换屏幕信号
    signal_ChangeAI = pyqtSignal()
    signal_Img = pyqtSignal()
    signal_Video = pyqtSignal()

    def __init__(self):
        super(VideoMain, self).__init__()
        self.raw_image = None
        self.ui = window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.TopbarAction_connect()

        # self.action_connect()
    def TopbarAction_connect(self):
        # 添加切屏的处理函数
        self.ui.actionAI.triggered.connect(self.slot_btn_changToAi)
        self.ui.action_17.triggered.connect(self.slot_btn_changToImg)
        self.ui.action_18.triggered.connect(self.slot_btn_changToVideo)
        self.signal_ChangeAI.connect(self.signal_ChangToAi_slot)
        self.signal_Img.connect(self.signal_ChangToImg_slot)
        self.signal_Video.connect(self.signal_ChangToVideo_slot)

    def slot_btn_changToAi(self):
        self.signal_ChangeAI.emit()

    def slot_btn_changToImg(self):
        self.signal_Img.emit()

    def slot_btn_changToVideo(self):
        self.signal_Video.emit()

    def signal_ChangToAi_slot(self):
        # self.hide()
        self.close()
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
# 信号槽绑定
#     def action_connect(self):
#         self.ui.action.triggered.connect(self.open_file)
#         self.ui.action_2.triggered.connect(self.save_file)
#         self.ui.action_5.triggered.connect(self.recover_img)
#
#         # 打开摄像头
#         self.ui.action_17.triggered.connect(self.new_camera)
#
#         # 标记人脸位置
#         self.ui.action_18.triggered.connect(self.mark_face)

# 显示图片
#     def show_image(self):
#         img_cv = cv2.cvtColor(self.current_img, cv2.COLOR_RGB2BGR)
#         img_width, img_height, a = img_cv.shape
#         ratio_img = img_width/img_height
#         ratio_scene = self.ui.graphicsView.width()/self.ui.graphicsView.height()
#         if ratio_img > ratio_scene:
#             width = int(self.ui.graphicsView.width())
#             height = int(self.ui.graphicsView.width() / ratio_img)
#         else:
#             width = int(self.ui.graphicsView.height() * ratio_img)
#             height = int(self.ui.graphicsView.height())
#         img_resize = cv2.resize(img_cv, (height-5, width-5), interpolation=cv2.INTER_AREA)
#         h, w, c = img_resize.shape
#         bytesPerLine = w * 3
#         qimg = QImage(img_resize.data, w, h, bytesPerLine, QImage.Format_RGB888)
#         self.scene = QGraphicsScene()
#         pix = QPixmap(qimg)
#         self.scene.addPixmap(pix)
#         self.ui.graphicsView.setScene(self.scene)

# # 显示灰度图像
#     def show_grayimage(self):
#         img_cv = self.gray_image
#         img_width, img_height = img_cv.shape
#         ratio_img = img_width/img_height
#         ratio_scene = self.ui.graphicsView.width()/self.ui.graphicsView.height()
#         if ratio_img > ratio_scene:
#             width = int(self.ui.graphicsView.width())
#             height = int(self.ui.graphicsView.width() / ratio_img)
#         else:
#             width = int(self.ui.graphicsView.height() * ratio_img)
#             height = int(self.ui.graphicsView.height())
#         img_resize = cv2.resize(img_cv, (height-5, width-5), interpolation=cv2.INTER_AREA)
#         h, w = img_resize.shape
#         qimg = QImage(img_resize.data, w, h, w, QImage.Format_Grayscale8)
#         self.scene = QGraphicsScene()
#         pix = QPixmap(qimg)
#         self.scene.addPixmap(pix)
#         self.ui.graphicsView.setScene(self.scene)

#
# # 显示直方图
#     def show_histogram(self):
#         if self.raw_image is None:
#             return 0
#         img = self.current_img
#         plt.figure(figsize=((self.ui.tab_3.width()-10)/100, (self.ui.tab_3.width()-60)/100), frameon=False)
#         plt.hist(img.ravel(), bins=256, range=[0, 256])
#         plt.axes().get_yaxis().set_visible(False)
#         # plt.axes().get_xaxis().set_visible(False)
#         ax = plt.axes()
#         # 隐藏坐标系的外围框线
#         for spine in ax.spines.values():
#             spine.set_visible(False)
#         plt.savefig('Hist.png', bbox_inches="tight", transparent=True, dpi=100)
#         pix = QPixmap("Hist.png")
#         self.ui.label.setPixmap(pix)
#         self.ui.label_2.setPixmap(pix)
#         self.ui.label_3.setPixmap(pix)



# 打开图片
#     def open_file(self):
#         fname = QFileDialog.getOpenFileName(None, '打开文件', './', ("Images (*.png *.xpm *.jpg)"))
#         if fname[0]:
#             img_cv = cv2.imdecode(np.fromfile(fname[0], dtype=np.uint8), -1)  # 注意这里读取的是RGB空间的
#             self.raw_image = img_cv
#             self.last_image = img_cv
#             self.current_img = img_cv
#             self.show_image()
#             self.show_histogram()
#             self.imgskin = np.zeros(self.raw_image.shape)
#         self.intial_value()

# # 恢复图片
#     def recover_img(self):
#         self.current_img = self.raw_image
#         self.show_image()
#         self.show_histogram()
#         self.intial_value()
#
# # 饱和度
#     def change_saturation(self):
#         if self.raw_image is None:
#             return 0
#
#         value = self.ui.horizontalSlider.value()
#         img_hsv = cv2.cvtColor(self.current_img, cv2.COLOR_BGR2HLS)
#         if value > 2:
#             img_hsv[:, :, 2] = np.log(img_hsv[:, :, 2] /255* (value - 1)+1) / np.log(value + 1) * 255
#         if value < 0:
#             img_hsv[:, :, 2] = np.uint8(img_hsv[:, :, 2] / np.log(- value + np.e))
#         self.current_img = cv2.cvtColor(img_hsv, cv2.COLOR_HLS2BGR)

# 明度调节
#     def change_darker(self):
#         if self.raw_image is None:
#             return 0
#         value = self.ui.horizontalSlider_4.value()
#         img_hsv = cv2.cvtColor(self.current_img, cv2.COLOR_BGR2HLS)
#         if value > 3:
#             img_hsv[:, :, 1] = np.log(img_hsv[:, :, 1] /255* (value - 1)+1) / np.log(value + 1) * 255
#         if value < 0:
#             img_hsv[:, :, 1] = np.uint8(img_hsv[:, :, 1] / np.log(- value + np.e))
#         self.last_image = self.current_img
#         self.current_img = cv2.cvtColor(img_hsv, cv2.COLOR_HLS2BGR)

# 人脸识别
    def detect_face(self):
        img = self.raw_image
        face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        return faces
