import cv2

image = cv2.imread("../../img/input/Lenna.png")

# Invertendo a imagem na horizontal
flip_h = image[::-1, :]
# flip_h = cv2.flip(image, 1) # Tem o mesmo efeito do slicing acima

# Invertendo a imagem na vertical
flip_v = image[:, ::-1]
# flip_v = cv2.flip(image, 0)

# Invertendo a imagem nos dois sentidos
flip = image[::-1, ::-1]
# flip = cv2.flip(image, -1)

cv2.imshow("Original", image)
cv2.imshow("Flip Horizontal", flip_h)
cv2.imshow("Flip Vertical", flip_v)
cv2.imshow("Flip", flip)
cv2.waitKey(0)
