def get_multiplied_digits(number):
    str_number = str(number)

    first = int(str_number[0])

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


user_input = int(input("Введите целое число: "))

result = get_multiplied_digits(user_input)

print(f"Произведение цифр числа {user_input} равно {result}")
