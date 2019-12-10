import math
import time

import dlib
from PyQt5 import Qt
from PyQt5 import QtCore,QtWidgets,QtGui
import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QGraphicsRectItem, QGraphicsScene, QMainWindow, \
    QMessageBox, QDialog
from PyQt5.QtGui import QPixmap, QImage, QMouseEvent, QCursor
from PyQt5.QtCore import QSize, QObject, QPointF
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PyQt5.QtCore import pyqtSignal
from matplotlib.backends.backend_template import FigureCanvas

import  ImgUi as window
import  AiMain
import  VideoMain
import GetImgFromCamera
import about
import colormap
import  pil
from PIL import ImageFilter, Image


class ImageMain(QMainWindow):
    #处理切换屏幕信号
    signal_ChangeAI = pyqtSignal()
    signal_Img = pyqtSignal()
    signal_Video = pyqtSignal()

    def __init__(self):
        super(ImageMain, self).__init__()
        self.raw_image = None
        self.origin_image = None
        self.current_img = None
        self.ui = window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_var()
        self.action_connect()

    def init_var(self):
        self.acne = False
        self.Totutoujing = False
        self.acneSize=1

    # 信号槽绑定
    def action_connect(self):
        self.ui.pushButton_3.clicked.connect(self.open_file)

        # 人脸识别绑定
        self.ui.pushButton_4.clicked.connect(self.detect_face)
        # 添加切屏的处理函数
        self.ui.actionAI.triggered.connect(self.slot_btn_changToAi)
        self.ui.action_17.triggered.connect(self.slot_btn_changToImg)
        self.ui.action_18.triggered.connect(self.slot_btn_changToVideo)
        # 取消当前载入的图片
        self.ui.action_21.triggered.connect(self.delete)
        # 保存当前图片
        self.ui.action.triggered.connect(self.saveCurrent)
        # 另存为
        self.ui.action_2.triggered.connect(self.saveCurrentAs)
        # 怀旧滤镜
        self.ui.pushButton_6.clicked.connect(self.Reminiscene)
        #关于我们
        self.ui.action_5.triggered.connect(self.aboutUs)

        # PIL滤镜选框点击
        self.ui.pushButton_5.clicked.connect(self.open_pil)
        # 颜色滤镜选框点击
        self.ui.pushButton_8.clicked.connect(self.open_colorMap)
        self.ui.pushButton_9.clicked.connect(self.sky_Filter)
        # 切屏按钮事件绑定
        self.signal_ChangeAI.connect(self.signal_ChangToAi_slot)
        self.signal_Img.connect(self.signal_ChangToImg_slot)
        self.signal_Video.connect(self.signal_ChangToVideo_slot)
        #亮度功能绑定
        # self.ui.horizontalSlider_4.valueChanged.connect(self.slider_change)
        # self.ui.horizontalSlider_4.valueChanged.connect(self.brightness)

        self.ui.horizontalSlider_4.sliderReleased.connect(self.brightness)

        self.ui.horizontalSlider.sliderReleased.connect(self.saturation)
        # 磨皮
        self.ui.horizontalSlider_11.sliderReleased.connect(self.Microdermabrasion)
        # 美白
        self.ui.horizontalSlider_13.sliderReleased.connect(self.Whitening)
        self.ui.horizontalSlider_2.sliderReleased.connect(self.acneSizeTest)

        self.ui.pushButton_10.clicked.connect(self.reset)

        self.ui.pushButton_2.clicked.connect(self.new_camera)

        # 凸透镜
        self.ui.pushButton_7.clicked.connect(self.tutoujing)
        self.ui.pushButton.clicked.connect(self.Toacne)

        # self.ui.horizontalSlider_4.valueChanged.connect(self.brightness)
        # self.ui.horizontalSlider_4.sliderPressed.connect(self.sldDisconnect)
        # self.ui.horizontalSlider_4.sliderReleased.connect(self.sldReconnect)
        # self.ui.action_2.triggered.connect(self.save_file)
        # self.ui.action_5.triggered.connect(self.recover_img)
        #
        # # 打开摄像头
        # self.ui.action_17.triggered.connect(self.new_camera)
        #
        # # 标记人脸位置
        # self.ui.action_18.triggered.connect(self.mark_face)



    # 保存为
    def saveCurrent(self):
        if self.raw_image is None :
            QMessageBox().information(self, "提示", "请先录入图像！", QMessageBox.Yes)
            return 0

        fileName = "./"+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+".jpg"
        print(fileName)
        cv2.imwrite(fileName,self.current_img)
        QMessageBox().information(self, "提示", "图片保存成功！", QMessageBox.Yes)

    # 另存为
    def saveCurrentAs(self):
        if self.raw_image is None :
            QMessageBox().information(self, "提示", "请先录入图像！", QMessageBox.Yes)
            return 0
        # fname = QFileDialog.getOpenFileName(None, '打开文件', './', ("Images (*.png *.jpeg *.jpg)"))
        fname = QFileDialog.getSaveFileName(None,"另存为","./","jpg Files (*.jpg);;png Files (*.png);;jpeg Files (*.jpeg)")
        if fname[0]:
            cv2.imwrite(fname[0],self.current_img)
            QMessageBox().information(self, "提示", "图片保存成功！", QMessageBox.Yes)
            # print(fname[0])

    def aboutUs(self):
        try:
            Dialog = QtWidgets.QMainWindow()
            self.dialog = Dialog
            self.ui_5 = about.Ui_MainWindow()
            self.ui_5.setupUi(Dialog)
            Dialog.show()
        except Exception as e:
            print(e)



    def slot_btn_changToAi(self):
        self.signal_ChangeAI.emit()

    def slot_btn_changToImg(self):
        self.signal_Img.emit()

    def slot_btn_changToVideo(self):
        self.signal_Video.emit()

    # 凸透镜功能可用
    def tutoujing(self):
        if self.raw_image is None:
            QMessageBox().information(self, "提示", "请先录入图像！", QMessageBox.Yes)
            return 0
        self.Totutoujing=True
    # 祛痘功能可用
    def Toacne(self):
        if self.raw_image is None:
            QMessageBox().information(self, "提示", "请先录入图像！", QMessageBox.Yes)
            return 0
        self.acne=True

    # 三个切屏事件响应函数
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

    # 打开PIL滤镜选择框
    def open_pil(self):
        if self.raw_image is None:
            QMessageBox().information(self, "提示", "请先录入图像！", QMessageBox.Yes)
            return 0
        try:
            Dialog = QtWidgets.QMainWindow()
            self.dialog = Dialog
            self.ui_3 = pil.Ui_MainWindow()
            self.ui_3.setupUi(Dialog)
            # PIL滤镜弹出框按钮事件绑定
            self.ui_3.pushButton.clicked.connect(self.CONTOUR)
            self.ui_3.pushButton_2.clicked.connect(self.EDGE_ENHANCE_MORE)
            self.ui_3.pushButton_3.clicked.connect(self.EMBOSS)
            Dialog.show()
            # Dialog.exec_()
        except Exception as e :
            print(e)

    def delete(self):
        self.raw_image = None
        self.last_image = None
        self.current_img = None
        self.ui.graphicsView.setScene(None)
        print("已经恢复")

    # 打开颜色滤镜选择框
    def open_colorMap(self):
        if self.raw_image is None:
            QMessageBox().information(self, "提示", "请先录入图像！", QMessageBox.Yes)
            return 0

        try:
            Dialog = QtWidgets.QMainWindow()
            self.dialog = Dialog
            self.ui_4 = colormap.Ui_MainWindow()
            self.ui_4.setupUi(Dialog)
            # 颜色滤镜按钮选框事件绑定
            self.ui_4.pushButton.clicked.connect(self.color_autumn)
            self.ui_4.pushButton_2.clicked.connect(self.color_bone)
            self.ui_4.pushButton_3.clicked.connect(self.color_hot)
            self.ui_4.pushButton_4.clicked.connect(self.color_jet)
            self.ui_4.pushButton_5.clicked.connect(self.color_ocean)
            self.ui_4.pushButton_6.clicked.connect(self.color_ocean)
            self.ui_4.pushButton_7.clicked.connect(self.color_spring)
            self.ui_4.pushButton_8.clicked.connect(self.color_summer)
            self.ui_4.pushButton_9.clicked.connect(self.color_winter)
            Dialog.show()
            # Dialog.exec_()
        except Exception as e:
            print(e)
    # 秋日滤镜绑定
    def color_autumn(self):
        self.dialog.close()
        current_gray = cv2.cvtColor(self.current_img.copy(),cv2.COLOR_RGB2GRAY)
        im_color = cv2.applyColorMap(current_gray, cv2.COLORMAP_AUTUMN)
        self.current_img = im_color
        self.show_image()

    # 萧瑟滤镜绑定
    def color_bone(self):
        self.dialog.close()
        current_gray = cv2.cvtColor(self.current_img.copy(), cv2.COLOR_RGB2GRAY)
        im_color = cv2.applyColorMap(current_gray, cv2.COLORMAP_BONE)
        self.current_img = im_color
        self.show_image()

    # hot滤镜绑定
    def color_hot(self):
        self.dialog.close()
        current_gray = cv2.cvtColor(self.current_img.copy(), cv2.COLOR_RGB2GRAY)
        im_color = cv2.applyColorMap(current_gray, cv2.COLORMAP_HOT)
        self.current_img = im_color
        self.show_image()

    # 喷射滤镜绑定
    def color_jet(self):
        self.dialog.close()
        current_gray = cv2.cvtColor(self.current_img.copy(), cv2.COLOR_RGB2GRAY)
        im_color = cv2.applyColorMap(current_gray, cv2.COLORMAP_JET)
        self.current_img = im_color
        self.show_image()

    # 海洋滤镜绑定
    def color_ocean(self):
        self.dialog.close()
        current_gray = cv2.cvtColor(self.current_img.copy(), cv2.COLOR_RGB2GRAY)
        im_color = cv2.applyColorMap(current_gray, cv2.COLORMAP_OCEAN)
        self.current_img = im_color
        self.show_image()

    # 彩虹滤镜绑定
    def color_rainbow(self):
        self.dialog.close()
        current_gray = cv2.cvtColor(self.current_img.copy(), cv2.COLOR_RGB2GRAY)
        im_color = cv2.applyColorMap(current_gray, cv2.COLORMAP_RAINBOW)
        self.current_img = im_color
        self.show_image()

    # 春日滤镜绑定
    def color_spring(self):
        self.dialog.close()
        current_gray = cv2.cvtColor(self.current_img.copy(), cv2.COLOR_RGB2GRAY)
        im_color = cv2.applyColorMap(current_gray, cv2.COLORMAP_SPRING)
        self.current_img = im_color
        self.show_image()

    # 夏日滤镜绑定
    def color_summer(self):
        self.dialog.close()
        current_gray = cv2.cvtColor(self.current_img.copy(), cv2.COLOR_RGB2GRAY)
        im_color = cv2.applyColorMap(current_gray, cv2.COLORMAP_SUMMER)
        self.current_img = im_color
        self.show_image()

    # 冬日滤镜绑定
    def color_winter(self):
        self.dialog.close()
        current_gray = cv2.cvtColor(self.current_img.copy(), cv2.COLOR_RGB2GRAY)
        im_color = cv2.applyColorMap(current_gray, cv2.COLORMAP_WINTER)
        self.current_img = im_color
        self.show_image()


    # 浮雕滤镜
    def EMBOSS(self):
        try:
            self.dialog.close()
            PIL_Img = Image.fromarray(self.current_img)
            pilAnsImg = PIL_Img.filter(ImageFilter.EMBOSS)
            self.current_img = np.asarray(pilAnsImg)
            self.show_image()
        except Exception as e:
            print(e)

    # 轮廓滤镜
    def CONTOUR(self):

        try:
            self.dialog.close()
            PIL_Img = Image.fromarray(self.current_img)
            pilAnsImg = PIL_Img.filter(ImageFilter.CONTOUR)
            self.current_img = np.asarray(pilAnsImg)
            print("???")
            self.show_image()
        except Exception as e:
            print(e)

    # PIL边界增强滤镜
    def EDGE_ENHANCE_MORE(self):

        try:
            self.dialog.close()
            PIL_Img = Image.fromarray(self.current_img)
            pilAnsImg = PIL_Img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            self.current_img = np.asarray(pilAnsImg)
            self.show_image()
        except Exception as e:
            print(e)

    # 显示图片
    def show_image(self):
        img_cv = cv2.cvtColor(self.current_img, cv2.COLOR_RGB2BGR)
        # img_cv = self.current_img
        img_width, img_height, a = img_cv.shape
        # cv2.imshow("??",img_cv)
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
        # bytesPerLine = img_width * 3
        qimg = QImage(img_resize.data, w, h, bytesPerLine, QImage.Format_RGB888)
        # qimg = QImage(img_cv.data, img_width, img_height, QImage.Format_RGB888)
        # self.scene = QGraphicsScene()
        self.scene = CARscene()
        pix = QPixmap(qimg)
        self.scene.addPixmap(pix)
        self.ui.graphicsView.setScene(self.scene)
        # cv2.imshow("???",img_resize)
        return img_resize

    # 鼠标点击事件
    def mousePressEvent(self,QMouseEvent):
        if self.acne == True:
            self.Acne()
        if self.Totutoujing == True:
            self.Convex_lens_Filter()


    # 打开图片
    def open_file(self):
        fname = QFileDialog.getOpenFileName(None, '打开文件', './', ("Images (*.png *.xpm *.jpg)"))
        if fname[0]:
            img_cv = cv2.imdecode(np.fromfile(fname[0], dtype=np.uint8), -1)  # 注意这里读取的是RGB空间的
            #
            # img_cv = cv2.imread(fname[0])
            self.current_img = img_cv
            self.origin_image = cv2.imread(fname[0])
            self.origin_image = cv2.resize(self.origin_image,(375,500))
            final_img=self.show_image()
            cv2.imwrite("user.jpg",final_img)
            canuse = cv2.cvtColor(final_img,cv2.COLOR_BGR2RGB)
            self.raw_image = canuse
            self.last_image = canuse
            self.current_img = canuse
            self.imgskin = np.zeros(self.raw_image.shape)



    # 怀旧滤镜
    def Reminiscene(self):
        if self.raw_image is None:
            QMessageBox().information(self, "提示", "请先录入图像！", QMessageBox.Yes)
            return 0
        img = self.current_img.copy()
        rows, cols, channals = img.shape
        for r in range(rows):
            for c in range(cols):
                B = img.item(r, c, 0)
                G = img.item(r, c, 1)
                R = img.item(r, c, 2)
                img[r, c, 0] = np.uint8(min(max(0.272 * R + 0.534 * G + 0.131 * B, 0), 255))
                img[r, c, 1] = np.uint8(min(max(0.349 * R + 0.686 * G + 0.168 * B, 0), 255))
                img[r, c, 2] = np.uint8(min(max(0.393 * R + 0.769 * G + 0.189 * B, 0), 255))
        self.current_img = img
        self.show_image()



    # 凸透镜
    def Convex_lens_Filter(self):
        if self.raw_image is None:
            QMessageBox().information(self, "提示", "请先录入图像！", QMessageBox.Yes)
            return 0
        center_x = self.scene.y
        center_y = self.scene.x
        print(center_x)
        print(center_y)
        if center_x == 0 or center_y == 0:
            return 0
        row = self.current_img.shape[0]
        col = self.current_img.shape[1]
        channel = self.current_img.shape[2]
        new_img = np.zeros([row, col, channel], dtype=np.uint8)
        radius=math.sqrt(center_x*center_x+center_y*center_y)/2
        for i in range(row):
            for j in range(col):

                distance = ((i - center_x) * (i - center_x) + (j - center_y) * (j - center_y))
                new_dist = math.sqrt(distance)
                new_img[i, j, :] = self.current_img[i, j, :]
                if distance <= radius ** 2:
                    new_i = np.int(np.floor(new_dist * (i - center_x) / radius + center_x))
                    new_j = np.int(np.floor(new_dist * (j - center_y) / radius + center_y))
                    new_img[i, j, :] = self.current_img[new_i, new_j, :]
        self.current_img = new_img
        self.Totutoujing = False
        self.show_image()

    # 天空区域检测
    def skyRegion(self,picname):
        iLow = np.array([100, 43, 46])
        iHigh = np.array([124, 255, 255])
        # img = cv2.imread(picname)
        img = picname
        # imgOriginal = cv2.imread(picname)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # hsv split
        h, s, v = cv2.split(img)
        cv2.equalizeHist(v)
        hsv = cv2.merge((h, s, v))
        imgThresholded = cv2.inRange(hsv, iLow, iHigh)
        cv2.imshow("aaa", imgThresholded)
        imgThresholded = cv2.medianBlur(imgThresholded, 9)
        cv2.imshow("bbb", imgThresholded)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
        Erode_img = cv2.erode(imgThresholded, kernel)
        Dilation_img = cv2.dilate(Erode_img, kernel)
        # print(tmp)
        cv2.imshow("xx", Dilation_img)
        # open
        kernel = np.ones((5, 5), np.uint8)
        imgThresholded = cv2.morphologyEx(imgThresholded, cv2.MORPH_OPEN, kernel, iterations=10)
        imgThresholded = cv2.medianBlur(imgThresholded, 9)
        cv2.imshow("??", imgThresholded)
        return imgThresholded
    # 天空背景滤镜
    def sky_Filter(self):
        if self.raw_image is None:
            QMessageBox().information(self, "提示", "请先录入图像！", QMessageBox.Yes)
            return 0
        src_img  = self.origin_image
        sky_img = cv2.imread('sky.jpg')
        try:
            merge_img = self.Segment(src_img, sky_img)

            self.current_img = merge_img
            self.show_image()
        except Exception as e :
            print(e)
    # 天空区域合并
    def Segment(self,src, sky_img):
        mask = self.skyRegion1(src)
        notmask = cv2.bitwise_not(mask)
        cv2.imshow("notmask", notmask)
        frontpic = cv2.bitwise_and(src, src, mask=notmask)

        sky_resize = cv2.resize(sky_img, (src.shape[1], src.shape[0]))
        backimage = cv2.bitwise_and(sky_resize, sky_resize, mask=mask)
        merge_img = cv2.add(backimage, frontpic)
        cv2.imshow("merge_img", merge_img)
        return merge_img

    # 还原
    def reset(self):
        if self.current_img is None or self.raw_image is None:
            QMessageBox().information(self, "提示", "请先录入图像！", QMessageBox.Yes)
            return 0
        self.current_img = self.raw_image
        self.show_image()
        self.intial_value()

    # 重置滑动条的值
    def intial_value(self):
        self.calculated = False
        self.ui.horizontalSlider.setValue(0)
        self.ui.horizontalSlider_2.setValue(0)
        self.ui.horizontalSlider_4.setValue(0)
        self.ui.horizontalSlider_11.setValue(0)
        self.ui.horizontalSlider_13.setValue(0)

    # 饱和度
    def saturation(self):
        if self.raw_image is None:
            return 0
        # self.current_img = self.raw_image
        value = self.ui.horizontalSlider.value()
        img_hsv = cv2.cvtColor(self.current_img, cv2.COLOR_BGR2HLS)
        if value > 2:
            img_hsv[:, :, 2] = np.log(img_hsv[:, :, 2] / 255 * (value - 1) + 1) / np.log(value + 1) * 255
        if value < 0:
            img_hsv[:, :, 2] = np.uint8(img_hsv[:, :, 2] / np.log(- value + np.e))
        self.current_img = cv2.cvtColor(img_hsv, cv2.COLOR_HLS2BGR)
        self.show_image()

    # 亮度
    def brightness(self):
        if self.raw_image is None:
            self.ui.horizontalSlider_4.setValue(0)
            QMessageBox().information(self, "提示", "请先录入图像！", QMessageBox.Yes)
            return 0
        value = self.ui.horizontalSlider_4.value()
        # print(value)
        # self.current_img = self.raw_image
        img_hsv = cv2.cvtColor(self.current_img, cv2.COLOR_BGR2HLS)
        if value > 3:
            img_hsv[:, :, 1] = np.log(img_hsv[:, :, 1] / 255 * (value - 1) + 1) / np.log(value + 1) * 255
        if value < 0:
            img_hsv[:, :, 1] = np.uint8(img_hsv[:, :, 1] / np.log(- value + np.e))
        self.last_image = self.current_img
        self.current_img = cv2.cvtColor(img_hsv, cv2.COLOR_HLS2BGR)
        self.show_image()

    # 磨皮
    def Microdermabrasion(self):
        deep =self.ui.horizontalSlider_11.value()
        # blur = cv2.bilateralFilter(self.raw_image,deep,100,15)
        blur = cv2.bilateralFilter(self.raw_image,deep*5,100,15)
        cv2.imshow("no rui",blur)
        #模糊之后再进行锐化
        kernel = np.array([[0 ,-1 ,0],
                           [-1 ,5 ,-1],
                           [0 ,-1 ,0]],np.float32)
        dst = cv2.filter2D(blur,-1,kernel= kernel)
        cv2.imshow("rui",dst)
        cv2.waitKey(0)


    # 美白
    def Whitening(self):
        pass

    # 祛痘
    def Acne(self):
        self.acneSize = self.ui.horizontalSlider_2.value()
        print(self.acneSize)
        center_x = self.scene.x
        center_y = self.scene.y
        print(center_x)
        print(center_y)
        if center_x == 0 or center_y == 0:
            return 0
        row = self.current_img.shape[0]
        col = self.current_img.shape[1]
        channel =1
        mask = np.zeros([row, col, channel], dtype=np.uint8)
        cv2.circle(mask,(center_x,center_y),self.acneSize,(255,255,255),-1)
        new_img =cv2.inpaint(self.current_img, mask, 3, cv2.INPAINT_TELEA)
        self.current_img = new_img
        self.acne = False
        self.show_image()

    def acneSizeTest(self):
        if self.raw_image is None :
            self.ui.horizontalSlider_2.setValue(0)
            QMessageBox().information(self, "提示", "请先录入图像！", QMessageBox.Yes)
            return 0


    # 人脸识别
    def detect_face(self):
        img = self.current_img
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # 人脸分类器
        detector = dlib.get_frontal_face_detector()
        # 获取人脸检测器
        predictor = dlib.shape_predictor(
            "./face/shape_predictor_68_face_landmarks.dat"
        )
        dets = detector(gray, 1)
        for face in dets:
            # 在图片中标注人脸，并显示
            left = face.left()
            top = face.top()
            right = face.right()
            bottom = face.bottom()
            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.imshow("image", img)


    # 调用摄像头窗口
    def new_camera(self):
        Dialog = QtWidgets.QDialog()
        self.dialog = Dialog
        self.ui_2 = GetImgFromCamera.Ui_Form()
        self.ui_2.setupUi(Dialog)
        Dialog.show()
        self.ui_2.pushButton_2.clicked.connect(self.get_image)
        Dialog.exec_()
        if self.ui_2.cap.isOpened():
            self.ui_2.cap.release()
        if self.ui_2.timer_camera.isActive():
            self.ui_2.timer_camera.stop()

    # 获取摄像头的图片
    def get_image(self):
        if self.ui_2.image is not None:
            self.ui_2.captured_image = self.ui_2.image
            cv2.imwrite("testkk.jpg",self.ui_2.captured_image)
            self.raw_image = self.ui_2.captured_image
            self.current_img = self.ui_2.captured_image
            self.show_image()
            self.imgskin = np.zeros(self.raw_image.shape)
            self.intial_value()
            # QMessageBox().information(self, "提示", "图片录入成功！", QMessageBox.Yes)
            self.dialog.close()

        else:
            QMessageBox().information(self, "提示", "请先打开摄像头！", QMessageBox.Yes)
            self.dialog.raise_()
            print("ssss")


class CARscene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        super(CARscene, self).__init__(parent)
        self.x = 0
        self.y = 0

    def mousePressEvent(self, QMouseEvent):
        e = QMouseEvent.scenePos()
        e = e.toPoint()
        self.x = e.x()
        self.y = e.y()

    def mouseMoveEvent(self,QMouseEvent):
        self.QGraphicsScene.setMouseTracking(True)
        print("?")

    def enterEvent(self, QMouseEvent):
        print("123")


