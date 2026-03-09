def add(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ошибка типа")
    return a + b


def sub(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ошибка типа")
    return a - b


def mul(a: float, b: float) -> float:
    return a * b


def div(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Нельзя делить на 0")
    return a / b


def power(a: float, b: float) -> float:
    return a ** b


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Число < 0")
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def sin(x: float) -> float:
    import math
    return math.sin(x)


def median(nums: list[float]) -> float:
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2


while True:

    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Факториал")
    print("7. Синус")
    print("8. Медиана")
    print("9. Выход")
    print("--------------------")

    op = input("Операция: ")

    if op == "9":
        break

    if op == "1":
        a = float(input("Слагаемое 1: "))
        b = float(input("Слагаемое 2: "))
        print(">>>", add(a, b))

    elif op == "2":
        a = float(input("Уменьшаемое: "))
        b = float(input("Вычитаемое: "))
        print(">>>", sub(a, b))

    elif op == "3":
        a = float(input("Число 1: "))
        b = float(input("Число 2: "))
        print(">>>", mul(a, b))

    elif op == "4":
        a = float(input("Делимое: "))
        b = float(input("Делитель: "))
        print(">>>", div(a, b))

    elif op == "5":
        a = float(input("Основание: "))
        b = float(input("Степень: "))
        print(">>>", power(a, b))

    elif op == "6":
        n = int(input("Число: "))
        print(">>>", factorial(n))

    elif op == "7":
        x = float(input("Число: "))
        print(">>>", sin(x))

    elif op == "8":
        nums = list(map(float, input("Список чисел: ").split()))
        print(">>>", median(nums))

    print("--------------------")