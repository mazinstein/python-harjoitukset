import random
num = random.randint(1, 10)
inp = int(input("Arvaa luku 1-10:"))

while inp != num:
    if inp < num:
        print("Liian pieni")
        inp = int(input("Arvaa luku 1-10: "))
    else:
        print("Liian suuri")
        inp = int(input("Arvaa luku 1-10: "))

print("Oikein")