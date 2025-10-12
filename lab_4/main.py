import sys

from functions import *


# 9. Функция, которая последовательно вызывает ВСЕ вышесозданные функции.
# Функция ДОЛЖНА завершаться корректно и НЕ ДОЛЖНА иметь необработанных исключений

def call_all_functions():
    print("1")
    try:
        print('split value:', split_value('parameters', 'a'))
    except TypeError as e:
        print_has_runtime_errors_string('split_value', e)

    married_users = None
    try:
        married_users = getting_users_married('Bob', 'Mary')
    except TypeError as e:
        print_has_runtime_errors_string('getting_users_married', e)
    print('married users:', married_users)

    divorced_users = None
    if married_users:
        try:
            divorced_users = getting_users_divorce(married_users)
        except TypeError as e:
            print_has_runtime_errors_string('getting_users_divorce', e)

    if married_users and divorced_users:
        print('divorced users:', divorced_users)

        print("2")
        print(
            'validate married users',
            validate_users_are_married(married_users),
            '\nvalidate divorced users',
            validate_users_are_married(divorced_users)
        )

        print("3")
        not_specified_status = {
            'status': 'not specified',
        }
        print(
            'get status of married users:',
            get_married_status(married_users),
            '\nget not specified status:',
            get_married_status(not_specified_status)
        )

        print("4")
        # закомментирована, чтобы не создала файла при случайном вызове
        # read_file('C:/Users/1645284/OneDrive/lab_4.txt', married_users)
        set_married_term(married_users, '0fff')
        print('married users with term', married_users)
        print('married users term', get_married_term(married_users))

    print("5")
    print(compute_archimedes_power(13, 9.8, 'sdf'))

    print("6")
    print(get_user(24))
    print(
        'get secret info for admin:',
        get_secret_info(23),
        '\nget secret info for user:',
        get_secret_info(24)
    )

    print("7")
    print(get_users("Mos"))

    print("8")
    print(
        'check prime num 17:',
        check_prime_num(17),
        '\ncheck prime num 25:',
        check_prime_num(25),
    )
    print('get_user_by_name:', get_user_by_name('Mary'))
    print('get datetime from iso string:', get_datetime_from_string('2025-10-02T15:11:07.980'))


if __name__ == "__main__":
    call_all_functions()
