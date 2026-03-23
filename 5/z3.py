import random
import string
import json

first_names = ["Kirill", "Andrey", "Vitya", "Masha", "Liza", "Anna"]
last_names = ["Petrov", "Kirillov", "Gubov", "Gorenkov", "Brawn", "Lib"]

name = random.choice(first_names) + " " + random.choice(last_names)
age = random.randint(18, 65)

email = name.lower().replace(" ", ".") + "@mail.ru"

symbols = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choices(symbols, k=12))

user_data = {
    "name": name,
    "age": age,
    "email": email,
    "password": password
}

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user_data, file, indent=4)

with open("user.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print(json.dumps(loaded_data, indent=4))