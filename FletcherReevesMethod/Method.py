import math


def function(x):
    x1, x2 = x
    # return round(x1 ** 2 + 5 * x2 ** 2 + x1 * x2 + x1, 4)
    return round(2 * x1 ** 2 + x1 * x2 + x2 ** 2, 4)


def function_gradient(x):
    x1, x2 = x
    # return [round(2 * x1 + x2 + 1, 4),
    #         round(10 * x2 + x1, 4)]
    return [round(4 * x1 + x2, 4),
            round(x1 + 2 * x2, 4)]


def function_tk(x):
    x1, x2 = x
    t = round(((4 * x1 + x2) ** 2 + (x1 + 2 * x2) ** 2) / (
            4 * (4 * x1 + x2) ** 2 + 2 * (4 * x1 + x2) * (x1 + 2 * x2) + 2 * (x1 + 2 * x2) ** 2), 4)
    return t


def fletcherReevesMethod(x, m=50, e1=1e-2, e2=105e-3):
    print(f'Функция: f(x) = x1^2 + 5x2^2 + x1x2 + x1')
    print(f'   x0 = ({x[0]}, {x[1]});\n   e1 = {e1};\n   e2 = {e2};\n   M = {m}\n')
    k, xk, d, b = 0, 0, 0, 0
    xmk = 0
    while True:
        print(f'\nШаг 2. k= {k}')
        fg = function_gradient(x)
        print(f'Шаг 3. {fg}')
        norma = round(math.sqrt(fg[0] ** 2 + fg[1] ** 2), 4)
        print(f'Шаг 4. {norma} < {e1} ?')
        if norma < e1:
            print(f'x = {x}')
            return x, k
        print(f'Шаг 5. {k} >= {m} ?')
        if k >= m:
            print(f'x = {x}')
            return x, k
        elif k == 0:
            d = [el * -1 for el in fg]
            print(f'Шаг 6. d0 = {d}')
        else:
            b = round(math.sqrt(function_gradient(x)[0] ** 2 + function_gradient(x)[1] ** 2) ** 2 /
                      math.sqrt(function_gradient(xmk)[0] ** 2 + function_gradient(xmk)[1] ** 2) ** 2, 4)
            print(f'Шаг 7. b = {b}')
            d = [round(b * d[i] - fg[i], 4) for i in range(len(x))]
            print(f'Шаг 8. d = {d}')
        tk = function_tk(x)
        print(f'Шаг 9. t{k} = {tk}')
        xk = [round(x[0] - tk * fg[0], 4), round(x[1] - tk * fg[1], 4)]
        print(f'Шаг 10. x{k + 1} = {xk}')
        f, s = round(math.sqrt((xk[0] - x[0]) ** 2 + (xk[1] - x[1]) ** 2), 4), round(abs(
            function(xk) - function(x)), 4)
        print(f'Шаг 11. {f} < {e2} ?, {s} < {e2} ?')
        if f < e2 and f < e2:
            print(f'x = {xk}')
            return xk, k
        if k != 0:
            xmk = x
        x = xk
        k += 1


out = fletcherReevesMethod((0.5, 1), 10, 0.1, 0.15)
# out = fletcherReevesMethod((1, 1))
print(out[0])
