numbers = []
inp = input("Enter number: ")

while inp != "":
    numbers.append(int(inp))
    inp = input("Enter number: ")

numbers.sort(reverse=True)

for i in numbers[0:5]:
    print(i)