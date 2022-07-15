# Declare a delete_all function that accepts a list of strings and a target string
# Remove all occurrences of the target string from the list and return it
#
# EXAMPLES
# delete_all([1, 3, 5], 3)  => [1, 5]
# delete_all([5, 3, 5], 5)  => [3]
# delete_all([4, 4, 4], 4)  => []
# delete_all([4, 4, 4], 6)  => [4, 4, 4]
print("==========Remove all occurrences of a target string and return it challenge======")


def delete_all(items, target):
    while target in items:
        items.remove(target)
    return items

# def delete_all(strings, target):
#     results = []

#     for string in strings:
#         if string == target:
#             del string
#         else:
#             results.append(string)

#     return results


print(delete_all([1, 3, 5], 3))
print(delete_all([5, 3, 5], 5))
print(delete_all([4, 4, 4], 4))
print(delete_all([4, 4, 4], 6))

# Declare a push_or_pop function that accepts a list of numbers
# Build up and return a new list by iterating over the list of numbers
# If a number is greater than 5, add it to the end of the new list
# If a number is less than or equal to 5, remove the last element added to the new list
# Assume the order of numbers in the argument will never require removing from an empty list
#
# EXAMPLES
# push_or_pop([10])            => [10]
# push_or_pop([10, 4])         => []
# push_or_pop([10, 20, 30])    => [10, 20, 30]
# push_or_pop([10, 20, 2, 30]) => [10, 30]

print("==========if number greate 5 add to end of new list, if number less than or equal to 5, remove the last element added to the new list challenge======")


def push_or_pop(numbers):
    new_number_list = []

    for number in numbers:
        if number > 5:
            new_number_list.append(number)
        else:
            new_number_list.pop()
    return new_number_list


print(push_or_pop([10]))
print(push_or_pop([10, 4]))
print(push_or_pop([10, 20, 30]))
print(push_or_pop([10, 20, 2, 30]))
