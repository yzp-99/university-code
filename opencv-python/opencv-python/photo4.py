import cv2 as cv
import cv2
import numpy as np

img = cv2.imread('fushi.png')
#img = cv2.resize(img, (200, 300))

kernel = np.ones((5, 5), np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv.imshow('fat', img)
cv.waitKey(0)
cv.destroyAllWindows()