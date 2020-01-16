import cv2
import numpy as np
img = cv2.imread('lightning.png', 0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)

cnt = contours[0]
img_color1 = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
img_color2 = np.copy(img_color1)
cv2.drawContours(img_color1, [cnt], 0, (0, 0, 255), 2)
cv2.imshow(img_color1)
"""
cv2.imshow(img_color1)
cv2.imshow(img_color2)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

area = cv2.contourArea(cnt)  # 面积
print(area)

perimeter = cv2.arcLength(cnt, True)  # 周长
print(perimeter)

M = cv2.moments(cnt)  # 图像矩

cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']  #


print(cx, cy)
