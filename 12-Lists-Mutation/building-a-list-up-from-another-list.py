print("========Square list numbers==========")

powerball_numbers = [4, 8, 15, 16, 23, 42]


def squares(numbers):

    squared_number_list = []

    for number in numbers:
        squared_number_list.append(number ** 2)
    return squared_number_list


print(squares(powerball_numbers))

print("========Convert list numbers to floats==========")


def convert_to_float(numbers):

    floats = []

    for number in numbers:
        floats.append(float(number))
    return floats


print(convert_to_float(powerball_numbers))


print("======== Even or odd boolean from a number list==========")


def even_or_odd(numbers):
    boolean_list = []

    for number in numbers:
        if number % 2 == 0:
            boolean_list.append(True)
        else:
            boolean_list.append(False)
    return boolean_list


print(even_or_odd(powerball_numbers))
