import random
len_string = 5


def str_gen(n):
    string = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    new_str = ''
    while n != 0:
        new_str += ''.join(string[random.randrange(len(string))])
        n -= 1
    return new_str


string_gen = str_gen(len_string)


def write_string_to_file(string):
    with open('str_data.txt', 'a') as file:
        file.write(string + ' ')
    return f'В файл "str_data.txt" добавлена строка - "{string}"'


print(write_string_to_file(string_gen))
