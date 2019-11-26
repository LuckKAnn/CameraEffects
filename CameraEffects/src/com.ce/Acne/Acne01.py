import numpy as np
import cv2

img = cv2.imread('1.png') #原图
mask = cv2.imread('r.png',0) #掩码

dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()