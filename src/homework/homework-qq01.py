import cv2


img = cv2.imread('me.jpg', 0)
ret, thresh1 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)  # binary （黑白二值）
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)  # （黑白二值反转）
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)  # 得到的图像为多像素值
ret, thresh4 = cv2.threshold(img, 150, 255, cv2.THRESH_TOZERO)  # 高于阈值时像素设置为255，低于阈值时不作处理
ret, thresh5 = cv2.threshold(img, 180, 255, cv2.THRESH_TOZERO_INV)  # 低于阈值时设置为255，高于阈值时不作处理

print(ret)
cv2.namedWindow('thresh2',0)
cv2.imshow('thresh2', thresh4)
# cv2.imshow('thresh2', thresh2)
# cv2.imshow('thresh3', thresh3)
# cv2.imshow('thresh4', thresh4)
# cv2.imshow('thresh5', thresh5)
# cv2.imshow('grey-map', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
