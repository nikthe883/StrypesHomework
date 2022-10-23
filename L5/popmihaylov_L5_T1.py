from functools import lru_cache
from sys import argv

arguments = [int(x) for x in argv[1:]]

@lru_cache()
def fibonacci(n):
    if n in {0, 1}:
        return n
    else:
        x = fibonacci(n - 1) + fibonacci(n - 2)
    return x


seq = [fibonacci(n) for n in range(arguments[1])]
print(seq[arguments[0] - 1:arguments[1]])
