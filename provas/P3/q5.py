import cv2
import numpy as np
from matplotlib import pyplot as plt


def filtro_passa_alta(img, freq_corte):
    # Transformada de Fourier
    f = np.fft.fft2(img)

    # Centraliza a transformada de Fourier(deslocamento)
    fshift = np.fft.fftshift(f)

    linhas, colunas = img.shape
    cLinha, cColuna = linhas // 2, colunas // 2

    # Cria uma máscara para o filtro passa-alta
    mascara = np.zeros((linhas, colunas), np.uint8)
    mascara[cLinha - freq_corte:cLinha + freq_corte,
            cColuna - freq_corte:cColuna + freq_corte] = 1

    # Aplica a máscara na transformada de Fourier
    fshift_filtrada = fshift * mascara

    # Transforma a transformada de Fourier filtrada de volta para o domínio espacial
    f_ishift = np.fft.ifftshift(fshift_filtrada)
    img_filtrada = np.fft.ifft2(f_ishift)
    img_filtrada = np.abs(img_filtrada)

    return img_filtrada


# Carrega aigem
# Carrega a imagem em escala de cinza
img = cv2.imread('./images/camera.tif', 0)

# Aplica o filtro
freq_corte = 20
img_filtrada = filtro_passa_alta(img, freq_corte)

# Eibe a imagem original e a imagem filtrada
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Imagem original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(img_filtrada, cmap='gray')
plt.title('Imagem filtrada'), plt.xticks([]), plt.yticks([])
plt.show()
