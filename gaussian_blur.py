import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread("butterfly.jpeg")
img_copy= np.copy(img)
img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)
#plt.imshow(img_copy)
gray = cv2.cvtColor(img_copy, cv2.COLOR_RGB2GRAY )
#plt.imshow(gray)

blurred_img = cv2.GaussianBlur( gray, (9, 9), sigmaX =0)
#plt.imshow(blurred_img, cmap = 'gray')


kernel = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])

filtered_img = cv2.filter2D(blurred_img, -1, kernel)
#plt.imshow(filtered_img)

retval, binary_img = cv2.threshold(filtered_img, 50, 255, cv2.THRESH_BINARY)
plt.imshow(binary_img, cmap = 'gray')
