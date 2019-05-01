import cv2

cap=cv2.VideoCapture(0)
forcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('record.mp4',forcc,20.0,(640,480))

while(cap.isOpened()):
	ret,frame=cap.read()

	if ret==True:

		print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

		out.write(frame)

		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		cv2.imshow('Result',gray)
		if cv2.waitKey(1) & 0xFF==ord('q'):
			break

cap.release()
out.release()
cv2.destroyAllWindows()