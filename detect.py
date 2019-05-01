import cv2

img=cv2.imread('img/cute.jpg')

#Canny detector have 3 parameter
thresold1=50
thresold2=100

canny=cv2.Canny(img,thresold1,thresold2)

cv2.imshow('canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindow()