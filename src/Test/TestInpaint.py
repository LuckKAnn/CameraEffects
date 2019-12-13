import cv2

img = cv2.imread('testkk.jpg')
mask = cv2.imread('mask.png', 0)

cv2.imshow('img', img)
cv2.imshow('mask', mask)

dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
cv2.imshow('1', dst)

dst2 = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)
cv2.imshow('2', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()
