import math


def function(x):
    x1, x2 = x
    return round(x1 ** 2 + 5 * x2 ** 2 + x1 * x2 + x1, 4)


def function_gradient(x):
    x1, x2 = x
    return [round(2 * x1 + x2 + 1, 4),
            round(10 * x2 + x1, 4)]


def function_tk(x):
    x1, x2 = x
    t1 = round((2 * x1 + x2 + 1) ** 2 + (10 * x2 + x1) ** 2, 4)
    t2 = round(2 * (2 * x1 + x2 + 1) ** 2 + 10 * (10 * x2 + x1) ** 2 +
               2 * (2 * x1 + x2 + 1) * (10 * x2 + x1), 4)
    t = round(t1 / t2, 4)
    print(f'\t\t{t1}')
    print(f'\ttk= ------')
    print(f'\t\t{t2}')
    return t


def fletcherReevesMethod(x, m=50, e1=1e-2, e2=105e-3):
    print(f'Функция: f(x) = x1^2 + 5x2^2 + x1x2 + x1')
    print(f'   x0 = ({x[0]}, {x[1]});\n   e1 = {e1};\n   e2 = {e2};\n   M = {m}\n')
    k, xk, d, b = 0, 0, 0, 0
    xmk = [0, 0]
    while True:
        print(f'\nk= {k}')

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
        elif k == 0:
            d = [el * -1 for el in fg]
            print(f'\tШаг 6. d0 = {d}')
        else:
            fgx = function_gradient(xmk)
            b = round((math.sqrt(fg[0] ** 2 + fg[1] ** 2) ** 2) / (math.sqrt(fgx[0] ** 2 + fgx[1] ** 2) ** 2), 4)
            print(f'\tШаг 7. b = {b}')
            d = [round(b * d[i] - fg[i], 4) for i in range(len(x))]
            print(f'\tШаг 8. d = {d}')

        tk = function_tk(x)
        print(f'\tШаг 9. t{k} = {tk}')

        xk = [round(x[0] + tk * d[0], 4), round(x[1] + tk * d[1], 4)]
        print(f'\tШаг 10. x{k + 1} = {xk}')

        f, s = round(math.sqrt((xk[0] - x[0]) ** 2 + (xk[1] - x[1]) ** 2), 4), round(abs(
            function(xk) - function(x)), 4)

        print(f'\tШаг 11. {f} < {e2} ?, {s} < {e2} ?')
        if f < e2 and s < e2:
            print(f'x = {xk}')
            return xk, k

        xmk = x
        x = xk
        k += 1


method = fletcherReevesMethod((1, 1))
print()
print(f'Кол-во итераций: {method[1]}')
print(f'Точка: x = {method[0]}')
