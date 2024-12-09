f = 3


def get_factorial(n):
    if n == 1:
        return n
    return n * get_factorial(n - 1)


print(get_factorial(f))
