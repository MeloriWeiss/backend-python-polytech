import decimal
import locale
import math
import py_compile
import random
from dataclasses import dataclass, field
import uuid


# 3. Файлы байт-кода любых 7 модулей, написанных в течение курса (в том числе модулей этой лабораторной).
def get_byte_code_files():
    # пути к файлам байт-кода
    file_path = py_compile.compile("fns_1.py")
    file_path_2 = py_compile.compile("fns_2.py")
    file_path_3 = py_compile.compile("fns_3.py")
    file_path_4 = py_compile.compile("fns_4.py")
    file_path_5 = py_compile.compile("fns_5.py")
    file_path_6 = py_compile.compile("fns_6.py")
    file_path_7 = py_compile.compile("fns_7.py")
    # также можно читать эти файлы
    with open(file_path, "rb") as f:
        bc = f.read()
        print(bc)


# 4. Минимум 2 функции, использующие разные методы из модуля random
# возвращает случайное просто число в указанном интервале
def get_random_prime_num(num_from: int, num_to: int):
    # генерирует случайное целое число в диапазоне
    random_num = random.randint(num_from, num_to)

    # если это число не простое, но функция выполняется заново
    while not check_prime_num(random_num):
        random_num = random.randint(num_from, num_to)

    # если число простое, возвращаем его
    return random_num


# генерирует список случайной длины и возвращает количество значений серединного элемента списка
def count_center_values():
    lst = list()
    # заполняем список случайной длины с 0 по 10 случайными числами с 0 по 10
    for i in range(random.randint(1, 10)):
        lst.append(random.randint(1, 10))

    # print("print list for check:", lst)

    # проверяем на чётность: если число чётно, возвращаем с помощью рекурсии заново выполняющуюся функцию
    if len(lst) % 2 == 0:
        return count_center_values()

    # если число нечётно, ищём срединный индекс
    center_index = len(lst) // 2

    # возвращаем количество элементов списка с таким же значением, что и у центрального
    return lst.count(lst[center_index])


# 5. Минимум 3 функций, использующих разные методы из модуля math

# проверяет, простое число или нет
# при уверенности, что число не простое, будет выбрасывать ошибку и отлавливать, чтобы в конце вернуть объект ошибки
def check_prime_num(num: int):
    if num < 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    # находим квадратный корень числа с помощью метода sqrt и делаем его на 1 больше
    max_divisor = int(math.sqrt(num)) + 1
    for i in range(3, max_divisor, 2):
        if num % i == 0:
            return False

    return True


# считает площадь круга, используя метод pi, возвращающий число ПИ, и метод pow, возводящий число в степень
def calc_circle_area(radius):
    # возвращает результат по формуле
    return math.pi * math.pow(radius, 2)


# рассчитывает площадь треугольника
def calc_triangle_area(side_length_1: int, side_length_2: int, corner_degrees: int):
    # вычисляет синус угла между двумя сторонами, преобразуя градусную величину в радианы через math.radians,
    # так как math.sin работает с радианами
    corner_sin = math.sin(math.radians(corner_degrees))
    # возвращает округлённый результат по формуле
    return round(side_length_1 * side_length_2 * corner_sin, 3)


# 6. Минимум 3 функции, использующие разные методы из модуля locale

# возвращает список доступных локалей в системе
def get_available_locales():
    return locale.locale_alias


# устанавливает локаль на русский
def set_locale_to_russian():
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


# возвращает текущую локаль
def get_current_locale():
    return locale.getlocale()


# форматирует число как валюту в текущей локали
def format_currency(amount):
    return locale.currency(amount, grouping=True)


# 7. Минимум 2 функции, использующие разные методы из модуля decimal

# устанавливает правило по округлению decimal (в данном случае оно будет округляться всегда до меньшего целого числа)
def set_decimal_rounding_down():
    decimal.getcontext().rounding = decimal.ROUND_DOWN


# округляем число по текущим правилам округления
def round_decimal(num: str):
    dcm = decimal.Decimal(num)
    return dcm.quantize(decimal.Decimal("0.001"))


# считаем среднее арифметическое с определённой точностью
def calc_average(*args: float, prc: int = 10):
    # устанавливаем точность
    decimal.getcontext().prec = prc

    # создаём массив элементов типа Decimal
    decimal_nums = [decimal.Decimal(str(num)) for num in args]

    # высчитываем и возвращаем среднее арифметическое
    return decimal.Decimal(sum(decimal_nums)) / len(decimal_nums)


# 8. Минимум 3 разных data-класса.

@dataclass
class Person:
    first_name: str
    last_name: str
    age: int = 0
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class House:
    country: str
    city: str
    street: str
    number: int
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class Package:
    text: str
    person: Person
    house: House
    id: uuid.UUID = field(default_factory=uuid.uuid4)


# 9. Минимум 5 функций, использующих в своей работе описанные в п. 7 data-классы
# В функции ДОЛЖНО быть, как минимум, следующее:
# 9.1. Передача объекта data-класса как параметр
# 9.2. Работа со списком из объектов data-классов
# 9.3. Работа со словарём, где в качестве значения выступает объект data-класса
# 9.4. Модификация значений объекта data-класса
# 9.5. Создание объекта data-класса на основе передаваемых параметров (которые не являются объектов data-класса)

# получает строку с информацией о человеке
def get_person_info(person: Person):
    return f"{person.first_name} {person.last_name}, {person.age} years old"


# фильтрует объекты из списка по полю age
def filter_persons_by_age(persons: list[Person], age_greater_than: int = 18) -> list[Person]:
    return list(filter(lambda p: p.age > age_greater_than, persons))

# фильтрует объекты из словаря, где ключ - id, а значение - объект, по полю age
# возвращает список словарей
def filter_persons_by_age_2(persons: dict[uuid.UUID, Person], age_greater_than: int = 18) -> list[Person]:
    return list(filter(lambda p: p.age > age_greater_than, persons.values()))

# устанавливает имя человеку
def set_person_name(person: Person, new_name: str) -> Person:
    person.first_name = new_name
    return person

# создаёт объект data-класса
def create_person(first_name: str, last_name: str, age: int = 0) -> Person:
    return Person(first_name, last_name, age)
