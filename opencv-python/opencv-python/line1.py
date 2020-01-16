import numpy as np
import cv2 as cv

img = np.zeros((500, 500, 3), np.uint8)

#  绘制文字
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "Learning OpenCV", (150, 250), font, 1, (255, 0, 255), 2)

#  显示图像
cv.imshow('img', img)

cv.waitKey(0)
cv.destroyAllWindows()













