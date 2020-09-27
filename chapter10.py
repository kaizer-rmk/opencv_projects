import cv2


path="res/shape.jpg"
img= cv2.imread(path)

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)




cv2.imshow("OUTPUT",img)
cv2.waitKey(0)
