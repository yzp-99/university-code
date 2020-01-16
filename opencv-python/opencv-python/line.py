import cv2 as cv
import numpy as np
#  创建一幅背景为纯黑色图片
img = np.zeros((500, 500, 3), np.uint8)
#  创建一幅纯白图片
img1 = np.ones((500, 500, 3), np.uint8) * 255


#  绘制线段
cv.line(img, (0, 0), (499, 499), (0, 0, 255), 5, cv.LINE_AA)

#  显示这张图像
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyWindow('img')

#  绘制一个多边形
triangle = [(255, 200), (200, 300), (300, 300)]

# 绘制三角形
cv.line(img1, triangle[0], triangle[1], (0, 255, 0), 5, cv.LINE_AA)
cv.line(img1, triangle[1], triangle[2], (0, 255, 0), 5, cv.LINE_AA)
cv.line(img1, triangle[2], triangle[0], (0, 255, 0), 5, cv.LINE_AA)

cv.imshow('img1', img1)
cv.waitKey(0)
cv.destroyWindow('img1')


