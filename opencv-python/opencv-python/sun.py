import cv2 as cv
import cv2
import numpy  as np


img = cv.imread("./sun.jpg")

img1 = cv.imread("./sea.jpg")

#img2 = cv.imread("./time.jpg")

cv.imshow('img', img)

cv.imshow('img1', img1)
new1 = cv2.addWeighted(img, 0.5, img1, 0.5, 0)

new2 = cv2.add(img, img1)  # cv2.add():会把两个图片相加

new3 = img + img1
cv2.imshow("da", new1)
#cv2.imshow("er", new2)
cv2.imshow("s", new3)

cv2.waitKey(0)   # 等待指令
#  关闭所有窗口
cv2.destroyAllWindows()

