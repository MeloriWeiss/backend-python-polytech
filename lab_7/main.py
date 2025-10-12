from functions import *

def call_all_functions():
    print("1.")
    print(get_user_salary_string("Иван", "Менеджер", 21, 2300))

    print("\n2.")
    print(create_duplicate_strings("Иван", "ходил", "по", "городу", count=2))

    print("\n3.")
    print(count_substr_in_str("Ка", "Какой город кажется каждый день прокатным?"))

    print("\n4.")
    print(slice_string("Иван ходил по городу", 3, 7))

    print("\n5.")
    print(get_strs_and_count_with_latin_symbols("Kогда", "там", "были", "oни"))

    print("\n6. is_palindrome")
    print(is_palindrome("гоша8п8ашог"), "гоша8п8ашог")
    print(is_palindrome("гоша8пп8ашог"), "гоша8пп8ашог")
    print(is_palindrome("гошап7ашог"), "гошап7ашог")
    print(is_palindrome(54545), 54545)

    print("\n7.")
    print(remove_spaces_and_get_len("   Иван    ходил по    городу       "))

    print("\n8.")
    print(break_sentences("Иван остановился у булочной. Капли дождя медленно стекали по его морщинистым щекам! " +
                          "Рядом с ларьком тосковала собака, тихо скуля и только усиливая переживания Ивана??? Вечер. Тишина."))

    print("\n9.")
    print(words_count("Иван ходил по городу"))
    print(duplicate_all_symbols("Иван ходил по городу"))
    print(reverse_string("Иван ходил по городу", 3, 10))

if __name__ == '__main__':
    call_all_functions()