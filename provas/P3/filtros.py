import numpy as np


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
