import cv2
import numpy as np

def skyRegion1(picname) :
        iLow = np.array([100,43,46])
        iHigh = np.array( [124,255 ,255])
        img=cv2.imread( picname )
        imgOriginal = cv2.imread(picname)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        #hsv split
        h,s,v = cv2.split(img)
        cv2.equalizeHist(v)
        hsv = cv2.merge((h,s,v))
        imgThresholded = cv2.inRange(hsv, iLow, iHigh)
        imgThresholded = cv2.medianBlur( imgThresholded,9)
        #open
        kernel = np. ones((5,5),np. uint8)
        imgThresholded = cv2.morphologyEx( imgThresholded , cv2. MORPH_OPEN, kernel, iterations = 10)
        imgThresholded = cv2.medianBlur( imgThresholded,9)
        pic_name = picname.split('/')[-1].split('.')[0]
        # tmp = "tmp/"+pic_name+"-mask.jpg"
        # print(tmp)
        cv2.imshow("??",imgThresholded)
        notmask = cv2.bitwise_not(imgThresholded)
        cv2.imshow("notmask",notmask)
        cv2.waitKey(0)
        # cv2.imwrite(tmp, imgThresholded)
        # return tmp
        return imgThresholded

def seamClone(skyname, picname, maskname):
        # Read images
        src = cv2.imread( skyname) #sky
        dst = cv2.imread( picname)
        src_mask = cv2.imread( maskname,0)
        src_mask0 = cv2.imread( maskname)
        contours, hierarchy  = cv2.findContours(src_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnt = contours[0]
        x,y,w,h=cv2.boundingRect(cnt)
        if w==0 or h==0 :
             return dst
        dst_x = len(dst[0])
        dst_y = len(dst[1])
        src_x = len(src[0])
        src_y = len(src[1])
        scale_X = w*1.0/src_x
        # src = cv2. resize(src, (100, dshape), interpolation= cv2. INTERCUBIC)
        center =((x+w)//2, (y+h)//2)
        # Clone seamlessly .
        output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)
        # Save result
        c
        return output

mask = skyRegion1("testSKY04.jpg")
print(mask)
try:
        img=seamClone("sky.jpg","testSKY04.jpg",mask)
        cv2.imshow("src_sky", img)
        cv2.waitKey(0)
except Exception as e :
        print(e)

