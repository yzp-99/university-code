
import cv2
import numpy as np

#import matplotlib.pyplot as plt

# 加载图像
img1 = cv2.imread('cat.jpg', 1)

#  颜色空间变换 cv2.cvtColor() cv2.inRange()

cv2.imshow('RGB', img1)
img3 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
img4 = cv2.cvtColor(img1, cv2.COLOR_RGB2HSV)
img5 = cv2.cvtColor(img1, cv2.COLOR_RGB2LAB)
img6 = cv2.cvtColor(img1, cv2.COLOR_RGB2XYZ)
img7 = cv2.cvtColor(img1, cv2.COLOR_RGB2HLS)

cv2.imshow('GRAY', img3)
cv2.imshow('HSV', img4)
cv2.imshow('LAB', img5)
cv2.imshow('XYZ', img6)
cv2.imshow('HLS', img7)
cv2.waitKey(0)

cv2.destroyAllWindows()