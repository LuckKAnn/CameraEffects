# 调用摄像头实时单个/多个人脸检测，并依次在摄像头窗口，实时平铺显示检测到的人脸；

import dlib
import cv2
import time
import  numpy as np


def acne(roi):
    deep = 10
    # roi = face_trace()
    # blur = cv2.bilateralFilter(self.raw_image,deep,100,15)
    # blur = cv2.bilateralFilter(self.image, deep * 5, 100, 15)
    blur = cv2.bilateralFilter(roi, deep * 5, 100, 15)
    # cv2.imshow("no rui",blur)
    # 模糊之后再进行锐化
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]], np.float32)
    dst = cv2.filter2D(blur, -1, kernel=kernel)
    return  dst
    # self.image = dst

def face_trace():
    # 储存截图的目录
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    # 创建 cv2 摄像头对象
    cap = cv2.VideoCapture("./BeautyCamera02/video/vid.avi")
    # cap = cv2.VideoCapture(0)

    # 设置视频参数，propId 设置的视频参数，value 设置的参数值
    cap.set(60, 960)

    # 截图 screenshots 的计数器
    ss_cnt = 0

    while cap.isOpened():
        flag, img_rd = cap.read()
        # 每帧数据延时 1ms，延时为 0 读取的是静态帧
        k = cv2.waitKey(1)

        # 取灰度
        img_gray = cv2.cvtColor(img_rd, cv2.COLOR_RGB2GRAY)

        # 人脸数
        faces = detector(img_gray, 0)
        if len(faces) != 0:
            # 记录每次开始写入人脸像素的宽度位置
            faces_start_width = 0
            for face in faces:
                # 绘制矩形框
                cv2.rectangle(img_rd, tuple([face.left(), face.top()]), tuple([face.right(), face.bottom()]),
                              (0, 255, 255), 2)
                print(face.left())
                print(face.top())
                print(face.right())
                print(face.bottom())
                ROI = img_rd[face.top():face.bottom(),face.left(): face.right()]
                # cv2.imshow("ROU", ROI)
                dst = acne(ROI)
                img_rd[face.top():face.bottom(), face.left(): face.right()] = dst
                # cv2.imshow("ROU", img_rd)
                # cv2.waitKey(0)

        cv2.namedWindow("camera", 1)
        cv2.imshow("camera", img_rd)
        # cv2.waitKey(0)

    # 释放摄像头
    cap.release()

    # 删除建立的窗口
    cv2.destroyAllWindows()

face_trace()