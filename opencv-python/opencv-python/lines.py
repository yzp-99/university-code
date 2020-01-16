import cv2 as cv
import numpy as np

img = np.zeros((500, 500, 3), np.uint8)


img1 = np.ones((500, 500, 3), np.uint8) * 255
#  准备一些顶点坐标
pts = np.array([[100, 50], [200, 300], [300, 200], [400, 200]], np.int32)

pts = pts.reshape(-1, 1, 2)
print(pts.shape)
#  闭合多边形
cv.polylines(img, [pts], True, (0, 0, 255), 3, cv.LINE_AA)
#  不闭合多边形r
cv.polylines(img1, [pts], False, (0, 255, 0), 3, cv.LINE_AA)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img1, 'learning OpenCV', (0, 50), font, 1, (255, 255, 255), 2,
           cv.LINE_AA, False)
#   显示图像
cv.imshow('img', img)
cv.imshow('img1', img1)

cv.waitKey(0)
cv.destroyAllWindows()















