num_lst = [1, 0, 0, 7, 2, 2, 1, 0, 0, 2, 0, 3, 4]
n = len(num_lst)
zero = num_lst.count(0)

# def zero_transfer(lst):
#     count = 0
#     while 0 in lst:
#         count += 1
#         lst.remove(0)
#     return lst + ([0] * count)


def zero_transfer(lst):
    counter = 0
    for value in lst:
        if value > 0:
            counter += 1
            if counter <= (n - zero):
                lst.append(value)
    return lst[n:] + ([0] * zero)


print(zero_transfer(num_lst))
