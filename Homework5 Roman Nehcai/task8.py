lst = [0, ['one', 'two', [3, 4, [True, False]]], 1, ['five', 'six', []]]
counter = 0
lst1 = []


def count_list(array):
    global counter
    for value in array:
        if isinstance(value, list):
            counter += 1
            count_list(value)
    lst1.append(counter)
    print(lst1)
    counter = 0
    return max(lst1)


print(count_list(lst))
