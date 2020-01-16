import cv2 as cv
import numpy as np

img = np.zeros((500, 500, 3), np.uint8)

#  绘制圆形
cv.circle(img, (255, 255), 50, (255, 0, 0), 3)
cv.circle(img, (255, 255), 100, (255, 255, 255), 3, cv.LINE_AA)
cv.circle(img, (255, 255), 150, (0, 255, 255), 3)
#  画线
cv.line(img, (255, 255), (255 + 50, 255), (0, 0, 255), 3)
cv.line(img, (255, 255), (255, 255 + 100), (0, 0, 255), 3)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()













