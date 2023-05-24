import numpy as np
from scipy.optimize import minimize


def objective(x):
    return x[0] ** 2 + 5 * x[1] ** 2 + x[0] * x[1] + x[0]


def equality_constraint(x):
    return 2 * x[0] + 3 * x[1] - 1


def inequality_constraint(x):
    return -2 * x[0] - 3 * x[1] + 1


def penalty(x, r):
    return r / 2 * (equality_constraint(x) ** 2 + max(0, inequality_constraint(x)) ** 2)


def objective_with_penalty(x, r):
    return objective(x) + penalty(x, r)


x = np.array([1, 1])
r = 1
C = 10
epsilon = 0.01
k = 0

print("{:<10s} {:<20s} {:<20s} {:<20s} {:<20s}".format("rk", "x1", "x2", "F(x,rk)", "f(x)"))

while True:
    solution = minimize(objective_with_penalty, x, args=(r,), method='Nelder-Mead')

    x_star = solution.x
    penalty_value = penalty(x_star, r)

    print("{:<10d} {:<20.4f} {:<20.4f} {:<20.4f} {:<20.4f}".format(r, x_star[0], x_star[1],
                                                                   objective_with_penalty(x_star, r),
                                                                   objective(x_star)))

    if penalty_value <= epsilon:
        break
    else:
        r = C * r
        x = x_star
        k = k + 1

print("\nx = [{:.4f}, {:.4f}] \nF(x8) = {:.4f}".format(x_star[0], x_star[1], objective(x_star)))
