# функция без параметров
def get_hello():
    return "Hello World"


# функция с параметрами
def add(a, b):
    return a + b


# функция с несколькими параметрами со значениями по умолчанию
def action(a=0, b=0, fn=add):
    return fn(a, b)


# функция с несколькими параметрами, у которых задан тип
def get_new_user_string(name: str, age: int) -> str:
    return f"Новый участник {name}, возраст {age}"


# функция с неопределённым количеством параметров (args)
def get_average_value(*args):
    return sum(args) / len(args)


# функция с неопределённым количеством параметров (kwargs)
def secure_user_data(secured_data: list[str], **kwargs):
    data = []
    for key, value in kwargs.items():
        if key not in secured_data:
            data.append({key, value})

    return data


# функция, вызывающая внутри себя другую функцию
def call_action_fn(a=0, b=0, fn=add):
    return action(a, b, fn)


# функция, принимающая функцию как параметр (минимум 3 примера)
def apply_actions_to_number(number: int, *args):
    transformed_number = number
    for arg in args:
        transformed_number = arg(transformed_number)

    return transformed_number


def call_and_check_args_length(fn, args_len, *args):
    if len(args) > args_len:
        return None

    return fn(*args)


def print_string(fn):
    print(fn())


# функция с объявленной внутри локальной функцией (минимум 2 примера)
def double_and_square(num):
    def double_num():
        return num * 2

    def square_doubled_num():
        return double_num() ** 2

    return square_doubled_num()


def call_and_logging(fn, *args):
    def create_logging_str(action_type: str):
        return f"fn '{fn.__name__}' {action_type}"

    print(create_logging_str('start'))

    result = fn(*args)

    print(create_logging_str('end'))

    return result


# лямбда-выражение без параметров
get_simple_phrase = lambda: "Вот оно"

# лямбда-выражение с параметрами
get_sum = lambda x, y: x + y


# функция, принимающая лямбда-выражение как параметр, и вызывающая лямбда-выражение внутри себя
def do_anything(fn):
    return fn()

# функция с замыканиями (минимум 3 примера)
def create_incremental_fn():
    num = 0

    def increment():
        nonlocal num
        num += 1
        return num

    return increment

def multiply(first_num):
    def times(second_num):
        return first_num * second_num

    return times

def create_message(text):
    def message(name):
        return f"{text} {name}"

    return message


# вспомогательные функции
double = lambda x: x * 2
square = lambda x: x * x
