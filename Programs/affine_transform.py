import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("itachi.jpg", 0)
rows, cols = img.shape
pts1 = np.float32([[50, 50], [200, 50], [50,200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
transform_image = cv2.getAffineTransform(pts1, pts2)
distance = cv2.warpAffine(img, transform_image, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(distance), plt.title('Output')
plt.show()