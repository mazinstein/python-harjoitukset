def remove_odd(numbers):
    new_list = []

    for number in numbers:
        if number % 2 == 0:
            new_list.append(number)

    return new_list


numbers = [1, 2, 3, 4, 5, 6]

new_numbers = remove_odd(numbers)

print(numbers)
print(new_numbers)