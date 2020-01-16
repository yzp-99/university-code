import cv2 as cv
import numpy as np

img = np.ones((300, 500, 3), np.uint8) * 127



def nothing(x):
    pass

cv.namedWindow('image')
#  创建滑动条

cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)

# cv.circle('image', 55), 10, (255, 255, 255), 3, cv.LINE_AA)
switch = '0:OFF\n1:ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)
while True:

    R = cv.getTrackbarPos('R', 'image')
    G = cv.getTrackbarPos('G', 'image')
    B = cv.getTrackbarPos('B', 'image')
    img[:] = [B, G, R]
    cv.imshow('image', img)

    k = cv.waitKey(25) & 0xFF
    if chr(k) == 'q':
        break
cv.destroyWindow('image')


