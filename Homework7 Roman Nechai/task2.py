nums = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# string = 'MCMXCIV'
# string = 'II'
# string = 'IV'
# string = 'MCMXCVII'
# string = 'IX'
# string = 'DLV'
# string = 'CDXLIV'
# string = 'I'
string = 'MMMCMXCIX'


def convert_number(s, n):
    result = []
    summ = []
    for i in s:
        result.append(n[i])
    for j in range(len(result)):
        if j != len(result):
            try:
                if result[j] < result[j+1]:
                    summ.append(result[j+1] - result[j])
                    result.pop(j)
                else:
                    summ.append(result[j])
            except IndexError:
                summ.append(result[j])
        else:
            return sum(summ)
    return sum(summ)


print(convert_number(string, nums))
