import cv2 as cv

src = cv.imread('timg.jpg', cv.IMREAD_GRAYSCALE)

dst1 = cv.equalizeHist(src)
cla1 = cv.createCLAHE(clipLimit=5, tileGridSize=(50, 50))

dst2 = cla1.apply(src)

cv.imshow('src', src)
cv.imshow('dst1', dst1)
cv.imshow('dst2', dst2)

cv.waitKey(0)
cv.destroyAllWindows()

