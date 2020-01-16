import cv2 as cv
import cv2
img = cv.imread("xing.jpg")
img1 = cv2.resize(img, (300, 300))
img2 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)



cv.imshow('img', img)
cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.waitKey(0)
cv.destroyAllWindows()




