class GoldenRatio:
    def __init__(self, a, b, deb=False, e=5e-1):
        self.__left = a
        self.__right = b
        self.__deb = deb
        self.__e = e
        self.__result = self.golden_ratio()

    def __str__(self):
        return f'Кол-во итераций {self.__result[1]}\nПогрешность {self.__e}\nПриблизительное значение {self.__result[0]}'

    def function(self, x):
        return x ** 2 - 4 * x + 6

    def golden_ratio(self):
        k, sl, sr = 0, self.__left, self.__right
        x = sl + 0.38196 * (sr - sl)
        y = sl + sr - x
        if self.__deb:
            print(f'x{k} {x}    y{k}  {y}')
        while abs(sl - sr) > 2 * self.__e:
            if self.__deb:
                print(f'a{k} {sl}   b{k}  {sr}')
                print(f'x{k} {x}   y{k}  {y}')
                print(f'f(x{k}) {self.function(x)}   f(y{k}) {self.function(y)}')
            if self.function(x) <= self.function(y):
                sr = y
                y = x
                x = sl + sr - x
            else:
                sl = x
                x = y
                y = sl + sr - y
            k += 1
        return round((sl + sr) / 2, 4), k
