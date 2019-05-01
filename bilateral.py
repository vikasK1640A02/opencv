import cv2

img=cv2.imread('img/kris.jpg')

dimpixel=7
color=100
space=100

filters=cv2.bilateralFilter(img,dimpixel,color,space)
cv2.imshow('filter',filters)
cv2.waitKey(0)
cv2.destroyAllWindow()
