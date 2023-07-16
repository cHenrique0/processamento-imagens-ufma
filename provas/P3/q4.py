import cv2
import numpy as np
import matplotlib.pyplot as plt


def filtro_rejeita_notch(shape, d0=9, u_k=0, v_k=0):
    (M, N) = shape

    H_0_u = np.repeat(np.arange(M), N).reshape((M, N))
    H_0_v = np.repeat(np.arange(N), M).reshape((N, M)).transpose()

    D_uv = np.sqrt((H_0_u - M / 2 + u_k) ** 2 + (H_0_v - N / 2 + v_k) ** 2)
    D_muv = np.sqrt((H_0_u - M / 2 - u_k) ** 2 + (H_0_v - N / 2 - v_k) ** 2)

    seletor_1 = D_uv <= d0
    seletor_2 = D_muv <= d0

    seletor = np.logical_or(seletor_1, seletor_2)

    H = np.ones((M, N))
    H[seletor] = 0

    return H


# Carregando a imagem em tons de cinza
img = cv2.imread('./images/apollo17.png', 0)

# Aplicando a transformada de Fourier
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)  # centralizando a transformada
fase = np.angle(fshift)  # calculando a fase
magnitude = 20*np.log(np.abs(fshift))  # calculando a magnitude

# Aplicando o filtro rejeita notch
img_shape = img.shape
H1 = filtro_rejeita_notch(img_shape, 9, 72, 85)
H2 = filtro_rejeita_notch(img_shape, 9, -72, 85)

filtro_notch = H1*H2
centro_filtro_notch = fshift * filtro_notch
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
plt.imshow(magnitude*filtro_notch, "gray")
plt.axis('off')

plt.figure("Resultado")
plt.imshow(img_result, "gray")
plt.axis('off')


plt.show()
