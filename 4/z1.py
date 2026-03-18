from math import factorial
#Список квадратов первых 10 натуральных чисел.List Comprehension-[выражение for элемент in последовательность if условие]
#создания списков на основе существующих последовательностей.
def squares():
    squares = [i**2 for i in range(1, 11)]
    print("\nКвадраты первых 10 натуральных чисел:", squares)
#Словарь дней недели.Dict Comprehension-{ключ: значение for элемент in последовательность if условие}
#для создания словарей.
def days():
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    week = {day: number for number, day in enumerate(days, 1)}
    print("\nСловарь дней недели:", week)
#Множество тегов в нижнем регистре
def tags():
    libs = ["RUST", "FastAPI", "NuMpy", "GO", "JAVAScript", "C#", "Python", "ReAcT"]
    tags = {lib.lower() for lib in libs}
    print("\nМножество тегов в нижнем регистре:", tags)
#Только чётные числа
def numbers():
    numbers = [1, 3, 4, 87, 98, 15, 7, 4, 22, 45, 63, 12, 8, 91, 33, 56]
    result = [n for n in numbers if n % 2 == 0]
    print("\nТолько чётные числа:", result)
#Словарь чисел и их факториало
def factorials():
    fact = {i: factorial(i) for i in range(1, 6)}
    print("\nСловарь чисел и их факториалов:", fact)
#Меню выбора
def menu():
    print("\n")
    print("Меню:")
    print("\n")
    print("1.Список квадратов первых 10 натуральных чисел")
    print("2.Словарь дней недели")
    print("3.Множество тегов в нижнем регистре")
    print("4.Только чётные числа")
    print("5.Словарь чисел и их факториалов")
    print("0.Exit")
    print("\n")
#Выбор функции/подзаданиия в задании
while True:
    menu()
    op = input("Введите номер пункта(0-5):")
    if op == '1':
        squares()
    elif op == '2':
        days()
    elif op == '3':
        tags()
    elif op == '4':
        numbers()
    elif op == '5':
        factorials()
    elif op == '0':
        print("\nВыход")
        break
    else:
        print("\nТакого пункта нет")

    input("\nНажмите Enter чтобы продолжить")