import  cv2
import  numpy as np


def cr_otsu(image):
    """YCrCb颜色空间的Cr分量+Otsu阈值分割"""
    img = cv2.imread(image, cv2.IMREAD_COLOR)
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

    (y, cr, cb) = cv2.split(ycrcb)
    cr1 = cv2.GaussianBlur(cr, (5, 5), 0)
    _, skin = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.namedWindow("image raw", cv2.WINDOW_NORMAL)
    cv2.imshow("image raw", img)
    cv2.namedWindow("image CR", cv2.WINDOW_NORMAL)
    cv2.imshow("image CR", cr1)
    cv2.namedWindow("Skin Cr+OTSU", cv2.WINDOW_NORMAL)
    cv2.imshow("Skin Cr+OTSU", skin)

    dst = cv2.bitwise_and(img, img, mask=skin)
    cv2.namedWindow("seperate", cv2.WINDOW_NORMAL)

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

# cr_otsu("test05.jpg")
back0 = get_skin_yuv("me.jpg")
back0 = cv2.bilateralFilter(src=back0, d=10, sigmaColor=50, sigmaSpace=10)

cv2.imshow("what",back0)
lkk =  cv2.imread("me.jpg")
backans = np.zeros(lkk.shape,np.uint8)
(x, y,a) = back0.shape
print(a)
for k in range(a):
    for i in range(x):
        for j in range(y):
            # print(back0[i][j])
            if back0[i][j][k ]==0:
                backans[i][j][k ] = lkk[i][j][k ]
            else:
                backans[i][j][k ] = back0[i][j][k ]  # 这样做是为了让原图与滤波后的图合成时更准确
# ans = cv2.add(lkk,back0)
cv2.imshow("ans",backans)
cv2.waitKey(0)
