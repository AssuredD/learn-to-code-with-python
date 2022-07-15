# Define a split_in_two function that accepts a list and a number.
# If the number is even, return the list elements from the third element to the end of the list.
# If the number is odd, return the list elements from index 0 (inclusive) to 2 (exclusive)
#
# EXAMPLE:
# values = ["a", "b", "c", "d", "e", "f"]
# split_in_two(values, 3)     => ["a", "b"]
# split_in_two(values, 4)     => ["c", "d", "e", "f"]
# split_in_two(values, 1)     => ["a", "b"]
# split_in_two(values, 10)    => ["c", "d", "e", "f"]


def split_in_two(elements, number):
    if number % 2 == 0:  # even
        return elements[2:]
    else:  # odd
        return elements[:2]


Elements = ["a", "b", "c", "d", "e", "f"]

print(split_in_two(Elements, 3))
print(split_in_two(Elements, 4))
print(split_in_two(Elements, 1))
print(split_in_two(Elements, 10))
