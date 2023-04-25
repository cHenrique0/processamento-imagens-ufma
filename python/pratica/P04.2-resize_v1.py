import cv2
import numpy as np

# Carregando a imagem
image = cv2.imread("../../img/input/tucano.jpeg")

# Pegando altura e larguras originais
largura = image.shape[1]
altura = image.shape[0]

# Calculando a proporção
proporcao = float(altura/largura)

# Nova largura e altura
nova_largura = 320  # pixels
nova_altura = int(nova_largura * proporcao)

# Setando o novo tamanho da imagem
novo_tamanho = (nova_largura, nova_altura)

# Fazendo o redimensionamento
image_resize = cv2.resize(image, novo_tamanho, interpolation=cv2.INTER_AREA)

# Mostrando as imagens
cv2.imshow("Original", image)
cv2.imshow("Resize", image_resize)
cv2.waitKey(0)
