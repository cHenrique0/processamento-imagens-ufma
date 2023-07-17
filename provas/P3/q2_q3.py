import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("./images/blurry_moon.tif", 0)

f = img / 255  # Normaliza a imagem

# Transformada de Fourier
F = np.fft.fft2(f)
fShift = np.fft.fftshift(F)

# laplaciano
P, Q = F.shape
H = np.ones((P, Q), dtype=np.float32)
for u in range(P):
    for v in range(Q):
        H[u, v] = -4*np.pi*np.pi*((u-P/2)**2 + (v-Q/2)**2)

# Laplace
Lap = H * F
Lap = np.fft.ifftshift(Lap)
Lap = np.real(np.fft.ifft2(Lap))
oldRange = np.max(Lap) - np.min(Lap)
newRange = 1 - -1
LapScaled = (((Lap - np.min(Lap)) * newRange) / oldRange) + -1
c = -1
g = f + c*LapScaled
g = np.clip(g, 0, 1)

plt.imshow(g, cmap="gray")
plt.axis("off")
plt.show()
