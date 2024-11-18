lst = ['one', 'two', 'one', True, 'three', 3, 3, True, 'one', 'five']


def unic_elt(lst1):
    unic_lst = []
    for i in lst1:
        if lst1.count(i) == 1:
            unic_lst.append(i)
    return unic_lst


print(unic_elt(lst))
