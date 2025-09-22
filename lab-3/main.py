from functions import *

if __name__ == "__main__":
    # возвращает приветственную строку
    print(get_hello())

    # складывает два числа
    print(add(2, 3))

    # выполняет определённое действие над числами в зависимости от переданной функции
    print(action(2, 3))

    # составляет строку
    print(get_new_user_string("Татьяна", 23))

    # считает среднее значение из переданных чисел
    print(get_average_value(1, 2, 3))

    # исключает из переданных именованных аргументов ненужные
    print(secure_user_data(["address", "cardNumber"], name="Mark", age=23, address="1 street", cardNumber=453434223))

    # возвращает функцию action
    print(call_action_fn(2, 3))

    # применяет переданные функции к одному числу
    print(apply_actions_to_number(3, double, square))

    # вызывает функцию, если количество переданных аргументов не более нужного
    print(call_and_check_args_length(add, 2, 1, 2))

    # выводит возвращаемую переданной функцией строку в консоль
    print_string(get_hello)

    # увеличивает переменную в два раза и возводит в квадрат
    print(double_and_square(3))

    # вызывает функцию с переданными параметрами и пишет логи в консоль
    print(call_and_logging(add, 1, 2))

    # возвращает простую строку
    print(get_simple_phrase())

    # возвращает сумму двух элементов
    print(get_sum(1, 2))

    # выполняет любое действие внутри себя
    print(do_anything(lambda: 4 + 5))

    # увеличивает число на 1 при вызове возвращаемой функции
    increment = create_incremental_fn()
    print(increment(), increment(), increment())

    # умножает начальное число на переданное в возвращаемую функцию
    times = multiply(2)
    print(times(3), times(4), times(5))

    # генерирует приветственную строку с именем, переданным в возвращаемую функцию
    get_message = create_message("Привет,")
    print(get_message("Екатерина!"), get_message("Иван!"))
