import cv2 as cv

img = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)

ret, the = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

adaThe1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 3, 2)

adaThe2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 2)


cv.imshow('img', img)
cv.imshow('THE', the)
cv.imshow('adaThe1', adaThe1)
cv.imshow('adaThe2', adaThe2)

cv.waitKey(0)
cv.destroyAllWindows()
