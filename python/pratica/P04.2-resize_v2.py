import numpy as np
import cv2

image = cv2.imread("../img/input/tucano.jpeg")
resize = image[::2, ::2]

cv2.imshow("Original", image)
cv2.imshow("Resize", resize)
cv2.waitKey(0)
