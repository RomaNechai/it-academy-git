def get_limit(func):
    counter = 3

    def wrapper(*args, **kwargs):
        nonlocal counter
        while counter != 0:
            counter -= 1
            print(counter)
            return func(*args, **kwargs)
        return 'Лимит вызовов исчерпан'
    return wrapper


def say_hello():
    return 'Hello!'


result = get_limit(say_hello)

print(result())
print(result())
print(result())
print(result())
