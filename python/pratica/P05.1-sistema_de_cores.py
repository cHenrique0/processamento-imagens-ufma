import cv2

image = cv2.imread("../../img/input/Lenna.png")

# Escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# L*a*b
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

cv2.imshow("RGB", image)
cv2.imshow("Gray", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("L*a*b", lab)
cv2.waitKey(0)
