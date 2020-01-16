import cv2 as cv
import cv2
#  图片路径
img_path = './cat.jpg'

#  读入彩色图
img_bar = cv.imread(img_path)

#  读入灰度图
img_gray = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

# 显示两个名为'img_bar','img_gray'的图像窗口
cv.imshow('img_bar', img_bar)
cv.imshow('img_gray', img_gray)

cv2.waitKey(0)   # 等待指令
#  关闭所有窗口
cv2.destroyAllWindows()