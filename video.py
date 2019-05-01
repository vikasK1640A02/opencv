import cv2

cap=cv2.VideoCapture('vid/ai.mp4')

while(cap.isOpened()):
	ret,frame=cap.read()
	cv2.imshow('vid',frame)

	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
cap.realese()
cv2.destroyAllWindow()