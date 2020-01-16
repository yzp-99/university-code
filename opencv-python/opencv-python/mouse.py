import cv2 as cv
import numpy as np

ox = 0
oy = 0

img = np.ones((500, 500, 3), np.uint8) * 127

#  响应函数，在回调函数中处理
def draw_circle(event, x, y, flags, param):
    global img
    global ox, oy
#   鼠标左键双击
    if event == cv.EVENT_LBUTTONDBLCLK:
        img = np.ones((500, 500, 3), np.uint8) * 127
        cv.circle(img, (x, y), 20, (0, 255, 0), 3, cv.LINE_AA)
#  鼠标移动事件
    elif event == cv.EVENT_MOUSEMOVE:
        cv.line(img, (ox, oy), (x, y), (255, 255, 255), 3, cv.LINE_AA)
        ox, oy = x, y
#  创建一个窗体并为鼠标事件绑定监听回调函数
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)


while True:
    cv.imshow('image', img)
    k = cv.waitKey(25) & 0xff
    if chr(k) == 'q':
        break