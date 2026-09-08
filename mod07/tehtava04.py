def sum_numbers(numbers):
    result = 0

    for number in numbers:
        result += number

    return result


numbers = [1, 2, 3, 4, 5]

result = sum_numbers(numbers)

print(result)