import cv2 as cv
import numpy as np

img = cv.imread('4.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)

opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)

sure_bg = cv.dilate(opening, kernel, iterations=3)

dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)

ret, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, cv.THRESH_BINARY)

sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg, sure_fg)

ret, markersl = cv.connectedComponents(sure_fg)

markers = markersl + 1

markers[unknown == 255] = 0

markers3 = cv.watershed(img, markers)
img[markers3 == -1] = [255, 0, 0]

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
