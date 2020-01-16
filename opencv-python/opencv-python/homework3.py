import cv2 as cv
import cv2
img = cv.imread("zhu.jpg")

def nothing(x):
    pass


cv.namedWindow("ganen")
cv.createTrackbar("t1", "ganen", 0,255,nothing)
cv.createTrackbar("t2", "", 0,255,nothing)

while True:
    g1 = cv.getTrackbarPos("g1", "ganen")
    g2 = cv.getTrackbarPos("g1", "ganen")
    b = cv.Canny(img, g1, g2)
    cv.imshow("ganen", b)
    k = cv.waitKey(25) &0xff
    if chr(k) =="q":
        break
    elif chr(k) == "s":
        cv2.imwrite("guo.jpg", b)
        cv2.destroyAllWindows()

cv2.destroyAllWindows()