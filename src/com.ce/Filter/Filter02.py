import cv2
img = cv2.imread("../img/test06.jpg", cv2.IMREAD_GRAYSCALE)
# gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("gray",img)
im_color = cv2.applyColorMap(img, cv2.COLORMAP_SUMMER)
cv2.imshow("test",im_color)

cv2.waitKey()