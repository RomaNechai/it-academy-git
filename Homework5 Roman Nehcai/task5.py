def get_counter():
    counter = 0

    def count():
        nonlocal counter
        counter += 1
        return counter
    return count


result = get_counter()
print(result())
print(result())
print(result())
