import cv2

# Now we move to the webcam capture
# Webcam capture is very similar to video capturing we just need to write the id of our camera

# In order to capture video object we use the function  VideoCapture()
# 0 is used for default camera in our laptop
cap = cv2.VideoCapture(0)

# Now we define some parameter for it such as size, brightness
cap.set(3,640) #id:3 is used for width
cap.set(4,480) #id:4 is used for height
cap.set(10,100) #id:10 is used for brightness

# Basically video is a set of images so we use while loop for capturing all the images in the video


while True:
    # Here we use 2 variable where img saves those images  and success tells whether the video captured successfully or not
    # In order to capture images we use function by name read()
    success, img=cap.read()
    # In order to show img we use imshow()
    cv2.imshow("video",img)
    # We will use particular key for the end of while
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
