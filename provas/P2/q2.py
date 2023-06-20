import cv2
import numpy as np
from matplotlib import pyplot as plt


def calcHist(image):
    # Criando o histograma com zeros
    histogram = np.zeros(256, dtype=int)

    # Percorrendo os pixels da imagem e atualizando o histograma
    for row in image:
        for pixel in row:
            histogram[pixel] += 1

    return histogram


def calcCumulativeHist(histogram):
    # Criando o histograma cumulativo com zeros
    cumulativeHist = np.zeros(256, dtype=int)

    # Calculando o histograma cumulativo
    cumulativeHist[0] = histogram[0]
    for i in range(1, len(histogram)):
        cumulativeHist[i] = cumulativeHist[i-1] + histogram[i]

    return cumulativeHist


def equalizeHist(image):
    # Calculando o histograma da imagem
    histogram = calcHist(image)

    # Calculando o histograma cumulativo
    cumulativeHist = calcCumulativeHist(histogram)

    # Calculando o fator de normalização
    numPixels = image.shape[0] * image.shape[1]
    normalizationFactor = 255.0 / numPixels

    # Equalizando a imagem
    equalizedImage = np.zeros_like(image)
    for i in range(len(cumulativeHist)):
        equalizedValue = int(
            round(cumulativeHist[i] * normalizationFactor))
        equalizedImage[image == i] = equalizedValue

    return equalizedImage


# Carregando a imagem de entrada
img = cv2.imread(
    './images/ScenarioLowContrast.jpg')

# Convertendo a imagem para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Equalizando o histograma da imagem
outputImg = equalizeHist(gray)

# Exibindo a imagem original, a equalizada e seus respectivos histogramas
plt.figure("Imagem original", figsize=(15, 10))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.hist(img.ravel(), 256, [0, 256], edgecolor="black")

plt.figure("Imagem equalizada", figsize=(15, 10))
plt.subplot(1, 2, 1)
plt.imshow(outputImg, cmap="gray")
plt.subplot(1, 2, 2)
plt.hist(outputImg.ravel(), 256, [0, 256], edgecolor="black")

plt.show()
