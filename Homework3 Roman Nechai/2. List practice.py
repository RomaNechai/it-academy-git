# 1

lst1 = 'ab'
lst2 = 'bcd'


def mix_str(str1, str2):
    return [i + j for i in str1 for j in str2]


print(mix_str(lst1, lst2))

# 2
print(mix_str(lst1, lst2)[::2])

# 3
a_lst = 'a'


def mix_int_str(lst):
    return [str(i) + lst for i in range(1, 5)]


print(mix_int_str(a_lst))

# 4
cut_lst = mix_int_str(a_lst)
print(cut_lst.pop(1))

# 5


def full_lst(lst):
    new_lst = lst.copy()
    new_lst.insert(1, '2a')
    print(lst)
    return new_lst


print(full_lst(cut_lst))
