def function(x):
    return x ** 2 + 20 * x + 34


def svens_algorithm(x0=1):
    t, k = 1, 0
    f = [function(x0 - t), function(x0), function(x0 + t)]
    if f[0] >= f[1] <= f[2]:
        return x0 - t, x0 + t
    elif f[0] <= f[1] >= f[2]:
        print(f"Выберите другую точку x0 != {x0}")
    else:
        dx = 0
        a0, b0, xk = 0, 0, 0
        if f[0] >= f[1] >= f[2]:
            dx = t
            a0 = x0
            xk = x0 + t
            k += 1
        elif f[0] <= f[1] <= f[2]:
            dx = -t
            b0 = x0
            xk = x0 - t
            k += 1
        while f[xk] < f[x0]:
            xk, x0 = x0 + 2 ** k * dx, xk
            if dx == t:
                a0 = x0
            else:
                b0 = x0
            k += 1
        if dx == t:
            b0 = xk
        else:
            a0 = xk
        return a0, b0, k + 1


if __name__ == '__main__':
    print(svens_algorithm())
    print(function(-14), function(-6))
