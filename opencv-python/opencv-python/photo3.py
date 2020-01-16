import cv2 as cv
import cv2
import numpy as np

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # 椭圆结构

img = cv2.imread('fushi.png', 0)
img = cv.resize(img, (200, 300))
kernel1 = np.ones((5, 5), np.uint8)

erosion = cv2.erode(img, kernel)  # 腐蚀
#opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)  # 开运算
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 矩形结构

# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))  # 十字形结构

dilation = cv2.dilate(img, kernel)  # 膨胀

img2 = erosion

img3 = dilation


cv.imshow('src', img)
cv.imshow('shi', img2)
cv.imshow('fat', img3)
cv.waitKey(0)
cv.destroyAllWindows()