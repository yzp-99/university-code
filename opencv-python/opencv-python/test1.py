import cv2 as cv
import numpy as np

img_path = './img2.jpg'

img_bar = cv.imread(img_path)
cv.imshow('img_bar', img_bar)



cv.waitKey(0)

cv.destroyAllWindows()
