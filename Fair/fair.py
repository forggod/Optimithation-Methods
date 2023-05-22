import math


def function(x):
    x1, x2 = x
    return round(x1 ** 2 + 5 * x2 ** 2 + x1 * x2 + x1, 4)


def fair_method(param):
    print(f'Функция: f(x) = x1^2 + 5x2^2 + x1x2 + x1 \n    \t\tg(x) = 2x1 + 3x2')
    k, x, f, g = 0, [0, 0], 0, 0
    while k < 6:
        print(f'\nk = {k}')

        if k == 5:
            print(f'rk = oo')
            x[0] = 1
        else:
            print(f'rk = {param[k]}')
            x[0] = param[k] / (1 + param[k])
        x[1] = (4 * x[0] + 3) / 17
        print(f'x = {x}')

        f = x[0]**2 + 5*x[1]**2 + x[0]*x[1] + x[0]
        if k != 5:
            f += (param[k] * (2 * x[0] + 3 * x[1]) ** 2) / 2
        print(f'F = {f}')

        if k == 5:
            g = 0
        else:
            g = param[k] * (2*x[0] + 3*x[1])
        print(f'l1(rk) = {g}')

        k += 1


if __name__ == "__main__":
    fair_method([1, 2, 10, 100, 1000])
