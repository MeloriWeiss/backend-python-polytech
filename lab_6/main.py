from fns_1 import test_imports_2
from lab_6.functions import *


def call_all_functions():
    print("2.")
    test_imports_2()

    print("\n3.")
    get_byte_code_files()

    print("\n4.")
    print(get_random_prime_num(100, 158))
    print(count_center_values())

    print("\n5.")
    print(check_prime_num(139))
    print(calc_circle_area(2))
    print(calc_triangle_area(11, 9, 33))

    print("\n6.")
    print(get_available_locales())
    print(get_current_locale())
    set_locale_to_russian()
    print(get_current_locale())
    print(format_currency(233))

    print("\n7.")
    print(round_decimal("233.4355343324"))
    set_decimal_rounding_down()
    print(round_decimal("233.4355343324"))
    print(calc_average(3, 4, 10, 44, 23, 465, 3))

    print("\n9.")
    persons_list: list[Person] = [
        Person(first_name="Jack", last_name="Carver"),
        Person(first_name="Bob", last_name="Porter", age=25),
        Person(first_name="Jane", last_name="Smith", age=21),
        Person(first_name="Mark", last_name="Olden", age=17),
    ]
    persons_dict: dict[uuid.UUID, Person] = {person.id: person for person in persons_list}

    print("get_person_info:", get_person_info(persons_list[1]))
    print("filter_persons_by_age:", filter_persons_by_age(persons_list))
    print("filter_persons_by_age_2:", filter_persons_by_age_2(persons_dict))
    print("set_person_name:", set_person_name(persons_list[2], "Hanna"))
    print("create_person:", create_person("Diana", "Jerrera", 19))


if __name__ == '__main__':
    call_all_functions()
