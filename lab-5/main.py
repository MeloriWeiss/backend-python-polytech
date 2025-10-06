from functions import *


# 19. Функция, вызывающая все другие функции из шагов 1-18
def call_all_functions():
    print("1. reverse_list")
    print(reverse_list([1, 2, 3]))

    print("\n2. change_list")
    print(change_list([1, 2, 3, 4, 5]))

    print("\n3. get_is_lists_equal")
    print(get_is_lists_equal([1, 2, 3], [1, 2, 3], [1, 2, 3]))
    print(get_is_lists_equal([1, 2, 3], [1, 2, 4], [1, 2, 3]))

    print("\n4. get_part_of_list")
    print(get_part_of_list([1, 2, 3, 4, 5, 6, 7, 8], 2, 5, 2))

    print("\n5. create_list")
    print(create_list(5, 2, 3, 4))

    print("\n6. insert_into_list")
    print(insert_into_list([1, 2, 3, 4, 5], 2, 7))
    print(insert_into_list_2([1, 2, 3, 4, 5], 2, 7))

    print("\n7. merge_and_sort_lists")
    print(merge_and_sort_lists([1, 2, 3], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4], sort_fn=lambda x: len(x)))
    print(merge_and_sort_lists_2([1, 2, 3], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4], sort_fn=lambda x: len(x)))
    print(merge_and_sort_elems_of_lists([1, 9, -3, 4, 2], [1, -2, 3, 7, -5, 6], sort_fn=lambda x: abs(x)))

    print("\n8. count_center_values")
    print(count_center_values())

    print("\n9. concat_lists")
    print(concat_lists([1, 2, 3, 4, 5], 3, [1, 2, 3], [6, 7, 8]))

    print("\n10. sort_list")
    print(sort_list([1, -2, 49, 3, 50]))
    print(sort_list_2([1, -2, 49, 3, 50]))
    print(sort_list_3([1, -2, 49, 3, 50]))
    print(sort_list_4([1, -2, 49, 3, 50]))
    print(sort_list_5([1, -2, 49, 3, 50]))
    print(sort_list_6([1, -2, 49, 3, 50]))

    print("\n11. remove_min")
    print(remove_min([1, -2, 49, 3, 50]))

    print("\n12. get_tuples_types, get_ints_count")
    print(get_tuples_types_names((1, "sttt", 49, [1, 2], lambda x: x), ("fd", 45)))
    print(get_ints_count((1, "sttt", 49, [1, 2], lambda x: x), ("fd", 45)))

    print("\n13. get_tuple_types")
    print(get_tuple_types((1, "sttt", 49, [1, 2], lambda x: x)))

    print("\n14. has_element")
    print(has_element(("sttt", 49, [1, 2], lambda x: x), [1, 2]))

    print("\n15. get_doubled_values")
    print(get_multiple_values(3, [1, 2, 3, 4, 5], [3], [1, 2, 3], [6, 7, 8]))

    user_data = {
        "id": 24,
        "country": "Russia",
        "city": "Vladimir",
        "name": "Ivan",
        "role": "user",
        "age": 27
    }

    print("\n16.")
    print("previous data:", user_data)
    print("is_admin:", is_admin(user_data))
    print("increment_age:", increment_age(user_data))
    print("increment_age:", set_role(user_data, "admin"))
    print("is_admin:", is_admin(user_data))

    print("\n17. get_key_count")
    print(get_key_count("value",
                        {"name": "amount", "value": 2},
                        {"name": "status", "value": "pending"},
                        {"name": "users", "count": 2}
                        ))

    dct = {
        "name": "amount",
        "value": 2,
        "item": {
            "name": "amount",
            "value": "gram",
            "count": 15,
            "address": {
                "country": "Russia",
                "city": "Vladimir",
                "value": 13
            },
            "item": {
                "name": "amount",
                "value": "gram",
                "count": 15,
            }
        },
        "user_info": {
            "name": "amount",
            "value": "gram",
            "count": 15,
            "address": {
                "country": "Russia",
                "city": "Vladimir",
                "value": 13
            },
            "item": {
                "name": "amount",
                "value": "gram1",
                "count": 15,
                # самая длинная ветка
                # "item": {
                #     "name": "amount",
                #     "value": "kilogram",
                #     "count": 15,
                # }
            }
        }
    }

    print("\n18. find_elems_in_last_nesting_lvl")
    print(find_elems_in_last_nesting_lvl(dct, "value", "city"))
    print(find_elems_in_last_nesting_lvl_2(dct, "value", "city"))
    print(find_elems_in_last_nesting_lvl_3(dct, "value", "city"))


if __name__ == "__main__":
    call_all_functions()
