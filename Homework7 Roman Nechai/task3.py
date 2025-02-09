# nums = [2, 7, 11, 15]
# target = 9

# nums = [3, 2, 4]
# target = 6
# nums = [3, 3]
# target = 6
nums = [2, 2]
target = 4


def get_items(lst, num):
    for i in lst:
        for j in lst[1:]:
            if i + j == num:
                return [lst.index(i), lst.index(j, 1)]
    return 'Совпадений не найдено'


print(get_items(nums, target))
