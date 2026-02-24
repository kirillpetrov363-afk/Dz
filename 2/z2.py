#данные
dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
# пустое множество для ключей
kluchi = set()
# пустое множество для значений          
znacheniya = set()  

# циикл по словарю
for k in dct:
    # добавляем ключ в множество           
    kluchi.add(k)       
    # добавляем значение в множество
    znacheniya.add(dct[k])   

# объединяем два множества
obedinenie = kluchi | znacheniya   
# выводит результаты
print("Множество ключей:", kluchi)
print("Множество значений:", znacheniya)
print("Объединение множеств:", obedinenie)