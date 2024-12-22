num = 1
string = 'one'


def check_type(func):
    def wrapper(*args):
        if isinstance(args[0], int) and isinstance(args[1], str):
            return func(*args)
        raise ValueError('Переданные аргументы'
                         ' не соответствуют указынным типам')
    return wrapper


def get_dict(a, b):
    return {a: b}


result = check_type(get_dict)
print(result(num, string))
