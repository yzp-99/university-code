# -*- coding: utf-8 -*-
import cv2

image = cv2.imread('lightning.png')
src = image
image = cv2.resize(image, (500, 600))
k = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 灰度化
#image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # 二值化
cv2.threshold(image, 130, 255, 0, image)

cv2.namedWindow("Image")
cv2.imshow("Image", image)
cv2.imshow('src', src)
cv2.imshow('k', k)
cv2.waitKey(0)
cv2.destroyAllWindows()
