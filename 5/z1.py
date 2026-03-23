import random
import string
from pathlib import Path

folder = Path("random_files")
folder.mkdir(exist_ok=True)

file_list = []

for i in range(10):

    filename = ""
    all_symbols = string.ascii_letters + string.digits
   
    for _ in range(8):
        filename = filename + random.choice(all_symbols)
   
    filename = filename + ".txt"
   
    file_path = folder / filename
   
    file_path.touch()
   
    file_list.append(file_path)

for file in file_list:
    print(file.absolute())
    print("\n")

