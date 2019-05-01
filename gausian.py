import cv2

img=cv2.imread('img/jv.jpg')
mat=(7,7)
blur=cv2.GaussianBlur(img,mat,0)
cv2.imshow('blur',blur)
cv2.waitKey(0)
cv2.destroyAllWindow()