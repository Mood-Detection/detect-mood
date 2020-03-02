import cv2
import time
video=cv2.VideoCapture(0)
a=1 # print the frames 
while True: # use while condtion to repeat the image showing video 
    a=a+1
    check,frame=video.read()
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Capturing',frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
print(a) # This will print the number of frames
video.release()
cv2.destroyAllWindows()
