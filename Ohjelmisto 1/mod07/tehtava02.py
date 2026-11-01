import random

sides = int(input())

def random_number(sides):
    result = random.randint(1, sides)
    return result

result = random_number(sides)

while result != sides:
    print(result)
    result = random_number(sides)

print(result)