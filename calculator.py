def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError as error:
        return "Invalid value for denominator, cant't divide by 0!"


def multiply(x, y):
    return x * y


def square(x):
    x = abs(x ** 2)
    return x


def power(x, y):
    z = abs(x ** y)
    return z


def sqrt(x):
    z = sqrt(abs(x))
    return z
