from typing import Sequence
import numpy as np
from scipy.linalg import cholesky, solve_triangular

N = 8


def f(x):
    return 1 / (1 + 25 * x**2)

def s(x):
    pass

def wezly_jednorodne():
    """Lista jednorodnych węzłów interpolacji."""
    return [-1 + 2*(i/(N)) for i in range(N+1)]


def wartosci_ksi(yi: Sequence[float]):
    A = np.diagflat([4]*(N-2), k=0) +\
        np.diagflat([1]*(N-3), k=-1) +\
        np.diagflat([1]*(N-3), k=1)
    C = cholesky(A, lower=True)

    b = [yi[i] - 2*yi[i+1] + yi[i+2] for i in range(N-2)]
    h = 2/N
    b = np.multiply(6/h**2, b)

    y = solve_triangular(C, b, lower=True)
    x = solve_triangular(C.T, y, lower=False)
    # x ma wartości ksi od drugiego do przedostatniego
    # dla naturalnego splajnu kubicznego pierwsza i ostatnia wartość wynosi 0
    Ksi = [0, *x, 0]
    return Ksi


if __name__ == "__main__":
    ksi = wartosci_ksi([f(x) for x in wezly_jednorodne()])
    print(ksi)
    print(type(ksi))