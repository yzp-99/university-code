import cv2 as cv
import numpy as np

# 边缘轮廓检测

def nothing1(x):
    pass

def nothing2(x):
    print('你好')


cv.namedWindow('Sobel x')
cv.namedWindow('Sobel y')

cv.createTrackbar('xsize', 'Sobel x', 1, 15, nothing1)
cv.createTrackbar('ysize', 'Sobel y', 1, 15, nothing2)

img = cv.imread('shape.png', cv.IMREAD_GRAYSCALE)

cv.imshow('src', img)

while True:
    kx = cv.getTrackbarPos('xsize', 'Sobel x')
    ky = cv.getTrackbarPos('ysize', 'Sobel y')

    if (kx % 2) == 0:
        kx += 1
    if (ky % 2) == 0:
        ky += 1


    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=kx)

    sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=ky)


    sobelx = cv.convertScaleAbs(sobelx)
    sobely = cv.convertScaleAbs(sobely)


    sobel_xy = cv.addWeighted(sobelx, .5, sobely, .5, 0)

    k = cv.waitKey(25) & 0xFF
    if chr(k) == 'q':
        break
    cv.imshow('Sobel x', sobelx)
    cv.imshow('Sobel y', sobely)
    cv.imshow('sobel_xy', sobel_xy)

cv.destroyAllWindows()






















