# Define a divisible_by_three_and_four function that accepts a number as its argument.
# It should return True if the number is evenly divisible by both 3 and 4 .
# It should return False otherwise.
#
# divisible_by_three_and_four(3)   => False
# divisible_by_three_and_four(4)   => False
# divisible_by_three_and_four(12)  => True
# divisible_by_three_and_four(18)  => False
# divisible_by_three_and_four(24)  => True

def divisible_by_three_and_four(number):
    if number % 3 == 0 and number % 4 == 0:
        return "True"
    else:
        return "False"


print(divisible_by_three_and_four(3))
print(divisible_by_three_and_four(4))
print(divisible_by_three_and_four(12))
print(divisible_by_three_and_four(18))
print(divisible_by_three_and_four(24))

# Declare a string_theory function that accepts a string as an argument.
# It should return True if the string has more than 3 characters
# and starts with a capital “S”. It should return False otherwise.
#
# string_theory("Sansa") => True
# string_theory("Story") => True
# string_theory("See") => False
# string_theory("Fable") => False

print("====================")


def string_theory(word):
    if len(word) > 3 and word.capitalize() and word[0] == "S":
        return "True"
    elif len(word) <= 3:
        return "False"
    else:
        return "False"


print(string_theory("Sansa"))
print(string_theory("Story"))
print(string_theory("See"))
print(string_theory("Fable"))

print("+++++++++++++++++++")


def string_theory(word):
    return len(word) > 3 and word.capitalize() and word[0] == "S"


print(string_theory("Sansa"))
print(string_theory("Story"))
print(string_theory("See"))
print(string_theory("Fable"))
