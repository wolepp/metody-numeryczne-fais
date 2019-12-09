"""Prototyp zadania numerycznego NUM5."""

N = 100
ITERATION_LIMIT = 10000

def a(i, j):
    """Generuje wartości aij z macierzy A."""
    if i == j:
        return 3
    if abs(i - j) == 1:
        return 1
    if abs(i - j) == 2:
        return 0.2
    return 0


def b(i):
    """Generuje wartości bi z wektora b."""
    return i+1

def is_converged(vec_a: list, vec_b: list, desired_conv: float):
    for i in range(len(vec_a)):
        if abs(vec_a[i] - vec_b[i]) > desired_conv:
            return False
    return True


def jacobi(desired_conv: float = 10e-15, start: list = [0 for elem in range(N)]):

    x = list(start)
    x_new = list(x)
    for iteration in range(ITERATION_LIMIT):
        x_new[0] = 1/a(0, 0) * (b(0) - 0 - (a(0, 1)*x[1] + a(0, 2)*x[2]))
        x_new[1] = 1/a(1, 1) * (b(1) - (a(1, 0)*x[0]) - (a(1, 2)*x[2] + a(1, 3)*x[3]))
        x_new[N-2] = 1/a(N-2, N-2) * (b(N-2) - (a(N-2, N-4) * x[N-4] + a(N-2, N-3)*x[N-3]) - (a(N-2, N-1)*x[N-1]))
        x_new[N-1] = 1/a(N-1, N-1) * (b(N-1) - (a(N-1, N-3) * x[N-3] + a(N-1, N-2)*x[N-2]) - 0)
        for i in range(2, N-2):
            s1 = (a(i, i-2)*x[i-2] + a(i, i-1)*x[i-1])
            s2 = (a(i, i+1)*x[i+1] + a(i, i+2)*x[i+2])
            x_new[i] = 1/a(i, i) * (b(i) - s1 - s2)
        
        if is_converged(x_new, x, desired_conv):
            break
        x = list(x_new)
    return x_new

def gauss_seidel(desired_conv: float = 10e-15, start: list = [0 for elem in range(N)]):
    x = list(start)
    for iteration in range(ITERATION_LIMIT):
        x_old = list(x)
        x[0] = 1/a(0, 0) * (b(0) - 0 - (a(0, 1)*x[1] + a(0, 2)*x[2]))
        x[0] = 1/a(0, 0) * (b(0) - a(0, 1)*x[1] - a(0, 2)*x[2])
        x[1] = 1/a(1, 1) * (b(1) - a(1, 0)*x[0] - a(1, 2)*x[2] - a(1, 3)*x[3])
        for i in range(2, N-2):
            s1 = a(i, i-2)*x[i-2] + a(i, i-1)*x[i-1]
            s2 = a(i, i+1)*x[i+1] + a(i, i+2)*x[i+2]
            x[i] = 1/a(i, i) * (b(i) - s1 - s2)
        x[N-2] = 1/a(N-2, N-2) * (b(N-2) - a(N-2, N-4)*x[N-4] - a(N-2, N-3)*x[N-3] - a(N-2, N-1)*x[N-1])
        x[N-1] = 1/a(N-1, N-1) * (b(N-1) - a(N-1, N-3)*x[N-3] - a(N-1, N-2)*x[N-2])

        if is_converged(x, x_old, desired_conv):
            break
    return x


if __name__ == '__main__':
    jacob = jacobi()
    gs = gauss_seidel()
    for i in range(len(jacob)):
        print ("{}\t{}\t{}".format(jacob[i], gs[i], abs(jacob[i] - gs[i])))
        