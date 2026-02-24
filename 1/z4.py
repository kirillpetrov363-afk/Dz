while True:
    num = input("Введите число: → ")

    if num == "exit":
        print("Выход из программы...")
        break

    if num.lstrip('-').isdigit() and num != '-':
        if num[0] == '-':
            print(f"В этом числе {len(num) - 1} цифр.")
        else:
            print(f"В этом числе {len(num)} цифр.")
    else:
        print("Ошибка: данные не являются числом.")