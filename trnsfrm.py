import cv2
import numpy as np


imge=cv2.imread('img/jv.png')

rows=imge.shape[1]
cols=imge.shape[0]

m=np.float32([[0,1,250],[1,0,170]])

shift=cv2.warpAffine(img,m,(cols,rows))
cv2.imshow("shifted",shift)
cv2.waitKey(0)
cv2.destroyAllWindow()