age = input("Введите ваш возраст: ")

if age.isdigit():

    number = int(age)
    if number > 0:
        if number > 17:
            print(f"Вы совершеннолетний.")
        else:
            print(f"Вы несовершеннолетний")
    else:
        print("Ошибка: возраст не может быть отрицательным!")

else:
    print("Ошибка: данные не являются числом.")