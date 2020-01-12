from typing import Sequence
import numpy as np
from scipy.linalg import cholesky, solve_triangular

N = 8


def y(x):
    return 1 / (1 + 25 * x**2)


def wezly_jednorodne():
    """Lista jednorodnych węzłów interpolacji."""
    return [-1 + 2*(i/(N)) for i in range(N+1)]


def wartosci_ksi(f: Sequence[float]):
    A = np.diagflat([4]*(N-2), k=0) +\
        np.diagflat([1]*(N-3), k=-1) +\
        np.diagflat([1]*(N-3), k=1)
    C = cholesky(A, lower=True)
    b = [f[i] - 2*f[i+1] + f[i+2] for i in range(N-2)]

    y = solve_triangular(C, b, lower=True)
    x = solve_triangular(C.T, y, lower=False)
    return x


if __name__ == "__main__":
