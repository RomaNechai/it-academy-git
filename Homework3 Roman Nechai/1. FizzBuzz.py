lst = [n for n in range(1, 101)]


def funny_func(value):
    new_lst = []
    for i in value:
        if i % 3 == 0 and i % 5 == 0:
            i = 'FizzBuzz'
        elif i % 3 == 0:
            i = 'Fizz'
        elif i % 5 == 0:
            i = 'Buzz'
        new_lst.append(i)
    return new_lst


print(*funny_func(lst))
