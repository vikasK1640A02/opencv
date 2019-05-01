import cv2

cap=cv2.VideoCapture('vid/ai.mp4')

fourcc=cv2.VideoWriter_fourcc(*'XVID')
fps=30
frmaesize=(720,480)
out=cv2.VideoWriter('vid/vikas.avi',fourcc,fps,frmaesize)

while(cap.isOpened()):
	ret,frame=cap.read()
	cv2.imshow('vid',frame)

	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
		
out.realese()
cap.realese()
cv2.destroyAllWindow()