"""
    图像处理主功能函数
"""
import math
import time

from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QGraphicsRectItem, QGraphicsScene, QMainWindow, \
    QMessageBox, QDialog
from PyQt5.QtGui import QPixmap, QImage, QMouseEvent, QCursor
import cv2
import numpy as np
from PyQt5.QtCore import pyqtSignal
import  ImgUi as window
import  AiMain
import  VideoMain
import GetImgFromCamera
import about
import colormap
import  pil
from PIL import ImageFilter, Image
from LogUpUi import LogUpUi

class LogUpMain(QMainWindow):


    def __init__(self):
        super(LogUpMain, self).__init__()
        self.ui =LogUpUi()
        self.ui.setupUi(self)



