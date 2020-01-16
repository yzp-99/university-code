import cv2 as cv
import numpy as np
import cv2
ox = 0
oy = 0
sx = 0
sy = 0

#  回调函数

def draw_rectangle(event, x, y, flags, param):
    #  global 修饰的字段，表示使用全局变量
    global img
    global ox, oy, sx, sy

    #  鼠标左键单击清理图像

    if event == cv.EVENT_FLAG_RBUTTON:
        img = np.ones((500, 500, 3), np.uint8) * 127
    elif event != cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        sx, sy = x, y
        ox, oy = x, y

    #  左键按下且鼠标移动事件

    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.line(img, (ox, oy), (x, y), (255, 255, 255), 3, cv.LINE_AA)
        ox, oy = x, y

    elif event == cv.EVENT_LBUTTONUP:
    # elif flags != cv.EVENT_FLAG_LBUTTON and event != cv.EVENT_MOUSEMOVE:
        cv.rectangle(img, (sx, sy), (x, y), (255, 0, 255), 3, cv.LINE_AA)

#  创建一个窗体并为鼠标事件绑定监听回调函数

cv.namedWindow('image')
cv.setMouseCallback('image', draw_rectangle)

#  创建一张灰白图片

img = np.ones((500, 500, 3), np.uint8) * 127
while True:
    cv.imshow('image', img)
    k = cv.waitKey(25) & 0XFF
    if chr(k) == 'q':
        break

















