"""
    视频处理主功能类
"""

import time

import dlib
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QGraphicsRectItem, QGraphicsScene, QMainWindow, \
    QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QSize, pyqtSignal
import cv2
import numpy as np

import AiMain
import ImageMain
import  VideoUi as window
import about


class VideoMain(QMainWindow):
    # 处理切换屏幕信号
    signal_ChangeAI = pyqtSignal()
    signal_Img = pyqtSignal()
    signal_Video = pyqtSignal()

    def __init__(self):
        super(VideoMain, self).__init__()
        self.image = None
        self.ui = window.Ui_MainWindow()
        self.ui.setupUi(self)
        #功能启用flag
        #分别是启用祛痘，贴纸，亮度调整，美白，磨皮，对比度
        self.acneFlag = False
        self.tieFlag = False
        self.brightFlag = False
        self.baiFlag = False
        self.microdermabrasionFlag = False
        self.saturationFlag = False
        self.faceTraceFlag = False
        # self.action_connect()
        # 视频显示设置
        self.timer_camera = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.cap = cv2.VideoCapture()  # 视频流
        self.CAM_NUM = 0  # 为0时表示视频流来自笔记本内置摄像头
        self.TopbarAction_connect()
        self.detector = dlib.get_frontal_face_detector()
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
        self.ui.pushButton_2.clicked.connect(self.openMyVideo)
        self.timer_camera.timeout.connect(self.show_camera)  # 若定时器结束，则调用show_camera()
        self.ui.pushButton_3.clicked.connect(self.open_file)
        # 关于我们
        self.ui.action_5.triggered.connect(self.aboutUs)
        # 保存当前视频
        self.ui.action.triggered.connect(self.saveCurrent)
        # 另存为
        self.ui.action_2.triggered.connect(self.saveCurrentAs)
        # 还原
        self.ui.action_21.triggered.connect(self.reset)
        self.ui.pushButton_5.clicked.connect(self.setOrigin)
        #祛痘
        self.ui.pushButton.clicked.connect(self.changeAcneFlag)
        #贴纸
        self.ui.pushButton_12.clicked.connect(self.changeTieFlag)
        self.ui.pushButton_4.clicked.connect(self.changeFaceTraceFlag)
        #绑定亮度和对比度的flag
        self.ui.horizontalSlider_4.sliderReleased.connect(self.changeBrightnessFlag)
        self.ui.horizontalSlider.sliderReleased.connect(self.changeSaturationFlag)
        self.ui.horizontalSlider_11.sliderReleased.connect(self.changeMoFlag)
        self.ui.horizontalSlider_13.sliderReleased.connect(self.changeBaiFlag)

    def openMyVideo(self):
        self.CAM_NUM = 0
        self.button_open_camera_clicked()

    def changeMoFlag(self):
        if self.image is None:
            QMessageBox().information(self, "提示", "请先录入视频！", QMessageBox.Yes)
            self.ui.horizontalSlider_11.setValue(0)
            return 0
        self.microdermabrasionFlag = True

    def changeBaiFlag(self):
        if self.image is None:
            QMessageBox().information(self, "提示", "请先录入视频！", QMessageBox.Yes)
            self.ui.horizontalSlider_13.setValue(0)
            return 0
        self.baiFlag =True

    def changeBrightnessFlag(self):
        if self.image is None:
            QMessageBox().information(self, "提示", "请先录入视频！", QMessageBox.Yes)
            self.ui.horizontalSlider_4.setValue(0)
            return 0
        self.brightFlag = True

    def changeSaturationFlag(self):
        if self.image is None:
            QMessageBox().information(self, "提示", "请先录入视频！", QMessageBox.Yes)
            self.ui.horizontalSlider.setValue(0)
            return 0
        self.saturationFlag = True
    #祛痘
    def changeAcneFlag(self):
        if self.image is None:
            QMessageBox().information(self, "提示", "请先录入视频！", QMessageBox.Yes)
            return 0
        self.acneFlag = True

    def changeFaceTraceFlag(self):
        if self.image is None:
            QMessageBox().information(self, "提示", "请先录入视频！", QMessageBox.Yes)
            # self.ui.horizontalSlider.setValue(0)
            return 0
        self.faceTraceFlag = True


    def changeTieFlag(self):
        self.tieFlag = True

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

    def setOrigin(self):
        self.acneFlag = False
        self.tieFlag = False
        self.brightFlag = False
        self.baiFlag = False
        self.microdermabrasionFlag = False
        self.saturationFlag = False
        self.faceTraceFlag = False
        self.intial_value()

    def reset(self):

        self.video.release()
        self.image=None
        self.ui.graphicsView.setScene(None)
        self.cap.release()  # 释放视频流
        self.intial_value()
        if(self.timer_camera.isActive()):
            self.timer_camera.stop()

    # 重置滑动条的值
    def intial_value(self):
        self.calculated = False
        self.ui.horizontalSlider.setValue(0)
        self.ui.horizontalSlider_4.setValue(0)
        self.ui.horizontalSlider_11.setValue(0)
        self.ui.horizontalSlider_13.setValue(0)

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
        if self.image is None:
            QMessageBox().information(self, "提示", "请先录入视频！", QMessageBox.Yes)
            return 0
        self.video.release()

        QMessageBox().information(self, "提示", "视频保存成功！", QMessageBox.Yes)

    # 另存为
    def saveCurrentAs(self):
        if self.image is None:
            QMessageBox().information(self, "提示", "请先录入视频！", QMessageBox.Yes)
            return 0
        # fname = QFileDialog.getOpenFileName(None, '打开文件', './', ("Images (*.png *.jpeg *.jpg)"))
        fname = QFileDialog.getSaveFileName(None, "另存为", "./", "avi Files (*.avi)")
        try:
            self.video.release()
            if fname[0]:
                fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
                output = cv2.VideoWriter(fname[0], fourcc, 20.0, (640, 480))
                newCap = cv2.VideoCapture("./temp/" + self.nowTime + ".mp4")
                while (True):
                    success, frame = newCap.read()
                    # show = cv2.resize(frame, (640, 480))
                    if success == True:
                        # print("打开")
                        # frame = cv2.flip(frame, 1)  # 图像水平翻转实现镜子
                        output.write(frame)  # 写入一帧画面
                        # cv2.imshow('video', frame)  # 显示画面
                        # if cv2.waitKey(1) & 0xFF == ord('q'):  # 等待关闭操作
                        #     break
                    else:
                        break
                output.release()
                QMessageBox().information(self, "提示", "保存成功！", QMessageBox.Yes)
        except Exception as e:
            print(e)

    def button_open_camera_clicked(self):
        if self.timer_camera.isActive() == False:  # 若定时器未启动
            flag = self.cap.open(self.CAM_NUM)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            if flag == False:  # flag表示open()成不成功
                msg = QtWidgets.QMessageBox.warning(self, 'warning', "请检查相机于电脑是否连接正确", buttons=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
                self.nowTime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
                self.video = cv2.VideoWriter("./temp/"+self.nowTime+".mp4", cv2.VideoWriter_fourcc('M', 'P', '4', 'V'), 20, (640,480))
                # self.button_open_camera.setText('关闭相机')
        else:
            self.timer_camera.stop()  # 关闭定时器
            self.cap.release()  # 释放视频流

    def show_camera(self):

        flag, self.image = self.cap.read()  # 从视频流中读取
        if self.brightFlag: #亮度
             self.brightness()
        if self.saturationFlag: #对比度
             self.saturation()
        if self.baiFlag: #美白
            # self.faceBrightness()
            self.Whitening()
        if self.microdermabrasionFlag: #磨皮
            self.Microdermabrasion()
        if self.acneFlag:
            self.acne()
        if self.faceTraceFlag:
            self.face_trace()
        if self.tieFlag:
            self.tiezhi()

        show = cv2.resize(self.image, (640, 480))  # 把读到的帧的大小重新设置为 640x480
        self.video.write(show)
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        self.scene = QGraphicsScene()
        pix = QPixmap(showImage)
        self.scene.addPixmap(pix)
        self.ui.graphicsView.setScene(self.scene)
        # self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage


    def tiezhi(self):
        img = self.image #img对象就为当前视频的帧，直接对其进行操作即可
        # TODO: 视频兔耳朵贴纸 可以使用video下的视频文件进行处理，也可以用摄像头处理
        self.image = img #对img进行操作之后，赋值回到image即可显示，可能视频播放会变慢，这是正常现象，因为在处理


    # 打开图片
    def open_file(self):
        fname = QFileDialog.getOpenFileName(None, '打开文件', './')
        print(fname[0])
        self.CAM_NUM = fname[0]
        self.button_open_camera_clicked()

        # 亮度
    def brightness(self):

        value = self.ui.horizontalSlider_4.value()
        if value == 0:
            self.brightFlag = False
            return 0
        img_hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HLS)
        if value > 3:
            img_hsv[:, :, 1] = np.log(img_hsv[:, :, 1] / 255 * (value - 1) + 1) / np.log(value + 1) * 255
        if value < 0:
            img_hsv[:, :, 1] = np.uint8(img_hsv[:, :, 1] / np.log(- value + np.e))
        self.image = cv2.cvtColor(img_hsv, cv2.COLOR_HLS2BGR)

    # 饱和度
    def saturation(self):

        # self.current_img = self.raw_image
        value = self.ui.horizontalSlider.value()
        if value==0:
            self.saturationFlag=False
            return 0
        img_hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HLS)
        if value > 2:
            img_hsv[:, :, 2] = np.log(img_hsv[:, :, 2] / 255 * (value - 1) + 1) / np.log(value + 1) * 255
        if value < 0:
            img_hsv[:, :, 2] = np.uint8(img_hsv[:, :, 2] / np.log(- value + np.e))
        self.image = cv2.cvtColor(img_hsv, cv2.COLOR_HLS2BGR)


    def face_trace(self):

        img_gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)

        # 人脸数
        faces = self.detector(img_gray, 0)
        if len(faces) != 0:
            # 记录每次开始写入人脸像素的宽度位置
            for face in faces:
                # 绘制矩形框
                cv2.rectangle(self.image, tuple([face.left(), face.top()]), tuple([face.right(), face.bottom()]),
                              (0, 255, 255), 2)
                ROI = self.image[face.top():face.bottom(), face.left(): face.right()]
                return ROI,face.top(),face.bottom(), face.left(), face.right()


        # pass

    # 人脸皮肤美白
    # def faceBrightness(self):
    #     try:
    #         beta = self.ui.horizontalSlider_13.value()*5
    #         if beta ==0:
    #             self.baiFlag=False
    #             return 0
    #         blank = np.zeros(self.image.shape, self.image.dtype)
    #         # dst = alpha * img + (1-alpha) * blank + beta
    #         dst = cv2.addWeighted(self.image, 1, blank, 0, beta)
    #         self.image = dst
    #     except Exception as e:
    #         print(e)

    def faceBrightness(self, beta, img):
        try:
            blank = np.zeros(img.shape, img.dtype)
            # dst = alpha * img + (1-alpha) * blank + beta
            dst = cv2.addWeighted(img, 1, blank, 0, beta)
            # self.image = dst
            return dst
        except Exception as e:
            print(e)

        # 美白
    def Whitening(self):

        # 原理: 先进行人脸识别，对人脸区域进行皮肤检测，皮肤检测之后，进行皮肤检测图的整体美白，整体美白之后，和原图融合
        try:
            img = self.image
            img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            # 人脸数
            faces = self.detector(img_gray, 0)
            if len(faces) != 0:
                for face in faces:
                    # 绘制矩形框
                    cv2.rectangle(img, tuple([face.left(), face.top()]), tuple([face.right(), face.bottom()]),
                                  (0, 255, 255), 2)
                    ROI = img[face.top():face.bottom(), face.left(): face.right()]
                    backSkin = self.myGetSkin(ROI)
                    degree = self.ui.horizontalSlider_13.value() * 2
                    backSkin = self.faceBrightness(degree, backSkin)
                    # cv2.imshow("backSkin",backSkin)
                    WhiteningImg = np.zeros(ROI.shape, np.uint8)
                    (x, y, a) = ROI.shape
                    for i in range(x):
                        for j in range(y):
                            if backSkin[i, j, 0] == degree and backSkin[i, j, 1] == degree and backSkin[
                                i, j, 2] == degree:
                                WhiteningImg[i][j] = ROI[i][j]
                            else:
                                WhiteningImg[i][j] = backSkin[i][j]  # 这样做是为了让原图与滤波后的图合成时更准确
                    img[face.top():face.bottom(), face.left(): face.right()] = WhiteningImg
            self.image  = img
        except Exception as e:
            print(e)

    # 肤色检测之一: YCrCb之Cr分量 + OTSU二值化
    def myGetSkin(self,image):
        img = image
        ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)  # 把图像转换到YUV色域
        (y, cr, cb) = cv2.split(ycrcb)  # 图像分割, 分别获取y, cr, br通道图像

        # 高斯滤波, cr 是待滤波的源图像数据, (5,5)是值窗口大小, 0 是指根据窗口大小来计算高斯函数标准差
        cr1 = cv2.GaussianBlur(cr, (5, 5), 0)  # 对cr通道分量进行高斯滤波
        # 根据OTSU算法求图像阈值, 对图像进行二值化
        _, skin1 = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        backans = np.zeros(img.shape, np.uint8)
        (x, y) = skin1.shape
        for i in range(x):
            for j in range(y):
                if skin1[i, j] != 0:
                    backans[i][j] = img[i][j]  # 这样做是为了让原图与滤波后的图合成时更准确
        return backans

    # 磨皮
    def Microdermabrasion(self):

        deep = self.ui.horizontalSlider_11.value()
        # blur = cv2.bilateralFilter(self.raw_image,deep,100,15)
        # blur = cv2.bilateralFilter(self.image, deep * 5, 100, 15)
        # cv2.imshow("no rui",blur)
        # 模糊之后再进行锐化
        # kernel = np.array([[0, -1, 0],
        #                    [-1, 5, -1],
        #                    [0, -1, 0]], np.float32)
        # dst = cv2.filter2D(blur, -1, kernel=kernel)
        # self.image=blur
        img = self.image
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # 人脸数
        faces = self.detector(img_gray, 0)
        if len(faces) != 0:
            for face in faces:
                # 绘制矩形框
                cv2.rectangle(img, tuple([face.left(), face.top()]), tuple([face.right(), face.bottom()]),
                              (0, 255, 255), 2)
                ROI = img[face.top():face.bottom(), face.left(): face.right()]
                blur = cv2.bilateralFilter(ROI, deep * 5, 100, 15)
                kernel = np.array([[0, -1, 0],
                                   [-1, 5, -1],
                                   [0, -1, 0]], np.float32)
                dst = cv2.filter2D(blur, -1, kernel=kernel)
                img[face.top():face.bottom(), face.left(): face.right()] = dst

        self.image = img

    # def acne(self):
    #     deep = 10
    #     roi ,top,bottom,left,right = self.face_trace()
    #     # blur = cv2.bilateralFilter(self.raw_image,deep,100,15)
    #     # blur = cv2.bilateralFilter(self.image, deep * 5, 100, 15)
    #     blur = cv2.bilateralFilter(roi, deep * 5, 100, 15)
    #     # cv2.imshow("no rui",blur)
    #     # 模糊之后再进行锐化
    #     kernel = np.array([[0, -1, 0],
    #                        [-1, 5, -1],
    #                        [0, -1, 0]], np.float32)
    #     dst = cv2.filter2D(blur, -1, kernel=kernel)
    #     self.image[top:bottom,left:bottom] = dst

        # self.image = dst
    def acne(self):

        img = self.image
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # 人脸数
        faces = self.detector(img_gray, 0)
        if len(faces) != 0:
            for face in faces:
                # 绘制矩形框
                cv2.rectangle(img, tuple([face.left(), face.top()]), tuple([face.right(), face.bottom()]),
                              (0, 255, 255), 2)
                ROI = img[face.top():face.bottom(), face.left(): face.right()]
                deep = 10
                blur = cv2.bilateralFilter(ROI, deep * 5, 100, 15)
                kernel = np.array([[0, -1, 0],
                                  [-1, 5, -1],
                                  [0, -1, 0]], np.float32)
                dst = cv2.filter2D(blur, -1, kernel=kernel)
                img[face.top():face.bottom(), face.left(): face.right()] = dst

        self.image = img