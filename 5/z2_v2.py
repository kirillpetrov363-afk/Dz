import random
import statistics
import math

numbers = []
for i in range(100):
    numbers.append(random.randint(1, 100))

mean = statistics.mean(numbers)
median = statistics.median(numbers)
stdev = statistics.stdev(numbers)
total_sum = sum(numbers)
sqrt = round(math.sqrt(total_sum), 2)

print("\n", f"Среднее: {round(mean, 2)}, Медиана: {median}, "
      f"Стандартное отклонение: {round(stdev, 2)}, "
      f"Корень из суммы: {sqrt}", "\n")