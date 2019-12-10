import time

from PyQt5 import Qt
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QGraphicsRectItem, QGraphicsScene, QMainWindow, \
    QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QSize, pyqtSignal
import cv2
import numpy as np
from matplotlib import pyplot as plt

import AiMain
import ImageMain
import  VideoUi as window
import about
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

        # self.action_connect()
        # 视频显示设置
        self.timer_camera = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.cap = cv2.VideoCapture()  # 视频流
        self.CAM_NUM = 0  # 为0时表示视频流来自笔记本内置摄像头
        self.TopbarAction_connect()
        # 创建新的视频流
        self.video = None

    def TopbarAction_connect(self):
        # 添加切屏的处理函数
        self.ui.actionAI.triggered.connect(self.slot_btn_changToAi)
        self.ui.action_17.triggered.connect(self.slot_btn_changToImg)
        self.ui.action_18.triggered.connect(self.slot_btn_changToVideo)
        self.signal_ChangeAI.connect(self.signal_ChangToAi_slot)
        self.signal_Img.connect(self.signal_ChangToImg_slot)
        self.signal_Video.connect(self.signal_ChangToVideo_slot)
        self.ui.pushButton_2.clicked.connect(self.button_open_camera_clicked)
        self.timer_camera.timeout.connect(self.show_camera)  # 若定时器结束，则调用show_camera()
        self.ui.pushButton_3.clicked.connect(self.open_file)
        # 关于我们
        self.ui.action_5.triggered.connect(self.aboutUs)
        # 保存当前视频
        self.ui.action.triggered.connect(self.saveCurrent)
        # 另存为
        self.ui.action_2.triggered.connect(self.saveCurrentAs)

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

    def aboutUs(self):
        try:
            Dialog = QtWidgets.QMainWindow()
            self.dialog = Dialog
            self.ui_5 = about.Ui_MainWindow()
            self.ui_5.setupUi(Dialog)
            Dialog.show()
        except Exception as e:
            print(e)
    # 保存为
    def saveCurrent(self):
        if self.raw_image is None:
            QMessageBox().information(self, "提示", "请先录入图像！", QMessageBox.Yes)
            return 0

        fileName = "./" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".jpg"
        print(fileName)
        cv2.imwrite(fileName, self.current_img)
        QMessageBox().information(self, "提示", "图片保存成功！", QMessageBox.Yes)

    # 另存为
    def saveCurrentAs(self):
        if self.raw_image is None:
            QMessageBox().information(self, "提示", "请先录入图像！", QMessageBox.Yes)
            return 0
        # fname = QFileDialog.getOpenFileName(None, '打开文件', './', ("Images (*.png *.jpeg *.jpg)"))
        fname = QFileDialog.getSaveFileName(None, "另存为", "./",
                                            "jpg Files (*.jpg);;png Files (*.png);;jpeg Files (*.jpeg)")
        if fname[0]:
            cv2.imwrite(fname[0], self.current_img)
            QMessageBox().information(self, "提示", "图片保存成功！", QMessageBox.Yes)
            # print(fname[0])

    def button_open_camera_clicked(self):
        if self.timer_camera.isActive() == False:  # 若定时器未启动
            flag = self.cap.open(self.CAM_NUM)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            if flag == False:  # flag表示open()成不成功
                msg = QtWidgets.QMessageBox.warning(self, 'warning', "请检查相机于电脑是否连接正确", buttons=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
                self.video = cv2.VideoWriter("./VideoTest1.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), 30, (640,480))
                # self.button_open_camera.setText('关闭相机')
        else:
            self.timer_camera.stop()  # 关闭定时器
            self.cap.release()  # 释放视频流
            self.label_show_camera.clear()  # 清空视频显示区域
            self.button_open_camera.setText('打开相机')

    def show_camera(self):

        flag, self.image = self.cap.read()  # 从视频流中读取
        self.video.write(self.image)
        self.brightness()
        show = cv2.resize(self.image, (640, 480))  # 把读到的帧的大小重新设置为 640x480
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        self.scene = QGraphicsScene()
        pix = QPixmap(showImage)
        self.scene.addPixmap(pix)
        self.ui.graphicsView.setScene(self.scene)
        # self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage

    # 打开图片
    def open_file(self):
        # fname = QFileDialog.getOpenFileName(None, '打开文件', './', ("Videos (*.avi *.mp4)"))
        fname = QFileDialog.getOpenFileName(None, '打开文件', './')
        # if fname[0]:
        #     img_cv = cv2.imdecode(np.fromfile(fname[0], dtype=np.uint8), -1)  # 注意这里读取的是RGB空间的
        #     self.raw_image = img_cv
        #     self.last_image = img_cv
        #     self.current_img = img_cv
        #     self.show_image()
        #     self.show_histogram()
        #     self.imgskin = np.zeros(self.raw_image.shape)
        # self.intial_value()
        print(fname[0])
        self.CAM_NUM = fname[0]
        self.button_open_camera_clicked()

        # 亮度
    def brightness(self):
            value = self.ui.horizontalSlider_4.value()
            # print(value)
            # print(value)


            # self.current_img = self.raw_image
            img_hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HLS)
            if value > 3:
                img_hsv[:, :, 1] = np.log(img_hsv[:, :, 1] / 255 * (value - 1) + 1) / np.log(value + 1) * 255
            if value < 0:
                img_hsv[:, :, 1] = np.uint8(img_hsv[:, :, 1] / np.log(- value + np.e))
            self.image = cv2.cvtColor(img_hsv, cv2.COLOR_HLS2BGR)

