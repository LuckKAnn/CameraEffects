#!/bin/python
# 祛痘美白

import numpy as np
import cv2


def beauty_face(img):
    '''
    Dest =(Src * (100 - Opacity) + (Src + 2 * GuassBlur(EPFFilter(Src) - Src + 128) - 256) * Opacity) /100 ;
    https://my.oschina.net/wujux/blog/1563461
    '''

    dst = np.zeros_like(img)
    # int value1 = 3, value2 = 1; 磨皮程度与细节程度的确定
    v1 = 3
    v2 = 1
    dx = v1 * 5  # 双边滤波参数之一
    fc = v1 * 12.5  # 双边滤波参数之一
    p = 0.1

    temp4 = np.zeros_like(img)

    temp1 = cv2.bilateralFilter(img, dx, fc, fc)
    temp2 = cv2.subtract(temp1, img)
    temp2 = cv2.add(temp2, (10, 10, 10, 128))
    temp3 = cv2.GaussianBlur(temp2, (2 * v2 - 1, 2 * v2 - 1), 0)
    temp4 = cv2.add(img, temp3)
    dst = cv2.addWeighted(img, p, temp4, 1 - p, 0.0)
    dst = cv2.add(dst, (10, 10, 10, 255))
    return dst


def beauty_face2(src):
    '''
    Dest =(Src * (100 - Opacity) + (Src + 2 * GuassBlur(EPFFilter(Src) - Src + 128) - 256) * Opacity) /100 ;
    '''

    dst = np.zeros_like(src)
    # int value1 = 3, value2 = 1; 磨皮程度与细节程度的确定
    v1 = 3
    v2 = 1
    dx = v1 * 5  # 双边滤波参数之一
    fc = v1 * 12.5  # 双边滤波参数之一
    p = 0.1

    temp4 = np.zeros_like(src)

    temp1 = cv2.bilateralFilter(src, dx, fc, fc)
    temp2 = cv2.subtract(temp1, src)
    temp2 = cv2.add(temp2, (10, 10, 10, 128))
    temp3 = cv2.GaussianBlur(temp2, (2 * v2 - 1, 2 * v2 - 1), 0)
    temp4 = cv2.subtract(cv2.add(cv2.add(temp3, temp3), src), (10, 10, 10, 255))

    dst = cv2.addWeighted(src, p, temp4, 1 - p, 0.0)
    dst = cv2.add(dst, (10, 10, 10, 255))
    return dst


def init():
    img = cv2.imread('testSKY05.jpg')

    # blur1 = cv2.GaussianBlur(img, (5,5),0)
    # blur2 = cv2.bilateralFilter(img, 9 , 75, 75)
    blur3 = beauty_face(img)
    blur4 = beauty_face2(img)

    cv2.imshow('image0', img)
    # cv2.imshow('image1', blur1)
    # cv2.imshow('image2', blur2)
    cv2.imshow('image3', blur3)
    cv2.imshow('image4', blur4)

    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('image', 1000, 1000) #定义frame的大小

    cv2.waitKey(0)
    # cv2.imwrite('result1.png', blur3)
    # cv2.imwrite('result2.png', blur4)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    init()