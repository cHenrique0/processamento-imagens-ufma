import cv2
import matplotlib.pyplot as plt
import numpy as np

# Carregando a imagem
image = cv2.imread("../../img/input/Lenna.png")

# Convertendo para escala de cinza
if (len(image.shape) == 3):
    image = (cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))

# Eixo X do histograma (intensidades)
x_hist = [x for x in range(0, 256)]

# Eixo Y do histograma (pixels)
y_hist = []
aux = []
lin, col = image.shape
for y in range(0, lin):
    for x in range(0, col):
        aux.append(image[y, x])

print(len(y_hist))
print("\n")
print(y_hist)


# Mostrando a imagem
# cv2.imshow("Gray Scale", image)
# cv2.waitKey(0)
