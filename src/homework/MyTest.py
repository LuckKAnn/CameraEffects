import numpy as np
import cv2
from matplotlib import pyplot as plt

imgpath = 'me.jpg'
img = cv2.imread(imgpath)

# 预先绘制图片
fig = plt.figure()
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(122), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.colorbar()
plt.show()


def OnClick(event):
    # 获取当鼠标"按下"的时候，鼠标的位置
    global Coords1x, Coords1y
    if event.button == 1:
        Coords1x = int(event.xdata)
        Coords1y = int(event.ydata)
        # print("1x1y" + str(Coords1x) + str(Coords1y))


def OnMouseMotion(event):
    # 获取当鼠标"移动"的时候，鼠标的位置
    global Coords2x, Coords2y
    if event.button == 1:
        Coords2x = int(event.xdata)
        Coords2y = int(event.ydata)
        # print("2x2y" + str(Coords2x) + str(Coords2y))


def OnMouseRelease(event):
    if event.button == 1:
        fig = plt.gca()
        img = cv2.imread(imgpath)
        # 创建一个与所加载图像同形状的Mask
        mask = np.zeros(img.shape[:2], np.uint8)

        # 算法内部使用的数组,你必须创建两个np.float64 类型的0数组,大小是(1, 65)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)

        # 计算人工前景的矩形区域(rect.x,rect.y,rect.width,rect.height)
        rect = (Coords1x, Coords1y, Coords2x - Coords1x, Coords2y - Coords1y)
        print(rect)
        iterCount = 5
        cv2.grabCut(img, mask, rect, bgdModel, fgdModel, iterCount, cv2.GC_INIT_WITH_RECT)

        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        img = img * mask2[:, :, np.newaxis]
        plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.subplot(122), plt.imshow(
            cv2.cvtColor(cv2.imread(imgpath), cv2.COLOR_BGR2RGB))
        fig.figure.canvas.draw()


# 连接鼠标点击事件
fig.canvas.mpl_connect('button_press_event', OnClick)
# 连接鼠标移动事件
fig.canvas.mpl_connect('motion_notify_event', OnMouseMotion)
fig.canvas.mpl_connect('button_release_event', OnMouseRelease)
