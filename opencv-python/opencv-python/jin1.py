import cv2 as cv

img1 = cv.imread('jinzi.jpg')

img_small = cv.pyrDown(img1)


img_small1 = cv.pyrDown(img_small)



cv.imshow('img1', img1)
cv.imshow('small', img_small)


cv.waitKey(0)
cv.destroyAllWindows()