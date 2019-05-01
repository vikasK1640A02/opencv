import cv2
cap = cv2.VideoCapture("vid/vikas.avi")
backsub = cv2.createBackgroundSubtractorMOG2(history=200, varThreshold=128, detectShadows=True)
ret, im = cap.read()   
fgmask = backsub.apply(im, None, 0.01)
arr = arr + imarr
heat = cv2.applyColorMap(arr, cv2.COLORMAP_JET)
cv2.imwrite("heatmap.jpg", heat)
cv2.imshow("heatmap", heat)