import cv2
print("Imported successfully")

#In order to read images we have function by the name imread()
img = cv2.imread("res/cryptic.png")

#In order to display we have function by the name imshow() having 2 argument 1st one is name of the window and 2nd which image to display

cv2.imshow("output",img)

# Image appeared but for few sec
# So, we delay it by the function waitKey() : 0 means infinite delay  : other value means for that milliseconds

cv2.waitKey(0)

