# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:08:06 2019

@author: JEE-zhangjie
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np


# 寻找最大轮廓，传入的是一个二值的黑白图
def FindBigestContour(src):
    imax = 0
    imaxcontours = -1
    # 返回的是原图片，边界集合，轮廓的属性
    # image,\
    contours, hierarchy = cv2.findContours(src,
                                                  cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        itemp = cv2.contourArea(contours[i])
        if (imaxcontours < itemp):
            imaxcontours = itemp
            imax = i

    return contours[imax]


# 增强图像的对比度,输入的分别是图的对比度，最后是亮度,返回为转换后图片
def EnhanceSatutrtion(src, alpha, bright):
    blank = np.zeros_like(src, src.dtype)
    dst = cv2.addWeighted(src, alpha, blank, 1 - alpha, bright)
    #    dst=cv2.addWeighted(src,0.7,blank,0.3,0)#这样才能增加对比度
    return dst


def main():
    src= cv2.imread('testSKY04.jpg')
    # src = cv2.resize(src,(500,500))
    cloud= cv2.imread('sky.jpg')
    # cloud = cv2.resize(cloud,(500,500))

    # 1.背景天空分割
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)  # 转化为灰度图
    # Hue为色相，表示在色相环上的一种纯色，Saturation表示纯色在颜色
    # 中的百分比，S=1表示颜色最纯，最后一个是Value亮度，当V=0时，为黑色
    h, s, v = cv2.split(hsv)  # 将原图转化为hsv图，
    v = cv2.equalizeHist(v)
    mergeimg = cv2.merge([h, s, v])
    # 通过查表法确定蓝色的阀值
    minVal = np.array([100, 43, 46])
    maxVal = np.array([124, 255, 255])
    # 产生的是二值化的黑白图
    inRangimg = cv2.inRange(mergeimg, minVal, maxVal)
    kernel = np.ones([5, 5], np.uint8)  # 先定义一个卷积核
    #    cv2.dilate(imgdeal,kernel)
    imgdeal = cv2.dilate(cv2.erode(inRangimg, kernel), kernel)
    # cv2.imshow("/??",imgdeal)
    # cv2.waitKey(0)
    # mask = imgdeal.copy()
    ret, mask = cv2.threshold(imgdeal, 150, 255, cv2.THRESH_BINARY)
    notmask = cv2.bitwise_not(mask)
    frontpic = cv2.bitwise_and(src, src, mask=notmask)
    # 再融合,以1的结果mask，直接将云图拷贝过来（之前需要先做尺度变换）
    maxCountour = FindBigestContour(mask)
    # 返回的是（x,y,w,h）四个参数
    maxRect = cv2.boundingRect(maxCountour)
    #    if(maxRect.height==0||maxRect.width==0):
    #        maxRect=cv2.RECURS_FILTER
    matDst = src.copy()

    # cloud = cv2.resize(cloud, (maxRect[1], maxRect[0]))
    cloud = cv2.resize(cloud, (src.shape[1], src.shape[0]))

    # 要求为整数，所以传入不能带有小数
    center = (maxRect[2] // 2, maxRect[3] // 2)
    # Create an all white mask
    # 分别是目标影像，背景影像，目标影响上的mask，
    # 目标影像的中心在背景图像上的坐标！注意是目标影像的中心！
    # out_put = cv2.seamlessClone(cloud, src, mask, center, cv2.NORMAL_CLONE)
    # out_put = cv2.seamlessClone(cloud, src, mask, center, cv2.NORMAL_CLONE)
    cloud = cv2.bitwise_and(cloud, cloud, mask=mask)
    merge_img = cv2.add(cloud, frontpic)
    cv2.imshow("o",merge_img)
    cv2.imshow('output', EnhanceSatutrtion(merge_img, 1.1, 1.3))

    # temp = cv2.bilateralFilter(out_put.copy(), 5, 10.0, 2.0)
    # temp = cv2.cvtColor(temp, cv2.COLOR_BGR2YCrCb)
    # planes = cv2.split(temp)
    # planes[0] = cv2.equalizeHist(planes[0])
    # temp = cv2.merge(planes)
    # temp = cv2.cvtColor(temp, cv2.COLOR_YCrCb2BGR)
    #
    # matDst = EnhanceSatutrtion(temp, 1.1, 1.3)

    cv2.imshow('original', src)
    cv2.imshow('result', matDst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


main()
