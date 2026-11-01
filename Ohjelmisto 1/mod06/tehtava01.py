import random
määrä = int(input("how many? "))
result = 0

for i in range(määrä):
    dice = random.randint(1, 6)
    print(dice)
    result += dice

print(f"Sum = {result}")