import math


class NumbersShouldNotHaveSameSign(Exception):
    pass


class AndBshouldBeNumbers(Exception):
    pass


def func1(x):
    return math.pow(x, 3) + 3 * x - 5


def func2(x):
    return pow(math.e, x) - 2 * x - 2


def bisection(a, b, f):
    try:
        a = float(a)
        b = float(b)

    except ValueError:
        raise AndBshouldBeNumbers("Input should be numbers")

    if f(a) * f(b) >= 0:
        raise NumbersShouldNotHaveSameSign("Numbers should not have the same sign")
    c = 0
    while abs(b - a) >= 0.01:
        c = (a + b) / 2
        if f(c) == 0.0:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return f"{c:.4f}"


