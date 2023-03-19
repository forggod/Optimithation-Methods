from dyhotomy_method import DyhotomyMethod
from golden_ratio_method import GoldenRatio
from fibonachi_method import Fibonachi

if __name__ == '__main__':
    dyh = DyhotomyMethod(0, 10)
    gora = GoldenRatio(0, 10)
    fib = Fibonachi(0, 10, 6)
    print("Метод дихотомии")
    print(dyh)
    print("\nМетод золотого сечения")
    print(gora)
    print("\nМетод Фибоначчи")
    print(fib)
