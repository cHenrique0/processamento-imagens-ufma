import cv2
import numpy as np

image = cv2.imread("../../img/input/Lenna.png")

# Separando os canais da imagem (escala de cinza)
gBlue, gGreen, gRed = cv2.split(image)

# Unindo os canais da imagem
# result = cv2.merge([gBlue, gGreen, gRed])

# Separando os canais (colorido)
zeros = np.zeros(image.shape[:2], dtype="uint8")
blue = cv2.merge([gBlue, zeros, zeros])
green = cv2.merge([zeros, gGreen, zeros])
red = cv2.merge([zeros, zeros, gRed])

# Imagem original
cv2.imshow("Original", image)
# Canais em escala de cinza
# cv2.imshow("Canal Vermelho", gRed)
# cv2.imshow("Canal Verde", gGreen)
# cv2.imshow("Canal Azul", gBlue)
# Canaiz coloridos
cv2.imshow("Canal Vermelho", red)
cv2.imshow("Canal Verde", green)
cv2.imshow("Canal Azul", blue)
cv2.waitKey(0)
