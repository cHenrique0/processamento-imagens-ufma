import cv2

image = cv2.imread("../img/input/Lenna.png")
crop = image[230:390, 215:350]  # [y:y, x:x]

cv2.imshow("Original", image)
cv2.imshow("Crop", crop)
cv2.imwrite("../img/output/recorte_lena.png", crop)
cv2.waitKey(0)
