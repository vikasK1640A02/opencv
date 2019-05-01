import cv2
import numpy as np

pic=np.zeros((500,500,3),dtype='uint8')
#color=()
cv2.rectangle(pic,(0,0),(500,150),(123,200,98),3)
cv2.line(pic,(40,120),(500,150),(123,200,98),3)
cv2.circle(pic,(250,250),50,(123,200,98),3)
cv2.imshow('dark',pic)
cv2.waitKey(0)
cv2.destroyAllWindow()
