import cv2
img=cv2.imread("boy1.png",0)
cv2.imshow("boy1.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)
print(type(img))
