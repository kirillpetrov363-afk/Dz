import random
import datetime
import array

today = datetime.date.today()
start = today - datetime.timedelta(days=5 * 365)

dates = array.array('i')

# 10 случайных дат
for i in range(10):
    days = random.randint(0, (today - start).days)
    d = start + datetime.timedelta(days=days)
    dates.append(d.toordinal())

# разница между соседними
for i in range(len(dates) - 1):
    d1 = datetime.date.fromordinal(dates[i])
    d2 = datetime.date.fromordinal(dates[i + 1])

    diff = abs(dates[i + 1] - dates[i])

    print("Разница между", d1, "и", d2, ":", diff, "дней")