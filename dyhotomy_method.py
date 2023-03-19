class DyhotomyMethod:
    def __init__(self, a, b, deb=False, e=5e-1, step=2e-1):
        self.__left = a
        self.__right = b
        self.__deb = deb
        self.__e = e
        self.__step = step
        self.__result = self.dyhotomy()

    def __str__(self):
        return f'Кол-во операций {self.__result[1]}\nПогрешность {self.__e}\nПриблизительное значение {self.__result[0]}'

    def function(self, x):
        return x ** 2 - 4 * x + 6

    def dyhotomy(self):
        k, sl, sr, e, step = 0, self.__left, self.__right, self.__e, self.__step
        while abs(sr - sl) > 2 * e:
            x = (sl + sr - step) / 2
            y = (sl + sr + step) / 2
            if self.__deb:
                print(f'x{k} {x}    y{k} {y}')
                print(f'a{k} {sl}    b{k} {sr}')
                print(f'f(x{k}) {self.function(x)}    f(y{k}) {self.function(y)}')
            if self.function(x) < self.function(y):
                sr = y
            else:
                sl = x
            k += 1
        return (sl + sr) / 2, k
