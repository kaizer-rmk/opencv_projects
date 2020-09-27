import cv2
import numpy as np

img = cv2.imread("res/cards.jpg")

#Objective:- try to get spade as flat as possible by four corner point of the card

#This height and width are the standard height of a card
width,height=250,350

#These points are the coordinates of four corner which you will get on paint
pts1=np.float32([[540,260],[1040,195],[650,970],[1130,900]])

#There coordinates are the standard size of card
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

#To transform from pts1 to pts2 we use getPerspectiveTransform()
matrix=cv2.getPerspectiveTransform(pts1,pts2)

#Finally we wrap up the matrix by usning wrapPerspective()
imageOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image",img)
cv2.imshow("imageoutput",imageOutput)
cv2.waitKey(0)
