import cv2
import numpy as np
img = cv2.imread('itachi.jpg')
res = cv2.resize(img, None, fx=2, fy=3, interpolation=cv2.INTER_CUBIC)
height, width = img.shape[:2]
res = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)
cv2.imshow("Window Name", img)
cv2.waitKey(0)
cv2.destroyAllWindows()