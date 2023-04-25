# Importando o OpenCV
import cv2

# Lendo a imagem
img = cv2.imread("../../img/input/Lenna.png")
# [0] = largura, [1] = altura, [2] = canais
largura, altura, canais = img.shape

print(f"Largura: {largura} pixels")
print(f"Altura: {altura} pixels")
print(f"Canais: {canais}")

# Mostrando a imagem
cv2.imshow("Lenna", img)
cv2.waitKey(0)  # Aguarda uma tecla ser pressionada para fechar a janela

# Salvando a imagem
# cv2.imwrite("../../img/Lenna2.png", img)
