import cv2

# In order to capture video object we use the function  VideoCapture()

cap = cv2.VideoCapture("res/vid.mp4")

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
