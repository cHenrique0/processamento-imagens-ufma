import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carregando a imagem
img = cv2.imread('./images/WhiteHorse.jpg')

# Convertendo para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicando a limiarização
threshold = 150  # limiar
_, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

# Encontrando os contornos dos objetos segmentados
contours, _ = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Encontrando o contorno com a maior área
maxContour = max(contours, key=cv2.contourArea)

# Obtendo as coordenadas do retângulo delimitador
x, y, w, h = cv2.boundingRect(maxContour)

# Desenhando o retângulo ao redor do animal
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

# Mostrando as imagens
plt.figure("Imagem original", figsize=(6.8, 15), position=(0, 0))
plt.axis('off')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.figure("Imagem segmentada", figsize=(6.8, 15))
plt.axis('off')
plt.imshow(thresh, cmap='gray')
plt.show()
