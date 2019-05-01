import cv2

img=cv2.imread('img/love.jpg')
kernal=3
median=cv2.medianBlur(img,kernal)
cv2.imshow('median',median)
cv2.waitKey(0)
cv2.destroyAllWindow()