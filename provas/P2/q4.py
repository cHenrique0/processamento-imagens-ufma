import cv2
import numpy as np
from matplotlib import pyplot as plt

# Centro do objeto
cx, cy = 0, 0


def segmentBottleCap(image):
    # Convertendo a imagem para o espaço de cores HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Valores de limite para a cor vermelha
    lowerRed = np.array([0, 100, 100])
    upperRed = np.array([10, 255, 255])

    # Máscara com os valores de limite
    mask1 = cv2.inRange(hsv, lowerRed, upperRed)

    # Valores de limite adicionais para a cor vermelha
    lowerRed2 = np.array([170, 100, 100])
    upperRed2 = np.array([180, 255, 255])

    # Máscara com os valores de limite adicionais
    mask2 = cv2.inRange(hsv, lowerRed2, upperRed2)

    # Combinando as duas máscaras para obter a máscara final
    finalMask = cv2.bitwise_or(mask1, mask2)

    # Encontrando contornos na máscara
    contours, _ = cv2.findContours(
        finalMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        # Encontrando o contorno com a maior área
        maxContour = max(contours, key=cv2.contourArea)

        # Calculando o retângulo delimitador do contorno
        x, y, w, h = cv2.boundingRect(maxContour)

        # Desenhando um retângulo delimitador ao redor do objeto
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)

        # Calculando o centro do objeto
        centerX = x + w // 2
        centerY = y + h // 2

        global cx, cy
        cx, cy = centerX, centerY

        # Desenhando uma cruz no centro do objeto
        cv2.drawMarker(image, (centerX, centerY), (0, 255, 0), markerType=cv2.MARKER_CROSS, markerSize=30,
                       thickness=5)

        # Exibindo as coordenadas do objeto
        print(f"Coordenadas X,Y do objeto: ({centerX}, {centerY})")

    return image


# Carregando a imagem contendo a tampa da garrafa PET
img = cv2.imread("./images/tampa_fundo_azul.jpeg")
# img = cv2.imread("./images/tampa_fundo_preto.jpeg")

# Segmentando a tampa da garrafa PET na imagem usando a função criada
imSeg = segmentBottleCap(img.copy())

# Exibindo as imagens
figure = plt.figure(figsize=(15, 10), layout="constrained")
grid = figure.add_gridspec(1, 2)

figure.add_subplot(grid[0, 0])
plt.title("Imagem original")
plt.axis("off")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
figure.add_subplot(grid[0, 1])
plt.title("Imagem segmentada")
plt.axis("off")
plt.imshow(cv2.cvtColor(imSeg, cv2.COLOR_BGR2RGB))
plt.text(cx+90, cy-90, f"({cx}, {cy})", fontsize=20, color="#00ff00")

plt.show()
