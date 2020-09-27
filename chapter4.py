import cv2
import numpy as np
#numpy help us to deal with matrices

# Basic functions

#first we read the image
img = cv2.imread("res/cryptic.png")

#we define the kernel to get all of the values to be one
#size of matrix is 5x5
#type of object is unsigned integer of 8 bit(which means values can range 0-255)
kernel=np.ones((5,5),np.uint8)

# Now we convert this into gray scale
# To do that we use function known as cvtColor() which convert image in diffrent color space
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Now we use GaussianBlur() function to blur the image
#(7,7) is the kernel which is odd no.
#kernel is just a matrix which defines the size of and value of
# 0 is the sigmaX
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)

# In order to find edge in image we use Canny() function
# Here 100 is the thereshold values
imgCanny=cv2.Canny(img,100,100)

#To increase the thickness of edge as the edges are not perfect
#iterations is used for thickness
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)

#opposite of dialation
#For this we use erode() function
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)

#Now we display the image
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Gray Erosion",imgEroded)
cv2.waitKey(0)
