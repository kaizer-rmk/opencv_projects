import cv2
import numpy as np

#opencv convention
#In opencv the +ve x-axis is same as mathematical convention but the +ve y-axis is oposite

#Imp: To resize an image first of all we need to know the current size of image

img=cv2.imread("res/cryptic.png")

#Resize:

# img.shape will give (height,width,channels(BGR))
print(img.shape)

#Now to resize image we use resize() function
imgResize=cv2.resize(img,(800,900)) #width and height
print(imgResize.shape)

#Crop:

#To crop image we don't need cv2, we do it by using matrix
#[initial-height:max-height,initial-width:max-width]
imgCroped=imgResize[0:200,200:500]

cv2.imshow("image",img)
cv2.imshow("Resizeimage",imgResize)
cv2.imshow("Img crop",imgCroped)
cv2.waitKey(0)
