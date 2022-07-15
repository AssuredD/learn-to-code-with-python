# Define a string_adder function that accepts two strings (a and b) as arguments.
# It should return a concatenated version of the arguments with a space in between.
# If the user does not pass in arguments, both arguments should default to an empty string.
#
# EXAMPLES
# string_adder("Hello", "World")      => "Hello World"
# string_adder("Emilio", "Estevez")   => "Emilio Estevez"
# string_adder()                      => " "
# string_adder("Tiger")               => "Tiger "


def string_adder(a="", b=""):
    return a + " " + b


print(string_adder("Hello", "World"))
print(string_adder("Emilo", "Estevez"))
print(string_adder())
print(string_adder("Tiger"))

# Define a multiplier function that accepts three integers as arguments.
# Return the product of the arguments. The product is the total when values are multiplied together.
# If the user does not provide any arguments, all three parameters should have default arguments of 1.
#
# EXAMPLES
# multiplier(2, 2, 2)    => 8
# multiplier()           => 1
# multiplier(3)          => 3
# multiplier(2, 5)       => 10


def multiply_numbers(a=1, b=1, c=1):
    return a * b * c


print(multiply_numbers(3, 6, 2))
print(multiply_numbers())
print(multiply_numbers(9))
print(multiply_numbers(7, 5))
