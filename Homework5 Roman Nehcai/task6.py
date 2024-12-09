i = 5


def multiply(n):
    def inner(m):
        return n * m
    return inner


prod = multiply(i)
print(prod(5))
print(prod(prod(2)))
