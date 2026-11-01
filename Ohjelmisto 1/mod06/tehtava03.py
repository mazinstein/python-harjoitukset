number = int(input("Enter number: "))
is_prime = True

if number < 2:
    is_prime = False

for i in range(2, number):
    if number % i == 0:
        is_prime = False

if is_prime:
    print(f"{number} is prime")
else:
    print(f"{number} not prime")