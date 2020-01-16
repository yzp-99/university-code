# encoding:utf-8
import cv2

img = cv2.imread("13.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
gray = cv2.Canny(gray, 100, 300)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
# print(contours[0])
cv2.imshow("0", binary)
cv2.imshow("win10", img)
cv2.waitKey(0)
cv2.destroyAllWindows()