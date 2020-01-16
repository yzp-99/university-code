from cv2 import cv2
import numpy as np
import copy

f1 = open(r"F:\360MoveData\Users\ASUS\Desktop\timg.jpg")
img1 = cv2.imdecode(np.fromfile(f1,dtype=np.uint8),cv2.COLOR_RGB2BGR)
print(img1.shape)

img2 = copy.deepcopy(img1[15:300,165:420])
img3 = copy.deepcopy(img1[145:430,270:525])

g1 = copy.deepcopy(img2[:,:,1])
g1 = g1 * 1.5
print(g1[:5,:5])
print(g1.shape)

n = 0
m = 0
while True:
    if g1[n,m] >= 255:
        g1[n,m] = 255

    m += 1
    if m >= g1.shape[1]:
        n += 1
        m = 0

    if n >= g1.shape[0]:
        break

print(g1[:5,:5])
print(np.array(g1,dtype=np.uint8)[:5,:5])

# img2[:,:,1] = np.array(g1,dtype=np.uint8)

g2 = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
thresh,g3 = cv2.threshold(g2,95,255,type=cv2.THRESH_BINARY)
g4 = cv2.bitwise_not(g3)
g5 = cv2.bitwise_and(img3,img3,mask=g3)
g6 = cv2.bitwise_and(img2,img2,mask=g4)

g7 = g5 + g6

img1[15:300,165:420] = g5

cv2.imshow("g7", g7)
cv2.imshow("g6", g6)
cv2.imshow("g5", g5)
cv2.imshow("g4", g4)
cv2.imshow("g3", g3)
cv2.imshow("g2", g2)
cv2.imshow("img3", img3)
cv2.imshow("img2", img2)
cv2.imshow("img1", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
