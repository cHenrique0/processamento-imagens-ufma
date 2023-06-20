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

# Canais da imagem original
channels = cv2.split(img)
colors = ("b", "g", "r")

# Exibindo a imagem original, a equalizada e seus respectivos histogramas
figure1 = plt.figure(figsize=(15, 10), layout="constrained")
grid1 = figure1.add_gridspec(2, 2)

figure1.add_subplot(grid1[:, 0])
plt.title("Imagem original")
plt.axis("off")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
figure1.add_subplot(grid1[0, 1])
plt.title("Histograma RGB")
for (channel, color) in zip(channels, colors):
    hist = calcHist(channel)
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
figure1.add_subplot(grid1[1, 1])
plt.title("Histograma grayscale")
plt.hist(gray.ravel(), 256, [0, 256], edgecolor="black")

figure2 = plt.figure(figsize=(15, 10), layout="constrained")
grid2 = figure2.add_gridspec(1, 2)
figure2.add_subplot(grid2[0, 0])
plt.title("Imagem equalizada")
plt.axis("off")
plt.imshow(outputImg, cmap="gray")
figure2.add_subplot(grid2[0, 1])
plt.title("Histograma grayscale")
plt.hist(outputImg.ravel(), 256, [0, 256], edgecolor="black")

plt.show()
