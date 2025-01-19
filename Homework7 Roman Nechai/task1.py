# num_list = [8, 9, 9, 4]
num_list = [1, 1, 9, 9, 9, 9, 9, 1, 9, 8, 9]

# num_list = [8, 1, 9, 9, 9, 2, 9]
# num_list = [5, 9, 9, 9, 9, 1, 9, 9, 9]
# num_list = [1]


def get_summ(nums):
    if len(nums) == 1:
        if (nums[0] + 1) % 10 == 0:
            nums[0] = 0
            nums.insert(0, 1)
            return nums
        summ = nums[0] + 1
        nums[0] = summ
        return nums
    for i in reversed(range(len(nums))):
        if (nums[i] + 1) % 10 == 0:
            result = get_summ(nums[:-1])
            result.append(0)
            return result
        nums[-1] = nums[-1] + 1
        return nums
    return nums


print(get_summ(num_list))
