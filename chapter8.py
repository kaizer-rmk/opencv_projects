import cv2
import numpy as np

#Image joining

img=cv2.imread("res/rmk.jpg")

#First we use Horizontal stack
hor=np.hstack((img,img))

#Now we use Vertical stack
ver=np.vstack((img,img))

cv2.imshow("Horizontal",hor)
cv2.imshow("Vertical",ver)
cv2.waitKey(0)
