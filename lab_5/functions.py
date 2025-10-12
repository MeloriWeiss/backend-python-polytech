# 1. Функция, принимающая на вход список.
# Функция возвращает перевёрнутый список.
import itertools
import random
from functools import reduce


def reverse_list(lst: list) -> list:
    lst.reverse()
    return lst


# 2. Функция, принимающая на вход список.
# Функция изменяет одно, несколько или все значения списка.
# Функция возвращает изменённый список.

# не совсем понятно по тз, как именно функция должна изменять список, имея как параметр только его
def change_list(lst: list) -> list:
    # делаем ревёрс элементов с индексами с 1 по 3
    lst[1:4] = lst[1:4][::-1]
    return lst


# 3. Функция, принимающая на вход два или более списков.
# Функция сравнивает переданные на вход списки.
# Функция возвращает отметку, равны или нет все переданные на вход списки.

def get_is_lists_equal(*args: list) -> bool:
    # инициализируем флаг, которые отвечает за результат функции
    is_equal = True

    for arg in args:
        # будем сравнивать все элементы списка с первым
        # списки под капотом сравниваются поэлементно, поэтому можем спокойно использовать оператор !=
        if arg != args[0]:
            # если хотя бы один элемент списка не равен первому, значит, переданные списки не равны между собой
            is_equal = False
            break

    return is_equal


# 4. Функция, принимающая на вход список и доп. параметры (необходимо самостоятельно их определить).
# Функция ДОЛЖНА иметь возможность выбрать диапазон значений из переданного списка с заданным шагом.
# Нужно рассмотреть все возможные ситуации, связанные с передаваемыми значениями.
# Функция возвращает список, соответствующий диапазону.

# задаём всем доп. параметрам значения по умолчанию, чтобы можно было передавать только список
def get_part_of_list(lst: list, start_index=0, end_index=None, step=1) -> list:
    # так как мы не можем присвоить индекс последнего элемента переданного списка значению параметра end_index по умолчанию,
    # сделаем это ниже
    if not end_index:
        end_index = len(lst)

    # вернём часть списка с нужным шагом
    return lst[start_index:end_index:step]


# 5. Функция, принимающая на вход некие параметры.
# Функция создаёт список, основываясь на переданных параметрах.
# Создание списка, его наполнение и возврат полученного списка.

def create_list(length: int, *args) -> list:
    # создаём список из переданных значений для будущего списка
    lst = list(args)
    # если значений было передано меньше, чем должен быть итоговый список по длине,
    # добавляем последнее из переданных значений к списку до тех пор, пока он не станет нужной длины
    last_elem = lst[-1]
    while len(lst) < length:
        lst.append(last_elem)

    # возвращаем итоговый список
    return lst


# 6. Функция, принимающая на вход список и доп. параметры (необходимо самостоятельно их определить).
# Функция вставляет элемент в заданную позицию списка.
# Функция возвращает изменённый список.

def insert_into_list(lst: list, index: int, value) -> list:
    # вставляем элемент в нужную позицию, отодвигая последующие на индекс вперёд
    lst.insert(index, value)
    return lst


# или без метода insert
def insert_into_list_2(lst: list, index: int, value) -> list:
    lst = lst[:index] + [value] + lst[index:]
    return lst


# 7. Функция, принимающая на вход два или более списков и доп. параметры (необходимо самостоятельно их определить)..
# Функция объединяет все переданные на вход списки и сортирует их желаемым образом.
# Функция возвращает результирующий список.

# вопросы по тз: объединение списка это объединение их элементов в один список или объединение списков в список?
# и что нужно сортировать, сами списки внутри списка или элементы списков, когда элементы списков слились в один список?
# вопросы появились потому, что сказано, что функция объединяет списки, а затем ИХ же сортирует
# в любом случае, вот реализация всех случаев

# сортировка самих списков, а потом уже объединение в один
def merge_and_sort_lists(*args, sort_fn=None) -> list:
    return sorted(args, key=sort_fn)


# сортировка самих списков, а потом уже объединение элементов списка в один
def merge_and_sort_lists_2(*args, sort_fn=None) -> list:
    sorted_lists = sorted(args, key=sort_fn)
    return list(itertools.chain(*sorted_lists))


# сортировка самих элементов внутри объединённых элементов списка
def merge_and_sort_elems_of_lists(*args, sort_fn=None) -> list:
    result_list = list(itertools.chain(*args))
    return sorted(result_list, key=sort_fn)


# 8. Функция, не принимающая никаких параметров.
# Функция создаёт список из целых чисел произвольной длины.
# Функция проверяет, длина списка чётное число или нет.
# Если чётное, то функция сообщает об этом и создаёт новые списки до тех пор, пока не будет создан список нечётной длины.
# Если нечётное, то функция ищет центральный элемент списка и выводит количество элементов с таким же значением, что и у центрального элемента.

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


# 9. Функция, прибавляющая к первому списку другие списки.
# Если длина первого списка превышает заданный порог, необходимо удалить из списка некоторые элементы, чтобы число элементов списка не превышало порог.
# Функция возвращает изменённый первый список.

def concat_lists(lst: list, max_len: int, *args) -> list:
    # если длина списка превышает порог, удаляются лишние элементы
    if len(lst) > max_len:
        lst = lst[:max_len]
        # либо можно вызвать функцию заново с помощью рекурсии с новыми аргументами
        # return concat_lists(lst[:max_len], max_len, *args)

    # изменяем и возвращаем именно первый список, сохраняя его ссылку
    lst.extend(list(itertools.chain(*args)))
    return lst


# 10. Минимум 6 функций, которые сортируют список по заданным критериям.
# Минимум 3 из этих функций ДОЛЖНЫ использовать функцию map()

# сортирует числа по модулю
def sort_list(lst: list) -> list:
    return sorted(lst, key=lambda x: abs(x))


# сортирует числа по убыванию
def sort_list_2(lst: list) -> list:
    return sorted(lst, key=lambda x: -x)


# сортирует данные по их длине
def sort_list_3(lst: list) -> list:
    return sorted(lst, key=lambda x: len(str(x)))


# сортирует по возрастанию удвоенные элементы списка, кратные трём
def sort_list_4(lst: list) -> list:
    # преобразовываем начальный список
    doubled_list = map(lambda x: x * 2, lst)
    # фильтруем преобразованный список
    filtered_list = filter(lambda x: x % 3 == 0, doubled_list)
    # возвращаем сортировку
    return sorted(filtered_list)


# сортирует числа по возрастанию по первой цифре
def sort_list_5(lst: list) -> list:
    # map преобразует числа в структуру map по переданной функции (int, а полная запись lambda num: int(num))
    return sorted(lst, key=lambda x: list(map(int, str(abs(x))))[0])


# сортирует числа по сумме их цифр
def sort_list_6(lst: list) -> list:
    # ищем сумму всех цифр числа
    nums_sum = lambda x: reduce(lambda acc, c: acc + c, map(int, str(abs(x))), 0)
    # возвращаем отсортированный список по ключу
    return sorted(lst, key=nums_sum)


# 11. Функция, которая извлекает с удалением минимальный элемент списка.
# Функция возвращает минимальный элемент списка.

def remove_min(lst: list) -> list:
    # ищем минимальный элемент
    min_elem = min(lst)
    # удаляем элемент из списка
    lst.remove(min_elem)
    print('new list:', lst)
    return min_elem


# 12. Минимум 2 функции, принимающие на вход один или несколько кортежей, и, ВОЗМОЖНО, доп. параметры.
# Функции совершают некие операции над кортежем или кортежами.
# Функции МОГУТ возвращать некоторые значения.

# возвращает имена типов переданных кортежей в двумерном списке
def get_tuples_types_names(*args: tuple) -> list:
    # создаём результирующий список
    result = list()
    # проходимся по каждому кортежу
    for tpl in args:
        tpl_result = list()
        # в результирующий список названий типов добавляем название типа каждого элемента текущего кортежа
        for item in tpl:
            tpl_result.append(type(item).__name__)

        result.append(tpl_result)

    # возвращаем результат
    return result


# возвращаем количество типов int в каждом из переданных кортежей
def get_ints_count(*args: tuple) -> list:
    # создаём результирующий список
    result = list()
    # проходимся по каждому кортежу
    for tpl in args:
        tpl_ints_count = 0
        # в результирующий список добавляем количество типов int текущего кортежа
        for item in tpl:
            if type(item) == int:
                tpl_ints_count += 1
        result.append(tpl_ints_count)

    # возвращаем результат
    return result


# 13. Функция, принимающая на вход кортеж неопределённой длины, содержащий произвольные значения.
# Функция перебирает элементы кортежа и формирует новый кортеж, состоящий из типов данных каждого элемента входного кортежа.
# Функция возвращает кортеж из типов данных.

def get_tuple_types(tpl: tuple) -> tuple:
    # создаём результирующий список
    result = list()
    # проходимся по каждому элементу кортежа и добавляем в результирующий список тип элемента
    for item in tpl:
        result.append(type(item))

    # возвращаем результат в виде кортежа
    return tuple(result)


# 14. Функция, принимающая на вход кортеж и доп. параметры (необходимо самостоятельно их определить).
# Функция проверяет, есть ли заданный элемент в кортеже.
# Функция возвращает отметку, есть элемент или нет.

def has_element(tpl: tuple, element) -> bool:
    # считает количество нужных элементов, но не останавливает цикл, даже если элемент был найден
    # return tpl.count(element) > 0
    # или
    # ищет индекс первого подходящего элемента и отлавливает ошибку, если индекс не найден
    # try:
    #     # возвращает True, если хоть какой-то индекс найден
    #     return tpl.index(element) > -1
    # except ValueError:
    #     return False
    # или
    # ищет через цикл первый подходящий элемент и сразу возвращает True, если элемент нашёлся, заканчивая цикл
    # в противном случае возвращает False
    for item in tpl:
        if item == element:
            return True
    return False


# 15. Функция, принимающая на вход один или несколько списков, и, возможно, доп. параметры.
# Функция формирует двумерный список по произвольным критериям и возвращает этот список.
def get_multiple_values(multiplier: int, *args: list) -> list:
    result = list()
    for lst in args:
        doubled_list = list()
        for item in lst:
            doubled_list.append(item * multiplier)
        result.append(doubled_list)

    return result


# 16. Минимум 3 функции, которые принимают на вход словарь.
# Функции совершают некие операции над словарём.
# Функции возвращают какое-либо значениЕ, значениЯ.

# увеличивает возраст пользователя на 1
def increment_age(user: dict) -> int | None:
    if 'age' not in user:
        return None

    user['age'] = user['age'] + 1
    return user['age']


# устанавливает роль пользователю
def set_role(user: dict, role: str) -> str | None:
    if 'role' not in user:
        return None

    user['role'] = role
    return user['role']


# проверяет, является ли пользователь администратором
def is_admin(user: dict) -> bool | None:
    if 'role' not in user:
        return None

    if user['role'] == 'admin':
        return True

    return False


# 17. Функция, принимающая на вход два или более словарей и доп. параметры (необходимо самостоятельно их определить).
# Функция считает, сколько раз встречается элемент с определённым ключом во всех словарях суммарно и выводит это значение
# (например, если есть 3 словаря, в двух из них есть элемент с ключом 'name', а в третьем нет, то выводится значение 2).

def get_key_count(key: str, *args: dict) -> list:
    # создаём счётчик
    count = 0
    # проходимся по каждому словарю и, если переданный ключ есть в словаре, увеличиваем счётчик на 1
    for dct in args:
        if key in dct:
            count += 1

    # возвращаем значение счётчика
    return count


# 18. Функция, принимающая на вход комплексный словарь определённого формата, у которого будет минимум 3 уровня вложенности.
# Функция ищет в этом словаре определённый элемент или элементы, располагающиеся на самом последнем уровне вложенности.
# Функция возвращает значение найденного элемента или элементов или None, если такой элемент или элементы не найдены.

# ищет элементы в дереве, которое имеет одну ветку увеличения вложенности
def find_elems_in_last_nesting_lvl(dct: dict, *args: str) -> dict | None:
    result = dict()

    def find_last_dict(cur_dict: dict):
        for k in cur_dict.keys():
            if type(cur_dict[k]) == dict:
                return find_last_dict(cur_dict[k])
        return cur_dict

    last_dict = find_last_dict(dct)

    for key in args:
        if key in last_dict:
            result[key] = last_dict[key]

    return result

# ищет элементы в дереве, которое имеет несколько веток, и возвращает результат из самой длинной,
# но если есть несколько веток с одинаковой длиной, вернёт значения только из последней
def find_elems_in_last_nesting_lvl_2(dct: dict, *args: str) -> dict | None:
    result = dict()

    last_dict = dict()
    max_nesting_lvl = 1

    def find_last_dict(cur_dict: dict, cur_nesting_lvl: int):
        nonlocal last_dict
        nonlocal max_nesting_lvl

        if cur_nesting_lvl > max_nesting_lvl:
            max_nesting_lvl = cur_nesting_lvl
            last_dict = cur_dict

        for k in cur_dict.keys():
            if type(cur_dict[k]) == dict:
                find_last_dict(cur_dict[k], cur_nesting_lvl + 1)

    find_last_dict(dct, 1)

    for key in args:
        if key in last_dict:
            result[key] = last_dict[key]

    return result

# ищет элементы в дереве, которое имеет несколько веток, и, в отличие от предыдущих функций,
# сохраняет нужные значения из всех веток словаря, если они имеют одинаковую и максимальную длину
def find_elems_in_last_nesting_lvl_3(dct: dict, *args: str) -> list | None:
    res = list()

    last_dicts = list()
    max_nesting_lvl = 1

    def find_last_dict(cur_dict: dict, cur_nesting_lvl: int):
        nonlocal last_dicts
        nonlocal max_nesting_lvl

        if cur_nesting_lvl == max_nesting_lvl:
            last_dicts.append(cur_dict)

        if cur_nesting_lvl > max_nesting_lvl:
            max_nesting_lvl = cur_nesting_lvl
            last_dicts.clear()
            last_dicts.append(cur_dict)

        for k in cur_dict.keys():
            if type(cur_dict[k]) == dict:
                find_last_dict(cur_dict[k], cur_nesting_lvl + 1)

    find_last_dict(dct, 1)

    for last_dict in last_dicts:
        res_for_dict = dict()
        for key in args:
            if key in last_dict:
                res_for_dict[key] = last_dict[key]

        res.append(res_for_dict)

    return res