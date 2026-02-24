number_input = input("Введите число: ")

if number_input.isdigit():

    number = int(number_input)
    if number % 2 == 0:
            print(f"Число {number} является четным")
    else:
            print(f"Число {number} не является четным")

else:
    print("Ошибка: данные не являются числом.")