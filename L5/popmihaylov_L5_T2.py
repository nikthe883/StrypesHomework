from sys import argv

arguments = [int(x) for x in argv[1:]]


def power(exponent, number):
    if number == 0:
        return 1
    elif exponent == 1:
        return number
    else:
        return exponent * power(exponent, number - 1)


print(power(arguments[0], arguments[1]))
