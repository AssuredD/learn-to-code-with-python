# Declare a months tuple with the last 4 months of the year (September, October, November, December) as strings.
# Make sure the first letter of each month is capitalized.
print("======last 4 Months of Year Tuple====")

months = ("September", "October", "November", "December")
print(months)
print(type(months))


# Create a faves variable with a list of your 3 three favorite movies as strings.
# Use the tuple function to convert the list to a tuple and save the result in a movies variable.
print("======3 Favourite Movies====")

faves = ["A few Good Men", "Castle and Castle", "Greenleaf"]
movies = tuple(faves)
print(type(movies))

# Create a numbers_a, numbers_b, and numbers_c tuple.
# Each tuple should contain 3 integers.
# Declare an all_numbers tuple containing these three tuples.
print("======All Numbers====")

numbers_a = (1, 2, 3)
numbers_b = (4, 5, 6)
numbers_c = (7, 8, 9)

all_numbers = (numbers_a, numbers_b, numbers_c)
print(all_numbers)
print(type(all_numbers))
