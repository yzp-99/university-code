import cv2 as cv
import numpy as np


a = cv.imread('apple.png')
b = cv.imread('juice.png')

g = a.copy()
gpa = [g]

for i in range(6):
    g = cv.pyrDown(g)
    gpa.append(g)

g = b.copy()
gpb = [g]
for i in range(6):
    g = cv.pyrDown(g)
    gpb.append(g)

lpa = [gpa[5]]
for i in range(5, 0, -1):

    ge = cv.pyrUp(gpa[i])
    L = cv.subtract(gpa[i-1], ge)
    lpa.append(L)

lpb = [gpb[5]]
for i in range(5, 0, -1):

    ge = cv.pyrUp(gpb[i])
    L = cv.subtract(gpb[i-1], ge)
    lpb.append(L)

LS = []
for la, lb in zip(lpa, lpb):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols//2], lb[:, cols//2:]))
    LS.append(ls)

ls1 = LS[0]
for i in range(1, 6):
    ls1 = cv.pyrUp(ls1)
    ls1 = cv.add(ls1, LS[i])
real = np.hstack((a[:, :cols // 2], b[:, cols // 2:]))





cv.imshow('k', ls1)
cv.imshow('b', real)
cv.waitKey(0)
cv.destroyAllWindows()