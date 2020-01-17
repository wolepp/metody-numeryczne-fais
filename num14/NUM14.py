#!/usr/bin/env python3

import numpy as np
from scipy import linalg

RTOL = 10e-11
ATOL = 10e-13


def zbieznaDiag(A, B):
    diagA = np.diag(A)
    diagB = np.diag(B)
    return np.allclose(diagA, diagB, rtol=RTOL, atol=ATOL)


def algorytmQR(A):
    A_old = A.copy()
    Q, R = linalg.qr(A)
    A = np.dot(R, Q)
    i = 0
    while not zbieznaDiag(A, A_old):
        i += 1
        A_old = A
        Q, R = linalg.qr(A)
        A = np.dot(R, Q)
    return np.diag(A), i


if __name__ == "__main__":
    M = np.array([
        [3,   6,   6,  9],
        [1,   4,   0,  9],
        [0, 0.2,   6, 12],
        [0,   0, 0.1,  6]
    ])

    B = np.array([
        [3, 4, 2, 4],
        [4, 7, 1, -3],
        [2, 1, 3, 2],
        [4, -3, 2, 2]
    ])

    print('Macierz M:')
    eigenM = linalg.eigvals(M)
    print('{} : SciPy'.format(np.real(eigenM[::-1])))
    eigenQR, iteracjiQR = algorytmQR(M)
    print('{} : QR, {} iteracji'.format(eigenQR, iteracjiQR))
