import cv2 as cv
import numpy as np

x = np.uint8([250])
y = np.uint8([10])

print(cv.add(x, y))

print(x + y)
# 测试图片
# 保证图片大小，类型要一致

dog1 = cv.imread('./dog1.jpg')
dog2 = cv.imread('./dog2.jpg')
dog_add_cv = cv.add(dog1, dog2)
dog_add_np = dog1 + dog2
cv.imshow('src', np.vstack((dog1, dog2)))
cv.imshow('cv.add', dog_add_cv)
cv.imshow('np.add', dog_add_np)
cv.waitKey()
cv.destroyAllWindows()


