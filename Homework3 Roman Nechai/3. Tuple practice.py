# 1
lst1 = ['a', 'b', 'c']


def list_to_tuple(lst):
    return tuple(lst)


print(list_to_tuple(lst1))

# 2
tuple1 = ('a', 'b', 'c')


def tuple_to_list(lst):
    return list(lst)


print(tuple_to_list(lst1))

# 3


def assignment():
    a, b, c = ('a', 2, 'python')
    return f'a=\'{a}\', b={b}, c=\'{c}\''


print(assignment())

# 4
tuple2 = (4,)
print(len(tuple2))


def range_tuple(tpl):
    result = []
    for i in range(1, tpl[0]):
        result.append(i)
    return result


print(range_tuple(tuple2))
