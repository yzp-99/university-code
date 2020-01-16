import cv2 as cv
import cv2
img = cv.imread("en.jpg")  # 原图

def nothing(x):
    pass
cv.namedWindow("ganen")
cv.createTrackbar("t1", "ganen", 0,255,nothing)
cv.createTrackbar("t2", "", 0,255,nothing)

while True:
    t1 = cv.getTrackbarPos("t1", "ganen")
    t2 = cv.getTrackbarPos("t1", "ganen")
    e = cv.Canny(img, t1, t2)
    cv.imshow("ganen", e)
    k = cv.waitKey(25) &0xff
    if chr(k) =="q":
        break
    elif chr(k) == "s":
        # 相对路径保存图像
        cv2.imwrite("gan.jpg", e)
        cv2.destroyAllWindows()

cv2.destroyAllWindows()