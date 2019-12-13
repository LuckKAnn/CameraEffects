import cv2
import numpy as np

img = cv2.imread("me.jpg", 0)
canny = cv2.Canny(img, 0, 152)
# cv2.imwrite("canny.jp", cv2.Canny(img, 200, 300))
cv2.namedWindow("canny",0)
cv2.imshow("canny", canny)
cv2.waitKey()
cv2.destroyAllWindows()
