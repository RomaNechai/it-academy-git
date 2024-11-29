nums = [84, 90] # 6
nums = [140, 96] # 4
nums = [24, 8] # 8


def find_gcd(lst):
    a, b = lst
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


print(find_gcd(nums))