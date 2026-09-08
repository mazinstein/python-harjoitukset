import random
def random_number():
     result = random.randint(1, 6)
     return result

result = random_number()

while  result != 6 :
    print(result)
    result = random_number()

print(result)
