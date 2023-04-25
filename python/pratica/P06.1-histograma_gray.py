import cv2
import matplotlib.pyplot as plt

# Carregando a imagem
image = cv2.imread("../../img/input/Lenna.png")

# Convertendo pra escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculando o histograma
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Mostrando a imagem
# cv2.imshow("Original", image)
cv2.imshow("Gray", gray)

# Plotando o histograma
plt.figure(1)
plt.title("Histograma")
plt.xlabel("Intensidade")
plt.ylabel("Pixels")
plt.plot(hist)
plt.xlim([0, 256])

plt.figure(2)
plt.hist(image.ravel(), 256, (0, 256), ec="black", lw=0.4)
plt.show()

cv2.waitKey(0)
