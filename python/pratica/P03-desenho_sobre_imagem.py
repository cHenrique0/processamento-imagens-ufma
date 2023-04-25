import cv2

original_image = cv2.imread("../../img/input/tucano.jpeg")
copy_image = original_image.copy()

# Cores
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)

# Desenhando linhas
cv2.line(copy_image, (0, 0), (100, 200), green)
cv2.line(copy_image, (300, 200), (150, 150), red, 5)

# Desenhando retângulos
cv2.rectangle(copy_image, (20, 20), (120, 120), blue, 10)  # Não preenchido
cv2.rectangle(copy_image, (200, 50), (255, 125), green, -1)  # Preenchido

# Desenhando círculos
X, Y = copy_image.shape[1] // 2, copy_image.shape[0] // 2
for r in range(0, 175, 15):
    cv2.circle(copy_image, (X, Y), r, red)

# Escrevendo texto
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(copy_image, "OpenCV", (450, 65), font, 2, white, 2, cv2.LINE_AA)

# Mostrando a imagem
cv2.imshow("Original", original_image)
cv2.imshow("Manipulada", copy_image)
cv2.waitKey(0)
