from fns_5 import (
    # функция из 7 файла
    get_hello,
    # функция из 6 файла
    action,
    # функция из 5 файла
    secure_user_data
)


def call_and_check_args_length(fn, args_len, *args):
    if len(args) > args_len:
        return None

    return fn(*args)

def test_imports():
    # вызов функции из модуля 7
    return get_hello()

def double_and_square(num):
    def double_num():
        return num * 2

    def square_doubled_num():
        return double_num() ** 2

    return square_doubled_num()