import cv2
import numpy as np
import matplotlib.pyplot as plt
from filtros import filtro_rejeita_notch


# Carregando a imagem em tons de cinza
img = cv2.imread('./images/camera.tif', 0)

# Aplicando a transformada de Fourier
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)  # centralizando a transformada
fase = np.angle(fshift)  # calculando a fase
magnitude = 20*np.log(np.abs(fshift))  # calculando a magnitude

# Aplicando o filtro rejeita notch
img_shape = img.shape
H = filtro_rejeita_notch(img_shape, 4, 28, 0)
centro_filtro_notch = fshift * H
rejeita_notch = np.fft.ifftshift(centro_filtro_notch)
inversa_rejeita_notch = np.fft.ifft2(rejeita_notch)  # calculando a inversa

img_result = np.abs(inversa_rejeita_notch)

# Exibindo os resultados
plt.figure("Imagem Original")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.figure("Espectro de Frequência - Imagem Original")
plt.imshow(magnitude, cmap='gray')
plt.axis('off')

plt.figure("Filtro Rejeita Notch")
plt.imshow(magnitude*H, "gray")
plt.axis('off')

plt.figure("Resultado")
plt.imshow(img_result, "gray")
plt.axis('off')


plt.show()
