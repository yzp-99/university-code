import cv2 as cv
img = cv.imread('ga.png')

meaBlur = cv.medianBlur(img, 5)
cv.imshow('img', img)
cv.imshow('meaBlur', meaBlur)

cv.waitKey(0)
cv.destroyAllWindows()



