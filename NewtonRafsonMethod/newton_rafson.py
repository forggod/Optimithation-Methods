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
    t1 = round((4 * x1 + x2) ** 2 + (x1 + 2 * x2) ** 2, 4)
    t2 = round(4 * (4 * x1 + x2) ** 2 + 2 * (4 * x1 + x2) * (x1 + 2 * x2) + 2 * (x1 + 2 * x2) ** 2, 4)
    t = round(t1 / t2, 4)
    print(f'\t\t{t1}')
    print(f'\ttk= ------')
    print(f'\t\t{t2}')
    return t


def newton_method(x, m=50, e1=1e-2, e2=105e-3):
    print(f'Функция: f(x) = x1^2 + 5x2^2 + x1x2 + x1')
    print(f'\tx0 = ({x[0]}, {x[1]})\n   \tM = {m}\n   \te1 = {e1}\n   \te2 = {e2}')
    k, xk, dk = 0, 0, 0
    while True:
        print(f'\nk = {k}')
        fg = function_gradient(x)
        print(f'\tШаг 3. {fg}')

        norma = round(math.sqrt(fg[0] ** 2 + fg[1] ** 2), 4)
        print(f'\tШаг 4. {norma} < {e1} ?')
        if norma < e1:
            print(f'x = {x}')
            return x, k

        print(f'\tШаг 5. {k} >= {m} ?')
        if k >= m:
            print(f'x = {x}')
            return x, k

        h = hesse()
        print(f'\tШаг 6. \t{h[0]}')
        print(f'\t\t\t{h[1]}')

        ht = tr_hesse(h)
        print(f'\tШаг 7. \t{ht[0]}')
        print(f'\t\t\t{ht[1]}')

        det_ht = determinant(ht)
        print(f'\tШаг 8. {det_ht} > 0 ?')
        if det_ht > 0:
            dk = [round(-el[0] * fg[0] - el[1] * fg[1], 4) for el in ht]
        else:
            dk = [-el for el in fg]

        xk = [round(x[i] + dk[i], 4) for i in [0, 1]]
        print(f'\tШаг 9. {x}')

        tk = function_tk(xk)
        print(f'\tШаг 10. {tk}')

        xk = [round(x[i] + tk * dk[i], 4) for i in [0, 1]]
        print(f'\tШаг 11. {xk}')

        f, s = round(math.sqrt((xk[0] - x[0]) ** 2 + (xk[1] - x[1]) ** 2), 4), \
            round(abs(function(xk) - function(x)), 4)
        print(f'\tШаг 12. {f} < {e2} and {s} < {e2} ?')
        if f < e2 and s < e2:
            print(f'\tx = {xk}')
            return xk, k
        x = xk
        k += 1


x0 = [1, 1]
method = newton_method(x0)
print()
print(f'Кол-во итераций: {method[1]}')
print(f'Значение точки: x = {method[0]}')
