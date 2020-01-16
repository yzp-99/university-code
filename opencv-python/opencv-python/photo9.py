#  -*- coding: utf-8 -*-
import cv2
import numpy as np

fn = "02.png"
if __name__ == '__main__':
    print('loading %s' % fn)
    img = cv2.imread(fn)
    sp = img.shape
    print(sp)

    # 获取图像大小
    sz1 = sp[0]
    sz2 = sp[1]
    print('width:%d\nheight:%d' % (sz2, sz1))
    # 创建一个窗口显示图像
    cv2.namedWindow('img')
    cv2.imshow('img', img)
    # 复制图像矩阵，生成与源图像一样的图像，并显示
    myimg2 = img.copy();
    cv2.namedWindow('myimg2')
    cv2.imshow('myimg2', myimg2)

    # 复制并转换为灰度化图像并显示
    myimg1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('myimg1')
    cv2.imshow('myimg1',myimg1)
    cv2.waitKey()
    cv2.destroyAllWindows()

