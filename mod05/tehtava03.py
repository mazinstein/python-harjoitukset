luku = input("Anna luku:")

if luku != "":
    num = float(luku)
    smallest = num
    largest = num

while luku != "":
    num = float(luku)
    if num < smallest:
        smallest = num
    elif num > largest:
        largest = num
    luku = input("Anna luku:")

print(f"Pienin luku: {smallest}")
print(f"Suurin luku: {largest}")