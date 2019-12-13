import  cv2
import  numpy as np
"""
对我们的皮肤抠图back0单独滤波，这样可以保证背景不在转换过程中失真。最后要与原图合起来
"""
def get_skin_yuv(img):
    img = cv2.imread(img)
    ycrcb_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    (y, cr, cb) = cv2.split(ycrcb_img)
    (x, y) = cr.shape
    back = np.zeros(img.shape, np.uint8)
    for i in range(x):
        for j in range(y):
            if (cr[i][j] > 133) and (cr[i][j] < 173) and (cb[i][j] > 77) and (cb[i][j] < 127):
                back[i][j]=img[i][j]
                img[i][j]=0      #这样做是为了让原图与滤波后的图合成时更准确
    # cv2.imshow("kk",back)
    # cv2.waitKey(0)
    return  back

img = cv2.imread("test05.jpg")
img0 = np.zeros(img.shape, np.uint8)
infmg_1 = np.zeros(img.shape, np.uint8)
infmg_2 = np.zeros(img.shape, np.uint8)
infmg_3 = np.zeros(img.shape, np.uint8)
infmg_4 = np.zeros(img.shape, np.uint8)
back0 =get_skin_yuv("test05.jpg")
while (1):
    key = cv2.waitKey(1)
    if key > 0:
        break
    a = 0
    b= 0
    c = 0
    a2 =10
    b2 = 1
    c2 = 1
    if a2 != a or b2 != b or c2 != c:
        cv2.bilateralFilter(back0, a, b, c, infmg_1)
        a, b, c = a2, b2, c2
        dst1 = infmg_1 - back0 + 128
        # cv2.imshow("双边滤波", dst1)
        infmg_2 = cv2.GaussianBlur(dst1, (1, 1), 0, 0)
        infmg_3 = back0 + 2 * infmg_2 - 255
        # cv2.imshow("高斯滤波", infmg_3)
        infmg_4 = cv2.addWeighted(back0, 0.2, infmg_3, 0.8, 0)
        img0 = cv2.add(img, infmg_4)  # img是原图，infmg_4是最终滤波的结果
        cv2.imshow("美颜结果", img0)

cv2.imwrite("美颜结果.jpg", img0)
while 1:
    key = cv2.waitKey(1)
    if key > 0:
        break
cv2.destroyAllWindows()
