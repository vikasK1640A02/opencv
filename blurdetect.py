import cv2
from tqdm import trange


cap = cv2.VideoCapture('vid/v.mp4')
f = open('results.txt', 'w')

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

for i in trange(frame_count, unit=' frames', leave=False, dynamic_ncols=True, desc='Calculating blur ratio'):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	fm = cv2.Laplacian(gray, cv2.CV_64F).var()

	# Sample quality bar. Parameters adjusted manually to fit horizontal image size
	cv2.rectangle(frame, (0, 1080), (int(fm*1.6), 1040), (0,0,255), thickness=cv2.FILLED)

	im = cv2.resize(frame, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
	cv2.imshow("Output", im)

	f.write(str(fm)+'\r')

	k = cv2.waitKey(1) & 0xff
	if k == 27:
		break 