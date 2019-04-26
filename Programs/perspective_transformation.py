import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('itachi.jpg')
rows, cols, ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0], [300,0], [0,300], [300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.getPerspectiveTransform(pts1, pts2)
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()