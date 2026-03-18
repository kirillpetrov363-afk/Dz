def append_to_file(text, filename):
   
#Добавление текста
#'a'(append)-открываем файл для добавления в конец
#encoding='utf-8' - для поддержки русского текста
    with open(filename, 'a', encoding='utf-8') as file:
#Добавляем текст и переводим строку
        file.write(text + '\n')

#Чтение и анализ файла
#'r'(read)-открываем файл для чтения
    with open(filename, 'r', encoding='utf-8') as file:
#readlines() читает все строки и возвращает список
#Каждая строка содержит символ '\n' в конце
        lines = file.readlines()

#Вывод реезультат
    print(f"\nЧётные строки файла '{filename}':")
#enumerate создает пары (номер, строка), start=1 начинает с 1
    for number, line in enumerate(lines, start=1):
#Проверяем чётный ли номер строки
        if number % 2 == 0:
#rstrip'\n' удаляет символ перевода строки в конце,Строка {number}-выводит строка(номер)
            print(f"Строка {number}: {line.rstrip('\n')}")
            
#Добавляем первую строку
append_to_file("Это первая строка", "gg.txt")
#Добавляем вторую строку
append_to_file("Вторая строка добавлена", "gg.txt")
#Добавляем третью строку
append_to_file("Третья строка", "gg.txt")
#Добавляем четвёртую строку
append_to_file("Четвёртая запись здесь", "gg.txt")
#Добавляем пятую строку
append_to_file("Пятая — нечётная", "gg.txt")
