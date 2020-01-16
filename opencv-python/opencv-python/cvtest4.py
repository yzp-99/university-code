

import cv2

from matplotlib import pyplot as plt

img = cv2.imread('sun.jpg')

plt.title("k")
#  Matplotlib 有一个绘制直方图的函数：matplotlib.pyplot.hist()
plt.hist(img.ravel(), 256, [0, 256])
plt.show()





