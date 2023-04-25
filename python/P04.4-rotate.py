import cv2

image = cv2.imread("../img/input/Lenna.png")
H, W, C = image.shape  # altura, largura, canais

# Pegando o centro da imagem fazendo divisão inteira //
centro = (H//2, W//2)

# Criando a matriz de rotação 2D passando: centro, graus de rotação, escala
Mr = cv2.getRotationMatrix2D(centro, 45, 1.0)

# Aplicando a rotação
image_rotation = cv2.warpAffine(image, Mr, (H, W))

# Mostrando as imagens
cv2.imshow("Original", image)
cv2.imshow("Rotate", image_rotation)
cv2.waitKey(0)
