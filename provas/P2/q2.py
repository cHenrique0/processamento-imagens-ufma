import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregando a imagem usando o OpenCV
img = cv2.imread('./images/ScenarioLowContrast.jpg', 0)


# Equalização de histograma
imgEq = cv2.equalizeHist(img)

# Plotar histograma da imagem original
originalHist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.subplot(2, 2, 1)
plt.bar(np.arange(256), originalHist.ravel(), color='b')
plt.title('Histograma Original')
plt.xlim([0, 256])

# Plotar imagem original
plt.subplot(2, 2, 2)
plt.imshow(img, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

# Plotar histograma da imagem equalizada
eqHist = cv2.calcHist(
    [imgEq], [0], None, [256], [0, 256])
plt.subplot(2, 2, 3)
plt.bar(np.arange(256), eqHist.ravel(), color='b')
plt.title('Histograma Equalizado')
plt.xlim([0, 256])

# Plotar imagem equalizada
plt.subplot(2, 2, 4)
plt.imshow(imgEq, cmap='gray')
plt.title('Imagem Equalizada')
plt.axis('off')

# Exibir o plot
plt.tight_layout()
plt.show()
