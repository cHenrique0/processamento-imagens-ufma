import numpy as np
import cv2

image = cv2.imread("../../img/input/Lenna.png")
H, W, C = image.shape

# Criando uma matriz com as dimensões da imagem original
mask = np.zeros((H, W), dtype="uint8")

# Centro da imagem
cX, cY = (H//2, W//2)

# Aplicando a máscara
cv2.circle(mask, (cX, cY), 100, 255, -1)
image_mask = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original", image)
cv2.imshow("Mask", mask)
cv2.imshow("Image mask", image_mask)
cv2.waitKey(0)
