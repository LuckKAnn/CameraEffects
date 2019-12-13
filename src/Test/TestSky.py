import cv2
import numpy as np
import math


def skyRegion1(picname):
    iLow = np.array([100, 43, 46])
    iHigh = np.array([124, 255, 255])
    img = cv2.imread(picname)
    imgOriginal = cv2.imread(picname)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # hsv split
    h, s, v = cv2.split(img)
    cv2.equalizeHist(v)
    hsv = cv2.merge((h, s, v))
    imgThresholded = cv2.inRange(hsv, iLow, iHigh)
    cv2.imshow("aaa",imgThresholded)
    imgThresholded = cv2.medianBlur(imgThresholded, 9)
    cv2.imshow("bbb",imgThresholded)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
    Erode_img = cv2.erode(imgThresholded, kernel)
    Dilation_img = cv2.dilate(Erode_img, kernel)
    # print(tmp)
    cv2.imshow("xx",Dilation_img)
    # open
    kernel = np.ones((5, 5), np.uint8)
    imgThresholded = cv2.morphologyEx(imgThresholded, cv2.MORPH_OPEN, kernel, iterations=10)
    imgThresholded = cv2.medianBlur(imgThresholded, 9)
    cv2.imshow("??", imgThresholded)
    # notmask = cv2.bitwise_not(imgThresholded)
    # cv2.imshow("notmask", notmask)
    # cv2.waitKey(0)
    # cv2.imwrite(tmp, imgThresholded)
    # return tmp
    return imgThresholded

def Segment(src, sky_img):
    # hsv_img = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    # planes = cv2.split(hsv_img)
    # planes[2] = cv2.equalizeHist(planes[2])
    # mer_img = cv2.merge(planes)
    #
    # lower_red = np.array([100, 43, 46])
    # upper_red = np.array([124, 255, 255])
    # range_img = cv2.inRange(mer_img, lower_red, upper_red)
    #
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
    # Erode_img = cv2.erode(range_img, kernel)
    # Dilation_img = cv2.dilate(Erode_img, kernel)
    # # cv2.imshow("??",Dilation_img)
    # ret, mask = cv2.threshold(Dilation_img, 150, 255, cv2.THRESH_BINARY)
    # cv2.imshow("mask",mask)
    mask = skyRegion1("testSKY05.jpg")
    notmask = cv2.bitwise_not(mask)
    cv2.imshow("notmask",notmask)
    frontpic = cv2.bitwise_and(src, src, mask=notmask)

    sky_resize = cv2.resize(sky_img, (src.shape[1], src.shape[0]))
    backimage = cv2.bitwise_and(sky_resize, sky_resize, mask=mask)
    merge_img = cv2.add(backimage, frontpic)
    return merge_img


src_img = cv2.imread('testSKY05.jpg')
sky_img = cv2.imread('sky.jpg')
merge_img = Segment(src_img, sky_img)

cv2.imshow('src', src_img)
cv2.imshow('new_img', merge_img)
cv2.waitKey()
