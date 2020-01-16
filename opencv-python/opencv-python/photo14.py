
import matplotlib.pyplot as plt
import cv2 as cv

import numpy as np

img = cv.imread('shuzi.jpg')

rows, cols, ch = img.shape
print(rows, cols, ch)

pts1 = np.float32([[50, 65], [368, 52], [28, 387], [389, 398]])
pts2 = np.float32 ([[0,0],[300,0],[0,300],[300,300]])

M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (300, 300))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Input')

plt.subplot(1, 2, 2)
plt.imshow(dst)
plt.title('Output')
plt.show()












