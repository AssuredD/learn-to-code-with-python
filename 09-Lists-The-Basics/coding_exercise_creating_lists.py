# Create an empty list and assign it to the variable "empty".

empty = []

# Create a list with a single Boolean — True — and assign it to the variable "active".

active = [True]

# Create a list with 5 integers of your choice and assign it to the variable "favorite_numbers".

favorite_numbers = [77, 78, 8, 10, 15]
# Create a list with 3 strings  — "red", "green", "blue" — and assign it to the variable "colors".

colors = ["red", "green", "blue"]

# Declare an is_long function that accepts a single list as an argument
# It should return True if the list has more than 5 elements, and False otherwise


def is_long(list):
    return len(list) > 5


list = [77, 78, 8, 10, 15, 23]

print(is_long(list))
