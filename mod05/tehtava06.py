import random

määrä = int(input("Anna pisteiden määrä:"))
count = 0
checked = 0

while checked < määrä:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    checked += 1

    if x ** 2 + y ** 2 < 1:
        count += 1

result = 4 * count / määrä
print(result)