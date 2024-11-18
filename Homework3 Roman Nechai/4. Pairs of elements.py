string = '1 1 1 2 2 3 2 3 4 4 5'


def pairs(some_str):
    lst = string.split()
    pair_cnt = 0
    for i, value_i in enumerate(lst):
        for j, value_j in enumerate(lst[i+1:]):
            if value_i == value_j:
                pair_cnt += 1
    return pair_cnt


print(pairs(string))
