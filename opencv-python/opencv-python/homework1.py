import cv2 as cv
import numpy as np
#                宽   长              灰画布
img = np.ones((600, 900, 3), np.uint8) * 127


#    圆形    画布  圆心坐标 半径大小 颜色BGR  线条粗细 平滑
cv.circle(img, (200, 400), 50, (255, 255, 0), 3, cv.LINE_AA)
cv.circle(img, (200, 400), 100, (255, 255, 0), 3, cv.LINE_AA)
cv.circle(img, (200, 400), 150, (255, 255, 0), 3, cv.LINE_AA)

#     矩形           左下角坐标 右上角坐标 线条宽度 颜色
cv.rectangle(img, (50, 550), (350, 250), (0, 255, 255), 3, cv.LINE_AA)
cv.rectangle(img, (100, 500), (300, 300), (0, 255, 255), 3, cv.LINE_AA)
cv.rectangle(img, (150, 450), (250, 350), (0, 255, 255), 3, cv.LINE_AA)
#  线条       起点坐标    终点坐标   颜色       宽度
cv.line(img, (50, 400), (350, 400), (0, 0, 255), 3)
cv.line(img, (200, 250), (200, 550), (0, 0, 255), 3)

# 多边形

triangle = [(580, 350), (750, 340), (680, 420), (600, 500), (800, 500)]

# 绘制三角形
cv.line(img, triangle[0], triangle[1], (0, 0, 255), 3, cv.LINE_AA)
cv.line(img, triangle[1], triangle[2], (0, 0, 255), 3, cv.LINE_AA)
cv.line(img, triangle[2], triangle[0], (0, 0, 255), 3, cv.LINE_AA)
cv.line(img, triangle[2], triangle[3], (0, 0, 255), 3, cv.LINE_AA)
cv.line(img, triangle[3], triangle[4], (0, 0, 255), 3, cv.LINE_AA)
cv.line(img, triangle[4], triangle[2], (0, 0, 255), 3, cv.LINE_AA)

#  椭圆形
#               椭圆中心点  长短半轴 旋转角度 起始角度 终止角度
cv.ellipse(img, (220, 100), (220, 100), 0, 0, 360, (0, 255, 0), 3, cv.LINE_AA)

cv.ellipse(img, (200, 100), (100, 30), 0, 270, 90, (255, 255, 255), 3, cv.LINE_AA)
cv.ellipse(img, (200, 100), (110, 50), 180, 270, 180, (0, 0, 255), 3, cv.LINE_AA)
cv.ellipse(img, (200, 100), (120, 65), 180, 270, 180, (255, 0, 0), 3, cv.LINE_AA)
cv.ellipse(img, (200, 100), (110, 50), 180, 90, 180, (255, 255, 0), 3, cv.LINE_AA)
cv.ellipse(img, (200, 100), (120, 65), 180, 90, 180, (0, 255, 0), 3, cv.LINE_AA)


# 绘制文字
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'YU ZONG PENG', (380, 180), font, 2, (255, 255, 255), 2)

cv.imshow('img', img)
cv.imwrite("2.jpg", img)
cv.waitKey(0)
cv.destroyAllWindows()












