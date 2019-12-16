import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# ustawienia dla lepszego wyświetlania w LaTeX.
# matplotlib.use("pgf")
# matplotlib.rcParams.update({
#     "pgf.texsystem": "pdflatex",
#     'font.family': 'serif',
#     'text.usetex': True,
#     'pgf.rcfonts': False,
# })


def y(x):
    return 1 / (1 + 25 * x**2)


def y_prim(x):
    return 1 / (1 + x**2)


def wezly_jednorodne(n: int):
    """Lista jednorodnych węzłów interpolacji."""
    return [-1 + 2*(i/(n+1)) for i in range(n+1)]


def wezly_cos(n: int):
    """Lista węzłów interpolacji z funkcją cos."""
    return [math.cos((2*i+1) / (2*(n+1)) * math.pi) for i in range(n+1)]


def l(i: int, xlist: list):
    def lj(x):
        prod = 1
        xi = xlist[i]
        for j, xj in enumerate(xlist):
            if j != i:
                prod *= (x-xj)/(xi-xj)
        return prod
    return lj


def W(xlist: list, f: callable) -> callable:
    return lambda x: sum([l(j, xlist)(x) * f(xj) for j, xj in enumerate(xlist)])


if __name__ == "__main__":
    ZNANY_PUNKT = wezly_jednorodne(4)[1]
    assert y(ZNANY_PUNKT) == W(wezly_jednorodne(4), y)(ZNANY_PUNKT)

    ZESTAWY_PUNTKOW = [
        [6, 8, 16, 32],
        [6, 64],
        [5, 7, 15, 31]
    ]

    x = np.linspace(-1, 1, 200)
    for zp in ZESTAWY_PUNTKOW:
        plt.axes().set_ylim([-0.5, 1.5])
        plt.plot(x, [y(x_) for x_ in x], label='y(x)')
        for N in zp:
            wezly = wezly_jednorodne(N)
            wielomian = W(wezly, y)
            plt.plot(wezly, [wielomian(x_) for x_ in wezly], '.')
            plt.plot(x, [wielomian(x_) for x_ in x], label='W{}(x)'.format(N))

        plt.xlabel('x')
        plt.ylabel('Wn(x)')
        plt.title("Wielomiany Lagrange'a dla N={}".format(zp))
        plt.legend()
        plt.show()
