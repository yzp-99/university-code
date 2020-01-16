import cv2 as cv
import numpy as np

img = cv.imread('notebook.jpg')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

edges = cv.Canny(gray, 180, 250)


cv.imshow('edges', edges)
cv.waitKey(0)
cv.destroyAllWindows()