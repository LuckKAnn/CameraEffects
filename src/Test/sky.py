import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

imgname = 'msu1'
# img = cv2.imread('./{}.png'.format(imgname))
img = cv2.imread("testSKY04.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

lapl = cv2.Laplacian(img[:,:,0], cv2.CV_64F, ksize=3)
# cv2.imwrite('./{}_lapl.png'.format(imgname), lapl)

y0 = 219.5
u0 = 17.5+128
v0 = -17.9+128
dy = 40.0
du = 40.0
dv = 40.0

Pcol = np.zeros(lapl.shape)
Ppos = np.zeros(lapl.shape)

rows, cols = lapl.shape
for i in range(rows):
	for j in range(cols):
		Pcol.itemset((i,j), math.exp(-((img[i,j,0]-y0)/dy)**2 - ((img[i,j,1]-u0)/du)**2 - ((img[i,j,2]-v0)/dv)**2) )

# cv2.imwrite('./{}_pcol.png'.format(imgname), Pcol*255)

for i in range(rows):
	Ppos[i,:] = math.exp(-(i/float(rows+1))**2)

# cv2.imwrite('./{}_ppos.png'.format(imgname), Ppos*255)

# cv2.imwrite('./{}_col+pos.png'.format(imgname), Ppos*Pcol*255)

abslapl = abs(lapl)
abslapl = (abslapl.max()-abslapl)/abslapl.max()
# cv2.imwrite('./{}_lapl_abs.png'.format(imgname), abslapl*255)

# cv2.imwrite('./{}_col+pos+abslapl.png'.format(imgname), Ppos*Pcol*abslapl*255)

res = Ppos*Pcol*abslapl*255
ret, res1 = cv2.threshold(res, 90, 255, cv2.THRESH_BINARY)

# cv2.imwrite('./{}_skymap.png'.format(imgname), res1)

cv2.imshow('seesee',res1)
cv2.waitKey(0)




















