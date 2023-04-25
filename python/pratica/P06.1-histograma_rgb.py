import cv2
import matplotlib.pyplot as plt

# Carregando a imagem
image = cv2.imread("../../img/input/Lenna.png")

# Separando os canais
canais = cv2.split(image)
cores = ("blue", "green", "red")

# Mostrando a imagem
cv2.imshow("Original", image)

# Plotando o histograma
plt.figure(1)
plt.title("Histograma")
plt.xlabel("    Intensidade")
plt.ylabel("Pixels")

# Calculando o histograma para cada canal
for canal, cor in zip(canais, cores):
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist, c=cor, label=cor.capitalize())
    plt.xlim([0, 256])

plt.legend(title="Canais")
plt.show()

cv2.waitKey(0)
