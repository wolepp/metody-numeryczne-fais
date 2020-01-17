#!/usr/bin/env python3

import numpy as np
from scipy import linalg

RTOL = 10e-11
ATOL = 10e-13


def wektoryZbiezne(x, y):
    """
    Funkcja sprawdza, czy wektory x i y są do siebie zbliżone
    z dokładnością RTOL i ATOL w poniższy sposób:
    absolute(x - y) <= (ATOL + RTOL * absolute(y)).
    """
    return np.allclose(x, y, rtol=RTOL, atol=ATOL)


def algorytmQR(A):
    A_old = A.copy()
    Q, R = linalg.qr(A)
    A = np.dot(R, Q)
    i = 0
    while not wektoryZbiezne(np.diag(A), np.diag(A_old)):
        i += 1
        A_old = A
        Q, R = linalg.qr(A)
        A = np.dot(R, Q)
    return np.diag(A), i


def metodaPotegowa(A):
    y = np.ones(A.shape[1])
    y_old = y.copy()

    z = np.dot(A, y)
    y = z / np.linalg.norm(z)
    i = 0
    while not wektoryZbiezne(y, y_old):
        i += 1
        y_old = y
        z = np.dot(A, y)
        y = z / np.linalg.norm(z)
    return np.linalg.norm(z), i


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

    print('Wartości własne macierzy M:')
    eigenM = linalg.eigvals(M)
    print('{} : SciPy'.format(np.real(eigenM[::-1])))
    eigenQR, iteracjiQR = algorytmQR(M)
    print('{} : QR, {} iteracji'.format(eigenQR, iteracjiQR))

    print()
    print('Największa wartość własna macierzy B:')
    maxEigen = linalg.eigh(B, eigvals_only=True)[-1]
    print('{} : SciPy'.format(maxEigen))
    eigenPot, iteracjiPot = metodaPotegowa(B)
    print('{} : met. potegowa, {} iteracji'.format(eigenPot, iteracjiPot))
