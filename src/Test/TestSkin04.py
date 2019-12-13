import cv2
import numpy as np
imname = "testbai02.jpg"
# 肤色检测之一: YCrCb之Cr分量 + OTSU二值化
def myGetSkin():
    img = cv2.imread(imname, cv2.IMREAD_COLOR)
    cv2.imshow("whatimg",img)
    oriimg = cv2.imread(imname)
    cv2.imshow("whatori",oriimg)
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb) # 把图像转换到YUV色域
    (y, cr, cb) = cv2.split(ycrcb) # 图像分割, 分别获取y, cr, br通道图像


    # 高斯滤波, cr 是待滤波的源图像数据, (5,5)是值窗口大小, 0 是指根据窗口大小来计算高斯函数标准差
    cr1 = cv2.GaussianBlur(cr, (5, 5), 0) # 对cr通道分量进行高斯滤波
    # 根据OTSU算法求图像阈值, 对图像进行二值化
    _, skin1 = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    backans = np.zeros(oriimg.shape,np.uint8)
    (x, y) = skin1.shape
    # for k in range(a):
    # for a in range(3):
    for i in range(x):
        for j in range(y):
            # print(back0[i,j])
            if skin1[i,j]!=0:
            #     backans[i][j][0]= 0
            #     backans[i][j][1]= 0
            #     backans[i][j][2]= 0
            # else:
                backans[i][j] = oriimg[i][j] # 这样做是为了让原图与滤波后的图合成时更准确
    return  backans

def Contrast_and_Brightness(alpha, beta, img):
    blank = np.zeros(img.shape, img.dtype)
    # dst = alpha * img + (1-alpha) * blank + beta
    dst = cv2.addWeighted(img, alpha, blank, 1 - alpha, beta)
    return dst
#
img = cv2.imread("testbai02.jpg")
cv2.imshow("ori",img)
back0 = myGetSkin()
print(back0[0][0])
cv2.imshow("what",back0)
back0 = Contrast_and_Brightness(1, 50, back0)
print(back0[0][0])
backans = np.zeros(img.shape,np.uint8)
(x, y,a) = back0.shape
print(a)
# for k in range(a):
for i in range(x):
    for j in range(y):
        # print(back0[i,j])
        if back0[i,j,0]==50 and back0[i,j,1]==50 and back0[i,j,2]==50:
            backans[i][j] = img[i][j]
        else:
            backans[i][j] = back0[i][j] # 这样做是为了让原图与滤波后的图合成时更准确
# ans = cv2.add(lkk,back0)
cv2.imshow("ans",backans)
cv2.waitKey(0)