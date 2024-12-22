import time

n = 'one'
m = 'two'


def get_func_time(seconds=True):
    def inner(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            finish_time = time.time()
            run_time = finish_time - start_time
            if not seconds:
                return (f'Время выполнения функции - {(run_time / 60):.10f}'
                        f' мин.\nРезультат - {result}')
            return (f'Время выполнения функции - {run_time:.10f}'
                    f' сек.\nРезультат - {result}')
        return wrapper
    return inner


def get_params(*args, **kwargs):
    if kwargs:
        return args, kwargs
    return args


print(get_func_time()(get_params)(n, m))
# print(get_func_time(seconds=False)(get_params)(n, m))
