number = 5
string = "string"
stringNumber = "6"

# проверка возможности форматирования числа в строку
def check_can_format_to_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# форматирование числа в строку
# идентично проходит форматирование других типов данных
if check_can_format_to_number(stringNumber):
    formattedNumber = int(stringNumber)

    if formattedNumber > 5:
        print("Number successfully formatted")
else:
    print("Number not formatted")

# итерация по числам и строке
for num in range(1, 5):
    print(num)

for char in "New-York":
    print(char)

# итерация с помощью while
i = 0
while i < 2:
    print(f"{i} < 2")
    i += 1

# проверка типов и проверка на равенство
print(bool(type(stringNumber) is str))
print(stringNumber == "4")