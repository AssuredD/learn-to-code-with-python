# Define an only_evens function that accepts a list of numbers.
# It should return a new list consisting of only the even numbers from the original list.
#
# EXAMPLES
# only_evens([4, 8, 15, 16, 23, 42]) => [4, 8, 16, 42]
# only_evens([1, 3, 5])              => []
# only_evens([])                     => []

print("============Even numbers from list challenge ===========")


def only_evens(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


print(only_evens([4, 8, 15, 16, 23, 42]))
print(only_evens([1, 3, 5]))
print(only_evens([]))


# Define a long_strings function that accepts a list of strings.
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# EXAMPLES
# long_strings(["Hello", "Goodbye", "Sam"])  => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"])        => []
# long_strings([])                           => []


print("============Even numbers from list challenge ===========")


def long_strings(strings):
    results = []

    for string in strings:
        if len(string) >= 5:
            results.append(string)
    return results


print(long_strings(["Hello", "Goodbye", "Sam"]))
print(long_strings(["Ace", "Cat", "Job"]))
print(long_strings([]))
