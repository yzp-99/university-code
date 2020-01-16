import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('1.png', 0)
img2 = cv.imread('3.jpg')
dst = cv.inpaint(img2, img1, 3, cv.INPAINT_TELEA)
dst1 = cv.inpaint(img2, img1, 3, cv.INPAINT_NS)

plt.subplot(1, 2, 1)
plt.title('1')
plt.imshow(dst)


plt.subplot(1, 2, 2)
plt.title('2')
plt.imshow(dst1)

plt.show()

