import math


def function(x):
    x1, x2 = x
    return round(x1 ** 2 + 5 * x2 ** 2 + x1 * x2 + x1, 4)


def function_gradient(x):
    x1, x2 = x
    return round(2 * x1 + x2 + 1, 4), round(10 * x2 + x1, 4)


def hesse():
    return [[2, 1], [1, 10]]


def determinant(h):
    return h[0][0] * h[1][1] - h[0][1] * h[1][0]


def tr_hesse(h):
    det = determinant(h)
    matrix_tr = [[h[1][1], -h[0][1]],
                 [-h[1][0], h[0][0]]]
    return [[round(el[0] / det, 4), round(el[1] / det, 4)] for el in matrix_tr]


def function_tk(x):
    x1, x2 = x
    t1 = round((2 * x1 + x2 + 1) ** 2 + (10 * x2 + x1) ** 2, 4)
    t2 = round(2 * (2 * x1 + x2 + 1) ** 2 + 10 * (10 * x2 + x1) ** 2 + 2 * (2 * x1 + x2 + 1) * (10 * x2 + x1), 4)
    t = round(t1 / t2, 4)
    print(f'\t\t{t1}')
    print(f'\ttk= ------')
    print(f'\t\t{t2}')
    return t


def newton_method(param):
    print(f'Функция: f(x) = x1^2 + 5x2^2 + x1x2 + x1 \n    \t\tg(x) = 2x1 + 3x2')
    k, x, f, g = 0, [0, 0], 0, 0
    while k < 6:
        print(f'\nk = {k}')

        if k == 5:
            print(f'rk = oo')
            x[0] = 1
        else:
            print(f'rk = {param[k]}')
            x[0] = param[k] ** k / (1 + param[k] ** k)
        x[1] = (x[0] + 0.2) / 0.6
        print(f'x = {x}')

        f = (2 * x[0] ** 2 + x[1] ** 2 - x[0] * x[1] + x[0])
        if k != 5:
            f += param[k] ** k / 2 * (x[0] + x[1] - 3) ** 2
        print(f'F = {f}')

        if k == 5:
            g = -3
        else:
            g = param[k] * (x[0] + x[1] - 3)
        print(f'rk = {g}')

        k += 1


if __name__ == "__main__":
    newton_method([1, 2, 10, 100, 1000])
