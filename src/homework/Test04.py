#!/usr/bin/python
# -*- coding: utf-8 -*-
# !/usr/bin/python
import dlib  # 人脸识别库
import numpy as np  # 数据处理库
import cv2  # 图像处理库

detector = dlib.get_frontal_face_detector()  # 与人脸检测相同，使用dlib自带的frontal_face_detector作为人脸检测器

# predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')  # 使用官方提供的模型构建特征提取器

# 读取图像
img = cv2.imread("qi.jpg")
dets = detector(img)
print("人脸数", len(dets))
height_max = 0
width_sum = 0

# 计算要生成的图像img_blank大小
for k, d in enumerate(dets):
    height = d.bottom() - d.top()
    width = d.right() - d.left()

    width_sum += width

    if height > height_max:
        height_max = height
    else:
        height_max = height_max

print("img_blank的大小：")
print("高度", height_max, "宽度", width_sum)

img_blank = np.zeros((height_max+150, width_sum+150, 3), np.uint8)

blank_start = 0

for k, d in enumerate(dets):
    height = d.bottom() - d.top()+150
    width = d.right() - d.left()+150

    for i in range(height):
        for j in range(width):
            img_blank[i][blank_start + j] = img[d.top() + i-150][d.left() +0+ j]

    blank_start += width

cv2.namedWindow("img_faces", 0)
cv2.imwrite("testqi.jpg",img_blank)
cv2.imshow("img_faces", img_blank)
# cv2.imwrite("img_new.jpg", img_blank)
cv2.waitKey(0)