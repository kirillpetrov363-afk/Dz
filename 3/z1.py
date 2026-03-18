def multiply(numbers: list[int], multiplier: int = 2) -> list[int]:
#создаём пустой список с подсказкой типа
    result: list[int] = []     
#Проходим по каждому элементу списка numbers
#Переменная n по очереди будет равна каждому числу из списка
    for n in numbers:
#берём текущее число (n) × множитель → добавляем результат в список result   
        result.append(n * multiplier)
#Когда цикл закончился возвращаем заполненный список
    return result
#Короткая безымянная функция lambda делает то же самое
multiply_lambda = lambda numbers, multiplier=2: \
    list(map(lambda x: x * multiplier, numbers))
#Прочитали строку  разбили по пробелам каждую часть сделали int собрали в список
number = list(map(int, input("Введите список чисел через пробел: ").split()))
mult = input("Введите множитель (по умолчанию 2): ")

if mult == "":
    mult = 2
#Если пользователь просто нажал Enter используем  просто 2
else:
    mult = int(mult)
#Иначе пытаемся превратить введённую строку в int
print("Результат (функция):", multiply(number, mult))
#Вызываем обычную функцию multiply дальше печатаем что вернула
print("Результат (лямбда):", multiply_lambda(number, mult))
#Вызываем lambda-версию дальше печатаем что вернула