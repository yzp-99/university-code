import cv2 as cv
import cv2
img_src = cv.imread('color.jpg')

hsv_src = cv.cvtColor(img_src, cv.COLOR_BGR2HSV)


red_lod_hsv = (10, 43, 46)
red_high_hsv = (180, 255, 255)

mask_red = cv.inRange(hsv_src, red_lod_hsv, red_high_hsv)


cv.imshow('src', img_src)
cv.imshow('mask_red', mask_red)
cv.waitKey(0)
cv.destroyAllWindows()













