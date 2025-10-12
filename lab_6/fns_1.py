# * означает, что сюда импортируются все файлы из указанного модуля
# в данном случае, так как в нескольких файлах подряд указана именно *,
# сюда импортируются все функции из модулей 2 и 3 вместе с функциями, которые импортированы в модуль 4
from fns_2 import *

# 2. Функция, в которой демонстрируется работоспособность импортов из п. 1
def test_imports_2():
    # вызов функции из модуля 4, которая вызывает функцию из модуля 7
    print(test_imports())
    # вызов функции, которая импортирована из модуля 4, куда она попала импортом из модуля 7
    print(get_hello())

def getting_users_divorce(users: dict):
    if 'status' not in users:
        raise TypeError("users must have 'status' field")

    users['status'] = 'divorced'
    return users

def validate_users_are_married(users: dict):
    try:
        if 'status' not in users:
            raise TypeError("users must have 'status' field")
        # если пользователи не женаты, выбрасывается ошибка
        if users['status'] != 'married':
            raise TypeError("user must be married")
    # ошибка отлавливается и статус пользователей меняется на "женаты"
    except Exception as e:
        # log(e)...
        users['status'] = 'married'

    return users