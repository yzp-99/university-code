
import cv2

# 读取图片
source = cv2.imread("./img.jpg", 1)

# 定义x，y方向的缩放因子
scaleX = 0.5
scaleY = 0.5

# 将图片缩小为原来的0.5倍
scaleDown = cv2.resize(source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR)
# 将图片放大到原来的1.5倍
scaleUp = cv2.resize(source, None, fx=scaleX * 3, fy=scaleY * 3, interpolation=cv2.INTER_LINEAR)

# 剪切图像。我们直接操作numpy数组进行操作，将其中的指定行、列内容读出来，即完成图像剪切
crop = source[110:150, 120:200]

# 显示所有图片（原图、缩小、放大、剪切后的图）
cv2.imshow("Original", source)
cv2.imshow("Scaled Down", scaleDown)
cv2.imshow("Scaled Up", scaleUp)
cv2.imshow("Cropped Image", crop)
cv2.waitKey(0)






