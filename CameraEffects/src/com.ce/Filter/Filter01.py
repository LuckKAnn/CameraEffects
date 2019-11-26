import cv2
import numpy as np
import math

def Filter_Tutoujing(src_img):   #凸透镜

    row=src_img.shape[0]
    col=src_img.shape[1]
    channel=src_img.shape[2]
    new_img=np.zeros([row,col,channel],dtype=np.uint8)
    center_x=row/2
    center_y=col/2
    # radius=math.sqrt(center_x*center_x+center_y*center_y)/2
    radius = min(center_x,center_y)
    for i in range(row):
        for j in range(col):

            distance=((i-center_x)*(i-center_x)+(j-center_y)*(j-center_y))
            new_dist=math.sqrt(distance)
            new_img[i,j,:]=src_img[i,j,:]
            if distance<=radius**2:
                new_i=np.int(np.floor(new_dist*(i-center_x)/radius+center_x))
                new_j=np.int(np.floor(new_dist*(j-center_y)/radius+center_y))
                new_img[i,j,:]=src_img[new_i,new_j,:]
    return new_img

src_img_name='../img/test06.jpg'
src_img=cv2.imread(src_img_name)
new_img=Filter_Tutoujing(src_img)
cv2.imshow('src',src_img)
cv2.imshow('tutoujing',new_img)
cv2.waitKey()
