import cv2 as cv
import numpy as np

# 检测人脸

baby = cv.imread('baby.jpg')
baby_gray = cv.cvtColor(baby, cv.COLOR_BGR2GRAY)
cv.imshow('baby_gray', baby_gray)

hear_cascade_face = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

faces_rects = hear_cascade_face.detectMultiScale(baby_gray, scaleFactor=1.2, minNeighbors=5);

print("Faces found:", len(faces_rects))

for (x, y, w, h)in faces_rects:
    cv.rectangle(baby, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv.imshow('baby_face', baby)
cv.waitKey(0)
cv.destroyAllWindows()