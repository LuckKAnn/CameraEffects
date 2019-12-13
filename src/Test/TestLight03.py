import  cv2
import  numpy as np

def get_skin_yuv(img):
    # img = cv2.imread(img)
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

def Contrast_and_Brightness(alpha, beta, img):
    blank = np.zeros(img.shape, img.dtype)
    # dst = alpha * img + (1-alpha) * blank + beta
    dst = cv2.addWeighted(img, alpha, blank, 1 - alpha, beta)
    return dst

img = cv2.imread("testbai02.jpg")
cv2.imshow("ori",img)
back0 = get_skin_yuv(img)
print(back0[0][0])
cv2.imshow("what",back0)
# back0 = cv2.bilateralFilter(src=back0, d=10, sigmaColor=50, sigmaSpace=10)
back0 = Contrast_and_Brightness(1, 50, back0)
print(back0[0][0])
# back0 = get_skin_yuv(back0)
# cv2.imshow("what2",back0)
#
# img  = cv2.imread("me.jpg")
# cv2.imshow("origin",img)
#
# cv2.imshow("after",frame1)
lkk =  cv2.imread("testbai02.jpg")
backans = np.zeros(lkk.shape,np.uint8)
(x, y,a) = back0.shape
print(a)
# for k in range(a):
for i in range(x):
    for j in range(y):
        # print(back0[i,j])
        if back0[i,j,0]==50 and back0[i,j,1]==50 and back0[i,j,2]==50:
            backans[i][j] = lkk[i][j]
        else:
            backans[i][j] = back0[i][j] # 这样做是为了让原图与滤波后的图合成时更准确
# ans = cv2.add(lkk,back0)
cv2.imshow("ans",backans)
cv2.waitKey(0)

