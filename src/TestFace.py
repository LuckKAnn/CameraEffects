##  face_detetor_1.py  比原来代码略有改动
import dlib
from skimage import io

# 使用特征提取器frontal_face_detector
detector = dlib.get_frontal_face_detector()

# path是图片所在路径
path = "./Test/"
img = io.imread(path + "testkk.jpg")

# 特征提取器的实例化
dets = detector(img)

print("人脸数：", len(dets))

# 输出人脸矩形的四个坐标点
for i, d in enumerate(dets):
    print("第", i, "个人脸d的坐标：",
          "left:", d.left(),
          "right:", d.right(),
          "top:", d.top(),
          "bottom:", d.bottom())

# 绘制图片
win = dlib.image_window()
# 清除覆盖
# win.clear_overlay()
win.set_image(img)
# 将生成的矩阵覆盖上
win.add_overlay(dets)
# 保持图像
dlib.hit_enter_to_continue()
