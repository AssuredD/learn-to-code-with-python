# Define a function that iterates over a list of numbers,
# multiplies each number by one less than its index position
# and returns the total sum of those products.

def sum_of_number_by_one_less_than_index_position(numbers):
    total = 0

    for i, value in enumerate(numbers):
        total = (i - 1) * value
    return total


numbers = [1, 2, 3, 4, 5]

print(sum_of_number_by_one_less_than_index_position(numbers))
