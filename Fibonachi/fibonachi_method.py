class Fibonachi:
    def __init__(self, a, b, n, deb=False, e=1e-2, r=3):
        self.__left = a
        self.__right = b
        self.__n = n
        self.__deb = deb
        self.__e = e
        self.__r = r
        self.__result = self.method_fibonachi()

    def __str__(self):
        return f'Кол-во операций {self.__result[1]}\nПогрешность {self.__e}\nПриблизительное значение {self.__result[0]}'

    def function(self, x):
        return x ** 2 - 4 * x + 6

    def fib(self, n):
        f1, f2 = 1, 1
        for i in range(2, n + 1):
            f1, f2 = f2, f1 + f2
        return f2

    def method_fibonachi(self):
        k, sl, sr, n, e, r = 0, self.__left, self.__right, self.__n, self.__e, self.__r
        y = round(sl + self.fib(n - 2) * (sr - sl) / self.fib(n), r)
        z = round(sl + self.fib(n - 1) * (sr - sl) / self.fib(n), r)
        if self.__deb:
            print(f'a{k} = {sl};  b{k} = {sr}')
            print(f'y{k} = {y};  z{k} = {z}')
        while k - 1 != n - 3:
            if self.__deb:
                print(f'\nF(y{k}) = {round(self.function(y), r)};  F(z{k}) = {round(self.function(z), r)}')
            if self.function(y) <= self.function(z):
                sr = z
                z = y
                y = round(sl + self.fib(n - k - 3) * (sr - sl) / self.fib(n - k - 1), r)
            else:
                sl = y
                y = z
                z = round(sl + self.fib(n - k - 2) * (sr - sl) / self.fib(n - k - 1), r)
            k += 1
            if self.__deb:
                print(f'a{k} = {sl};  b{k} = {sr}')
                print(f'y{k} = {y};  z{k} = {z}')

        y = z
        z = round(y + e, r)
        if self.function(y) < self.function(z):
            sr = z
        else:
            sl = y
        k += 1
        if self.__deb:
            print(f'\ny{k} = {y};  z{k} = {z}')
            print(f'F(y{k}) = {round(self.function(y), r)};  F(z{k}) = {round(self.function(z), r)}')
            print(f'a{k} = {sl};  b{k} = {sr}')
        return (sl + sr) / 2, k + 1
