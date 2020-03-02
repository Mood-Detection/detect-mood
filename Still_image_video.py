import cv2
import time
video=cv2.VideoCapture(0) #   video capture 0 means default camera access
check,frame=video.read()
print(check)
print(frame)
time.sleep(1) # give time to cam to open
cv2.imshow('Capturing',frame)
cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()
