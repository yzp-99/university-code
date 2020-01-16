import cv2 as cv

img = cv.imread('forCLA.png', cv.IMREAD_GRAYSCALE)

img1 = cv.equalizeHist(img)

cv.imshow('src', img)  # 原图

cv.imshow('dst', img1)  # 均衡化后的图


cv.waitKey(0)
cv.destroyAllWindows()










