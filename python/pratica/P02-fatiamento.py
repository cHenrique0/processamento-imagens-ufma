import cv2

image_original = cv2.imread('../../img/input/Lenna.png')
image_copy = image_original.copy()

# Cria um retângulo azul por toda a largura da imagem
image_copy[30:50, :] = (255, 0, 0)

# Cria um quadrado vermelho
image_copy[100:150, 50:100] = (0, 0, 255)

# Cria um retângulo amarelo por toda a altura da imagem
image_copy[:, 200:220] = (0, 255, 255)

# Cria um retângulo verde da linha 150 a 300 nas colunas 250 a 350
image_copy[150:300, 250:350] = (0, 255, 0)

# Cria um quadrado ciano
image_copy[300:400, 50:150] = (255, 255, 0)

# Cria um quadrado branco
image_copy[250:350, 300:400] = (255, 255, 255)

# Cria um retângulo preto
image_copy[70:100, 300:450] = (0, 0, 0)

# Mostra a imagem
cv2.imshow("Original", image_original)
cv2.imshow("Manipulada", image_copy)
cv2.waitKey(0)
