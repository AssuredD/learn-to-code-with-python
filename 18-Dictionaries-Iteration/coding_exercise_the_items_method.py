# Declare an invert function that accepts a dictionary object.
# The function should return a new dictionary where the keys and values from the original dictionary are inverted.
# Each key should now be a value, and each value should be a key.
# Assume both the keys and values of the dictionary are immutable.
#
# EXAMPLE:
# my_dict = {
#   "A": "B",
#   "C": "D",
#   "E": "F"
# }
#
# invert(my_dict) => {'B': 'A', 'D': 'C', 'F': 'E'}
print("==========================")

my_dict = {
    "A": "B",
    "C": "D",
    "E": "F"
}


def invert(my_dict):
    results = {}

    for key, value in my_dict.items():
        results[value] = key
    return results


print(invert(my_dict))

# Declare a count_of_value function that accepts a dictionary and an integer.
# It should return a count of the number of times the integer appears
# as a value among the dictionary’s values.
#
# EXAMPLE:
# my_dict = { "a" : 5, "b" : 3, "c" : 5 }
#
# count_of_value(my_dict, 5) => 2
# count_of_value(my_dict, 3) => 1

print("==========================")

my_dict = {"a": 5, "b": 3, "c": 5}


def count_of_value(my_dict, number):
    count = 0

    for _, value in my_dict.items():
        if number == value:
            count += 1
    return count


print(count_of_value(my_dict, 5))
print(count_of_value(my_dict, 3))

# Declare a sum_of_values function that accepts a dictionary and a list of strings.
# The dictionary will have keys of strings and values of numbers.
#
# The function should return the sum of values for dictionary
# keys that are also found in the list.
#
# NOTE: sum is a reserved keyword in Python. Don’t use it as a variable name.
#
# EXAMPLES:
# my_dict = { "a": 5, "b": 3, "c": 10 }
#
# sum_of_values(my_dict, ["a"])            => 5
# sum_of_values(my_dict, ["a", "c"])       => 15
# sum_of_values(my_dict, ["a", "c", "b"])  => 18
# sum_of_values(my_dict, ["z"])            => 0

print("==========================")

my_dict = {"a": 5, "b": 3, "c": 10}


def sum_of_values(my_dict, strings):
    total = 0

    for key, value in my_dict.items():
        if key in strings:
            total += value
    return total


print(sum_of_values(my_dict, ["a"]))
print(sum_of_values(my_dict, ["a", "c"]))
print(sum_of_values(my_dict, ["a", "c", "b"]))
print(sum_of_values(my_dict, ["z"]))
