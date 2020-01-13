#!/usr/bin/env python3

from typing import Callable, Sequence

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import cholesky, solve_triangular

# ustawienia matplotlib dla lepszego wyświetlania w LaTeX.
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})


N = 14
DOKLADNOSC_PRZEDZIALU = 30


def f(x: float) -> float:
    """Funkcja interpolowana."""
    return 1 / (1 + 25 * x**2)

def s(xi, xi1, yi, yi1, ksi, ksi1) -> Callable:
    def wielomian(x) -> Callable:
        A = (xi1 - x) / (xi1 - xi)
        B = (x - xi) / (xi1 - xi)
        C = ((A**3 - A) * (xi1 - xi)**2) / 6
        D = ((B**3 - B) * (xi1 - xi)**2) / 6
        w = A*yi + B*yi1 + C*ksi + D*ksi1
        return w
    return wielomian


def wezly_jednorodne() -> Sequence[float]:
    """Lista jednorodnych węzłów interpolacji."""
    return [-1 + 2*(i/(N)) for i in range(N+1)]


def wartosci_ksi(yi: Sequence[float]) -> Sequence[float]:
    A = np.diagflat([4]*(N-1), k=0) +\
        np.diagflat([1]*(N-2), k=-1) +\
        np.diagflat([1]*(N-2), k=1)
    C = cholesky(A, lower=True)

    b = [yi[i] - 2*yi[i+1] + yi[i+2] for i in range(N-1)]
    h = 2/N
    b = np.multiply(6/h**2, b)

    y = solve_triangular(C, b, lower=True)
    x = solve_triangular(C.T, y, lower=False)
    # x ma wartości ksi od drugiego do przedostatniego
    # dla naturalnego splajnu kubicznego pierwsza i ostatnia wartość wynosi 0
    Ksi = [0, *x, 0]
    return Ksi


if __name__ == "__main__":

    # przestrzeń liniowa <-1, 1> próbkowana parametrem num
    linspace = np.linspace(-1, 1, num=DOKLADNOSC_PRZEDZIALU*(N))


    # ustawienie wykresu
    plt.figure(figsize=(5.5, 3.5))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.suptitle('Naturalny splajn kubiczny')
    plt.title('N = {}'.format(N))

    # rysowanie funkcji f
    plt.plot(linspace, list(map(f, linspace)), 'r--')


    # punkty sklejania
    xi = wezly_jednorodne()
    yi = [f(x) for x in xi]

    # drugie pochodne wielomianów
    Ksi = wartosci_ksi(yi)

    # rysowanie wielomianów w przedziałach
    for pkt_sklejenia in range(N):
        x_0 = xi[pkt_sklejenia]
        x_1 = xi[pkt_sklejenia+1]
        y_0 = yi[pkt_sklejenia]
        y_1 = yi[pkt_sklejenia+1]
        ksi_0 = Ksi[pkt_sklejenia]
        ksi_1 = Ksi[pkt_sklejenia+1]

        wielomian = s(x_0, x_1, y_0, y_1, ksi_0, ksi_1)
        przedzial = np.linspace(x_0, x_1, num=DOKLADNOSC_PRZEDZIALU)

        plt.plot(przedzial, list(map(wielomian, przedzial)))

    # plt.show()
    filename = '_'.join(['spline', 'N', str(N)])
    plt.savefig(filename + '.pgf')
