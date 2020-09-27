import cv2
import numpy as np

#First we create matrix using numpy library
#0 means black
#1 means white
#512 is the dimention
#3is the no. of color channel
#np.uint8 is the unsigned integer of 8 bit range 0-255
img=np.zeros((512,512,3),np.uint8)

print(img)

#To color the whole image
#img[:]=255,0,0

#To color some part of image
#img[0:200,100:200]=0,255,0

#Draw shape:-

#Line:
#For this we use line(image,x-axis,y-axis,color,thickness)
cv2.line(img,(0,0),(512,512),(0,0,255),1)

#Rectangle:
#For this we use rectangle(image,x-axis,y-axis,color,thickness)
cv2.rectangle(img,(0,0),(20,50),(0,255,0),cv2.FILLED)

#Circle:
#For this we use circle(image,center-point,radius,color,thickness)
cv2.circle(img,(250,250),50,(255,0,0),2)


#Put Text:-
#To do this we simply do putText(image,"Text you want to put",(origine),font,scale,color,thickness)
cv2.putText(img,"CryptiC",(50,400),cv2.FONT_HERSHEY_COMPLEX,2,(0,3,150),2)

cv2.imshow("image",img)
cv2.waitKey(0)
