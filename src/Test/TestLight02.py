# -*- coding: utf-8 -*-
import numpy as np
import cv2


def Contrast_and_Brightness(alpha, beta, img):
    blank = np.zeros(img.shape, img.dtype)
    # dst = alpha * img + (1-alpha) * blank + beta
    dst = cv2.addWeighted(img, alpha, blank, 1 - alpha, beta)
    return dst


cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()  ##ret返回布尔量
    cv2.imshow('frame', frame)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame1 = Contrast_and_Brightness(1, 100, frame)

    cv2.imshow('frame1', frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
