nums_lst1 = [17, 12, 31, 7, 9]
nums_lst2 = [17, 19, 32, 7, 8]


def unic_nums(lst1, lst2):
    nums_set1 = set(lst1)
    nums_set2 = set(lst2)
    return len(nums_set1.difference(nums_set2))


print(unic_nums(nums_lst1, nums_lst2))
