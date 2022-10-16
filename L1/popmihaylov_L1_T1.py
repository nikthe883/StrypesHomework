import sys
import math

arguments = sys.argv


def solve_quadratic(*args):

    if len(args) < 3:
        return "special case"
    a, b, c = [int(x) for x in args]

    if a == 0 or b == 0 or c == 0:
        return "special case"

    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x = (-b - math.sqrt(discriminant)) / (2 * a)
        y = (-b + math.sqrt(discriminant)) / (2 * a)
        return f"{x}|{y}"

    elif discriminant == 0:
        x = -b / (2 * a)
        return x

    else:
        return "no real roots"


print(solve_quadratic(*arguments[1:]))
