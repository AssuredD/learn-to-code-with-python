values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values = [5, 10, 15, 20, 25, 30]


def odds_sum(numbers):
    total = 0
    for number in numbers:
        if number % 2 != 0:
            total += number
    return total


print(odds_sum(values))
print(odds_sum(other_values))

print("--------Greatest number challenge solution-----------\n")


def greatest_number(numbers):
    return max(numbers)


print(greatest_number([1, 2, 3]))
print(greatest_number([3, 2, 1]))
print(greatest_number([4, 5, 5]))
print(greatest_number([-3, -2, -1]))

print("--------Alternative Greatest number challenge solution-----------\n")


def greatest_number2(numbers):
    greatest = numbers[0]

    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest


print(greatest_number2([1, 2, 3]))
print(greatest_number2([3, 2, 1]))
print(greatest_number2([4, 5, 5]))
print(greatest_number2([-3, -2, -1]))
