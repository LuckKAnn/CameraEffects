import cv2
import  numpy as np
def grab_cut(sourceDir):
            # 读取图片
            img = cv2.imread(sourceDir)
            # 图片宽度
            img_x = img.shape[1]
            # 图片高度
            img_y = img.shape[0]
            # 分割的矩形区域
            rect = (0,503, 1000, 1491)
            # 背景模式,必须为1行,13x5列
            bgModel = np.zeros((1, 65), np.float64)
            # 前景模式,必须为1行,13x5列
            fgModel = np.zeros((1, 65), np.float64)
            # 图像掩模,取值有0,1,2,3
            mask = np.zeros(img.shape[:2], np.uint8)
            # grabCut处理,GC_INIT_WITH_RECT模式
            cv2.grabCut(img, mask, rect, bgModel, fgModel, 5, cv2.GC_INIT_WITH_RECT)
            # 将背景0,2设成0,其余设成1
            mask2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
            # 重新计算图像着色,对应元素相乘
            img = img*mask2[:, :, np.newaxis]
            cv2.namedWindow("Result",0)
            cv2.imshow("Result", img)
            cv2.waitKey(0)


sourceDir = "me.jpg"
grab_cut(sourceDir)
