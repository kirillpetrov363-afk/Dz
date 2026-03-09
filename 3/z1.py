def multiply(numbers: list[int], multiplier: int = 2) -> list[int]:
    
    result: list[int] = []

    for n in numbers:
        result.append(n * multiplier)

    return result

multiply_lambda = lambda numbers, multiplier=2: list(map(lambda x: x * multiplier, numbers))

number = list(map(int, input("Введите список чисел через пробел: ").split()))
mult = input("Введите множитель (по умолчанию 2): ")

if mult == "":
    mult = 2
else:
    mult = int(mult)

print("Результат (функция):", multiply(number, mult))
print("Результат (лямбда):", multiply_lambda(number, mult))