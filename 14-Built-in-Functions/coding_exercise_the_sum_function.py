# Declare a greater_sum function that accepts two lists of numbers.
# It should return the list with the greatest sum.
# You can assume the lists will always have different sums.
#
# EXAMPLES
# greater_sum([1, 2, 3], [1, 2, 4]) => [1, 2, 4]
# greater_sum([4, 5], [2, 3, 6])    => [2, 3, 6]
# greater_sum([1], [])              => [1]
print("======Greater sum list Challenge========")


def greater_sum(numbers1, numbers2):
    if sum(numbers1) > sum(numbers2):
        return numbers1
    return numbers2


print(greater_sum([1, 2, 3], [1, 2, 4]))
print(greater_sum([4, 5], [2, 3, 6]))
print(greater_sum([1], []))

# Declare a sum_difference function that accepts two lists of numbers.
# It should return the difference between the sum of values in the first list and the second list
#
# EXAMPLES
# sum_difference([1, 2, 3], [1, 2, 4]) => 6 - 7 => -1
# sum_difference([4, 5], [2, 3, 6])    => 9 - 11 => -2
# sum_difference([1], [])              => 1

print("======Sum difference list Challenge========")


def sum_difference(values1, values2):
    return sum(values1) - sum(values2)


print(sum_difference([1, 2, 3], [1, 2, 4]))
print(sum_difference([4, 5], [2, 3, 6]))
print(sum_difference([1], []))
