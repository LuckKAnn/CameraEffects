# -*-coding: utf-8 -*-
"""
    @Project: IntelligentManufacture
    @File   : user_interaction.py
    @Author : panjq
    @E-mail : pan_jinquan@163.com
    @Date   : 2019-02-21 15:03:18
"""
# -*- coding: utf-8 -*-

import cv2
import image_processing
import numpy as np

global img
global point1, point2
global g_rect


def on_mouse(event, x, y, flags, param):
    global img, point1, point2, g_rect
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击,则在原图打点
        print("1-EVENT_LBUTTONDOWN")
        point1 = (x, y)
        cv2.circle(img2, point1, 10, (0, 255, 0), 5)
        cv2.imshow('image', img2)

    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):  # 按住左键拖曳，画框
        print("2-EVENT_FLAG_LBUTTON")
        cv2.rectangle(img2, point1, (x, y), (255, 0, 0), thickness=2)
        cv2.imshow('image', img2)

    elif event == cv2.EVENT_LBUTTONUP:  # 左键释放，显示
        print("3-EVENT_LBUTTONUP")
        point2 = (x, y)
        cv2.rectangle(img2, point1, point2, (0, 0, 255), thickness=2)
        cv2.imshow('image', img2)
        if point1 != point2:
            min_x = min(point1[0], point2[0])
            min_y = min(point1[1], point2[1])
            width = abs(point1[0] - point2[0])
            height = abs(point1[1] - point2[1])
            g_rect = [min_x, min_y, width, height]
            cut_img = img[min_y:min_y + height, min_x:min_x + width]
            cv2.imshow('ROI', cut_img)


def get_image_roi(rgb_image):
    '''
    获得用户ROI区域的rect=[x,y,w,h]
    :param rgb_image:
    :return:
    '''
    bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
    global img
    img = bgr_image
    cv2.namedWindow('image')
    while True:
        cv2.setMouseCallback('image', on_mouse)
        # cv2.startWindowThread()  # 加在这个位置
        cv2.imshow('image', img)
        key = cv2.waitKey(0)
        if key == 13 or key == 32:  # 按空格和回车键退出
            break
    cv2.destroyAllWindows()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return g_rect


def select_user_roi(image_path):
    '''
    由于原图的分辨率较大，这里缩小后获取ROI，返回时需要重新scale对应原图
    :param image_path:
    :return:
    '''
    orig_image = image_processing.read_image(image_path)
    orig_shape = np.shape(orig_image)
    resize_image = image_processing.resize_image(orig_image, resize_height=800, resize_width=None)
    re_shape = np.shape(resize_image)
    g_rect = get_image_roi(resize_image)
    orgi_rect = image_processing.scale_rect(g_rect, re_shape, orig_shape)
    roi_image = image_processing.get_rect_image(orig_image, orgi_rect)
    image_processing.cv_show_image("RECT", roi_image)
    image_processing.show_image_rect("image", orig_image, orgi_rect)
    return orgi_rect


if __name__ == '__main__':
    # image_path="../dataset/images/IMG_0007.JPG"
    image_path = "testSKY05.jpg"

    # rect=get_image_roi(image)
    rect = select_user_roi(image_path)
    print(rect)
