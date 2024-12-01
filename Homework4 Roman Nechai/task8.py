def create_dict():
    dct = {}
    counter = 1

    def local_func(*args):
        nonlocal dct, counter
        for value in args:
            dct.update({counter: value})
            counter += 1
        return dct
    return local_func


f_1 = create_dict()
f_2 = create_dict()
print(f_1('hello'))
print(f_1(100))
print(f_1([1, 2, 3]))
print(f_2('PoweR'))
