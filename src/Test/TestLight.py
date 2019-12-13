import  cv2
import  numpy as np

img = cv2.imread("me.jpg")
cv2.imshow("what",img)
ans = np.zeros(img.shape,np.uint8)
(x, y,a) = img.shape
for k in range(a):
    for i in range(x):
        for j in range(y):
            # print(back0[i][j])
            if img[i][j][k]+20<255:
                ans[i][j][k] = img[i][j][k]+20
            elif img[i][j][k]+10<255:
                ans[i][j][k] = img[i][j][k]+10
            else:
                ans[i][j][k] = img[i][j][k]

# ans = cv2.add(lkk,back0)
cv2.imshow("ans",ans)
cv2.waitKey(0)
