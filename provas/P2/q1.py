import cv2
import numpy as np
from matplotlib import pyplot as plt


# Carrega a imagem
img = cv2.imread("./images/A_blue_eye.jpg")
copia = img.copy()

# Extrai as cores entre o intervalo BGR definido
mask = cv2.inRange(img, (0, 0, 0), (60, 60, 60))

# Slice no preto
imask = mask > 0
preto = np.zeros_like(img, np.uint8)
preto[imask] = img[imask]
preto = cv2.cvtColor(preto, cv2.COLOR_BGR2GRAY)

# Detecção de círculos
circles = cv2.HoughCircles(preto, cv2.HOUGH_GRADIENT, 1, 100,
                           param1=30, param2=30, minRadius=20, maxRadius=100)

# Pelo menos um círculo encontrado
if circles is not None:
    # Converte para int
    circles = np.round(circles[0, :]).astype("int")

    # Loop nas coordenadas (x, y) e raio dos círculos encontrados
    for (x, y, r) in circles:
        r = r+50
        # Desenha o círculo encontrado
        cv2.circle(copia, (x, y), r - 25, (0, 255, 0), 2)

        # Desenha o retângulo do centro do círculo
        cv2.rectangle(copia, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    # Mostra a imagem com o círcuto e centro encontrado pelo Hough Circle
    # plt.figure('Original')
    # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.figure("Detecção da íris e pupila")
    plt.imshow(cv2.cvtColor(copia, cv2.COLOR_BGR2RGB))
    plt.show()
