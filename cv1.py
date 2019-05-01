import cv2
img=cv2.imread('img/baby.jpg')
cv2.imshow("img",img)
cv2.imwrite('img/baby1.png',img)
cv2.waitKey(0)
cv2.destroyAllWindow()