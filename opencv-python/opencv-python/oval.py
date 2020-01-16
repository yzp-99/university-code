
import numpy as np
import cv2
#create a black use numpy,size is:512*512
img = np.zeros((512,512,3), np.uint8)
#fill the image with white
img.fill(255)
###########################################
####Main Function                      ####
#draw
#        start x  y end x    y      color
cv2.line(img, (10,50), (511, 511), (255,0,0), 5)
cv2.rectangle(img, (384,0), (510, 128), (0, 255, 0), 3)
cv2.circle(img, (447, 63), 63, (0,0,255), -1)
cv2.ellipse(img, (256,256), (100,50),45,0,290,(0,0,255),-1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hello', (10,500), font, 4, (255,2,255), 2)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()





