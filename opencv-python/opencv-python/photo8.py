import cv2 as cv


import numpy as np



def nothing(x):
    print('ok')


img = cv.imread('shape.png', cv.IMREAD_GRAYSCALE)
cv.namedWindow('canny')


cv.createTrackbar('th1', 'canny', 0, 255, nothing)
cv.createTrackbar('th2', 'canny', 0, 255, nothing)

while True:
    th1 = cv.getTrackbarPos('th1', 'canny')
    th2 = cv.getTrackbarPos('th2', 'canny')
    edges = cv.Canny(img, th1, th2)
    cv.imshow('canny', edges)
    k = cv.waitKey(25) & 0xff
    if chr(k) == 'q':
        break
cv.destroyAllWindows()








