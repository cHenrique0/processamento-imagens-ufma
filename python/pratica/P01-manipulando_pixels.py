# Sistemas de coordenadas e manipulação de pixels

import cv2

img = cv2.imread("../../img/input/Lenna.png")

# No OpenCv a ordem das cores é BGR - Blue, Green, Red
blue, green, red = img[0, 0]  # acessando o pixel (0, 0)

print(f"Pixel (0, 0):\n* Red: {red}\n* Green: {green}\n* Blue: {blue}")

weight, height, channel = img.shape
""" for y in range(0, weight):
    for x in range(0, height):
        # pintando a imagem de azul
        # img[y, x] = (255, 0, 0)
        # componentes de cor
        # img[y, x] = (x % 256, y % 256, x % 256)
        # zerando a componente vermelha e azul e manipulando a componente verde
        # img[y, x] = (0, (x*y) % 256, 0) """

# adicionando pequenos quadrados de 5x5 pixels na imagem
for y in range(0, weight, 10):
    for x in range(0, height, 10):
        img[y:y+5, x:x+5] = (0, 255, 255)

cv2.imshow("Imagem modificada", img)
cv2.waitKey(0)
