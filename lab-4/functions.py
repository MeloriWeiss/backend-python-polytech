# 1. Минимум 2 разные функции, которые принимают на вход один или несколько параметров.
# Функции ДОЛЖНЫ выбрасывать исключение при определённых значениях входных параметров.
# Функции НЕ ДОЛЖНЫ содержать никаких обработчиков исключений.
import math
from datetime import datetime

# сплитит значение
def split_value(params, separator):
    # проверяется параметр на строку
    if type(params) is not str:
        raise TypeError("params must be a string")

    return params.split(separator)


# "объединяет" людей
def getting_users_married(male_name, female_name):
    # проверяются параметр на строку
    if type(male_name) is not str or type(female_name) is not str:
        raise TypeError("male and female names must be strings")

    # возвращается словарь с пользователями и статусом "женаты"
    return {
        'male_name': male_name,
        'female_name': female_name,
        'status': 'married'
    }


# разводит людей, не на деньги
def getting_users_divorce(users: dict):
    # меняется статус пользователей на "разведены", если поле status существует
    if 'status' not in users:
        raise TypeError("users must have 'status' field")

    users['status'] = 'divorced'
    return users


# 2. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА выбрасывать исключение при определённых значениях входных параметров.
# Функция ДОЛЖНА содержать ОДИН обработчик исключений общего типа (Exception). Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой исключения.
# Обработчик НЕ ДОЛЖЕН содержать блок finally.

# проверяет, состоят ли люди в браке
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


# 3. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА выбрасывать исключение при определённых значениях входных параметров.
# Функция ДОЛЖНА содержать ОДИН обработчик исключений общего типа (Exception). Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой исключения.
# Обработчик ДОЛЖЕН содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.

# получает статус нахождения в браке
def get_married_status(users: dict):
    status = users['status']
    try:
        if status is None:
            raise KeyError("status cannot be None")

        return status
    except Exception as e:
        return 'not_specified'
    finally:
        users['status'] = status if status is not None else 'not_specified'


# 4. Минимум 3 разные функции, которые принимают на вход один или несколько параметров.
# Функции ДОЛЖНЫ выбрасывать исключения при определённых значениях входных параметров.
# Функции ДОЛЖНЫ содержать НЕСКОЛЬКО обработчиков РАЗНЫХ типов исключений (минимум 3 типа исключений). Внутри блоков обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой соответствующего типа исключения.
# Каждый обработчик МОЖЕТ содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.

# читает данные из файла и создаёт его в базовыми данными, если файл не найден
def read_file(file_path: str, users: dict):
    f = None
    try:
        # проверяет статус пользователей
        if users['status'] != 'married':
            raise TypeError("user must be married")

        # читает файл, если статус это позволяет
        f = open(file_path, 'r')
        data = f.read()
        # возвращает данные из файла
        return data

    except TypeError:
        # если статус пользователей не подошёл, даём возможность сразу же это исправить
        return getting_users_married
    except FileNotFoundError:
        # если вдруг нужного файла не оказалось, создадим файл и запишем базовую информацию
        with open(file_path, 'w', encoding='utf-8') as new_file:
            new_file.write(f"{users['male_name']} and {users['female_name']} are {users['status']}")
    finally:
        # в самом конце закроем файл
        if f:
            f.close()


# устанавливает срок жизни брака
def set_married_term(users: dict, term: str | int):
    try:
        # пытаемся преобразовать срок в число
        users['term'] = int(term)
    except ValueError:
        # устанавливаем срок, если его не было
        users['term'] = 0
    finally:
        # в любом случае возвращаем срок
        return users['term']


# получает срок жизни брака
def get_married_term(users: dict):
    try:
        # преобразуем время жизни после преобразования в число
        term = int(users['term'])
        if term > 5:
            raise TypeError("term so long")
        return term

    except ValueError:
        # если не удалось преобразовать в число, устанавливаем срок в 0
        return set_married_term(users, 0)
    except TypeError:
        # если люди пожили вместе более 5 лет, разводим, достаточно
        getting_users_divorce(users)

        # но только для того, чтобы поженить заново
        getting_users_married(users['male_name'], users['female_name'])
        set_married_term(users, 0)
        return 0


# 5. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА генерировать исключения при определённых условиях (в Python есть конструкция для генерации исключений).
# Функция ДОЛЖНА содержать обработчики всех исключений, которые генерируются внутри этой функции. Внутри блоков обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой соответствующего типа исключения.
# Обработчик МОЖЕТ содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.

# вычисляет значение силы Архимеда
def compute_archimedes_power(r, g, v):
    # словарь с допустимыми или ошибочными значениями
    params = {
        'r': 'passed',
        'g': 'passed',
        'v': 'passed'
    }

    # проверка на соответствие подходящим типам
    if not isinstance(r, (int, float)):
        params['r'] = 'ex'
    if not isinstance(g, (int, float)):
        params['g'] = 'ex'
    if not isinstance(v, (int, float)):
        params['v'] = 'ex'

    # генерация ошибки при неподходящем типе хотя бы одного из параметров, при этом мы видим статус всех
    try:
        for value in params.values():
            if value == 'ex':
                raise Exception(params)
        return r * g * v

    # отлавливание ошибки и вызов функции с корректными параметрами
    except Exception as e:
        # log(e)...
        return compute_archimedes_power(
            r if params['r'] == 'passed' else 1,
            g if params['g'] == 'passed' else 8.1,
            v if params['v'] == 'passed' else 1
        )


# 6. Минимум 3 разных пользовательских исключения и примеры их использования
class BadRequestException(Exception):
    pass


class NotFoundException(Exception):
    pass


class NotAllowedException(Exception):
    pass


db_data = [{
    'id': 23,
    'country': "Russia",
    'city': "Moscow",
    'name': 'Mary',
    'role': 'admin'
}, {
    'id': 24,
    'country': "Russia",
    'city': "Vladimir",
    'name': 'Ivan',
    'role': 'user'
}]

# имитируем работу бэкенда
# получает пользователя
def get_user(user_id: int | str):
    try:
        try:
            int_user_id = int(user_id)
        except ValueError:
            raise BadRequestException('user_id must be an int')

        # ищем пользователя по id
        for user in db_data:
            if user['id'] == int_user_id:
                return user
        # если пользователь не найден, выбрасываем соответствующую ошибку
        raise NotFoundException('user not found')

    # обрабатываем ошибки
    except NotFoundException as e:
        return default_error(e)

    except Exception as e:
        return default_error(e)

# получает закрытую информацию
def get_secret_info(user_id: int):
    try:
        # ищем пользователя
        for user in db_data:
            if user['id'] == user_id:
                # проверяем его роль
                if user['role'] == 'admin':
                    return {
                        'info': 'secret_api_key'
                    }
                # выбрасываем ошибку о запрете доступа
                raise NotAllowedException('insufficient access rights')

        raise NotFoundException('user not found')

    # обрабатываем ошибки
    except NotFoundException as e:
        return default_error(e)

    except NotAllowedException as e:
        return default_error(e)

    except Exception as e:
        return default_error(e)

def default_error(error: Exception):
    return {
        'error': True,
        'message': error.args[0]
    }

# 7. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА выбрасывать пользовательское исключение, созданное на шаге 6. при определённых значениях входных параметров.
# Функция ДОЛЖНА содержать МИНИМУМ ОДИН обработчик исключений. Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой исключения.
# Обработчик МОЖЕТ содержать блок finally.

# получает всех пользователей
def get_users(city="", country=""):
    try:
        try:
            if type(country) is not str or type(city) is not str:
                raise TypeError("country and city must be strings")
            # тут может быть гораздо больше выбрасываний разных ошибок, поэтому делаем ещё одну прослойку с try
        except TypeError as e:
            # если данные пришли неправильные, выбрасываем соответствующую ошибку
            raise BadRequestException(e)

        # фильтрует пользователей по стране и городу
        filtered_users = filter(
            lambda user:
               country in user['country'] and city in user['city'],
            db_data
        )
        return list(filtered_users)

    # обрабатываем все ошибки
    except BadRequestException as e:
        return default_error(e)

    # сразу добавляем обработчик общих ошибок, потому что в любой момент код эндпоинта может измениться и мы можем этого не отследить
    except Exception as e:
        return default_error(e)

# 8. Минимум 3 функции, демонстрирующие работу исключений.
# Алгоритм функций необходимо придумать самостоятельно
class NonPrimeIntException(Exception):
    pass

# проверяет, простое число или нет
# при уверенности, что число не простое, будет выбрасывать ошибку и отлавливать, чтобы в конце вернуть объект ошибки
def check_prime_num(num: int):
    # сгенерируем ошибку и запишем в переменную
    prime_exception = NonPrimeIntException('number is not prime')
    try:
        if num < 1:
            raise prime_exception
        if num == 2:
            return True
        if num % 2 == 0:
            raise prime_exception
        # находим квадратный корень числа и делаем его на 1 больше
        max_divisor = int(math.sqrt(num)) + 1
        for i in range(3, max_divisor, 2):
            if num % i == 0:
                raise prime_exception

        return True

    # отловим ошибку
    except NonPrimeIntException as e:
        return default_error(e)

# получает пользователя по имени
def get_user_by_name(name: str):
    try:
        # ищем пользователя по name
        for user in db_data:
            if user['name'] == name:
                return user
        # если пользователь не найден, выбрасываем соответствующую ошибку
        raise NotFoundException('user not found')

    # обрабатываем ошибки
    except NotFoundException as e:
        return default_error(e)

    except Exception as e:
        return default_error(e)

# создаёт объект datetime по формату, по умолчанию формат = iso
def get_datetime_from_string(time: str, date_format: str = '%Y-%m-%dT%H:%M:%S.%f'):
    try:
        # преобразуем дату в объект даты
        return datetime.strptime(time, date_format)
    # отлавливаем ошибку при неправильно переданной строке даты или формата
    except ValueError as e:
        return default_error(e)


# вспомогательная функция
def print_has_runtime_errors_string(fn_name: str, e: Exception):
    print(f"{fn_name} has runtime errors:", e)