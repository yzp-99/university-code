import cv2
from matplotlib import pyplot as plt

img = cv2.imread('timg.jpg', cv2.IMREAD_GRAYSCALE)
_, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# 灰度渐变
_, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
thresh4 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 0)
thresh5 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 91, 0)
thresh6 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 0)
thresh7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 0)
ret, thresh8 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'adaptive_mean_5', 'adaptive_mean_91',
          'adaptive_gaussian_5', 'adaptive_gaussian_91', 'OTSU']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5, thresh6, thresh7, thresh8]

for i in range(9):
    plt.subplot(3, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()