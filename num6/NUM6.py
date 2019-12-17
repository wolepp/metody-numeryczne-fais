import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# ustawienia matplotlib dla lepszego wyświetlania w LaTeX.
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})


def y(x):
    y.tex_str = "$\\frac{1}{1+25x^{2}}$"
    y.str = 'y'
    return 1 / (1 + 25 * x**2)


def y_prim(x):
    y_prim.tex_str = "$\\frac{1}{1+x^{2}}$"
    y_prim.str = 'y_prim'
    return 1 / (1 + x**2)


def wezly_jednorodne(n: int):
    """Lista jednorodnych węzłów interpolacji."""
    wezly_jednorodne.str = 'wezly_jedn'
    return [-1 + 2*(i/(n+1)) for i in range(n+1)]


def wezly_cos(n: int):
    """Lista węzłów interpolacji z funkcją cos."""
    wezly_cos.str = 'wezly_cos'
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
        [2, 4],
        [6, 8, 16, 32],
        [6, 64],
        [5, 7, 15, 31]
    ]
    FUNKCJE = [y, y_prim]
    FUNKCJE_WEZLOW = [wezly_jednorodne, wezly_cos]

    x = np.linspace(-1, 1, 200)

    for nr_zestawu, zestaw_punktow in enumerate(ZESTAWY_PUNTKOW):
        for f in FUNKCJE:
            for fw in FUNKCJE_WEZLOW:

                plt.axes().set_ylim([-0.5, 1.5])
                plt.plot(x, [f(x_) for x_ in x], label='$y(x)=$' + f.tex_str)

                for N in zestaw_punktow:
                    wezly = fw(N)
                    wielomian = W(wezly, f)
                    plt.plot(wezly, [wielomian(x_) for x_ in wezly], '.')
                    plt.plot(x, [wielomian(x_) for x_ in x], label=f'W{N}(x)')

                plt.xlabel('x')
                plt.ylabel('y')
                plt.title("Wielomiany Lagrange'a dla N={}".format(
                    ', '.join([str(n) for n in zestaw_punktow])))
                plt.legend()

                filename = 'plots/' + '_'.join(
                    ['plot', fw.str, f.str, 'nr', str(nr_zestawu+1)])
                plt.savefig(filename + '.pgf')
                # plt.show()
