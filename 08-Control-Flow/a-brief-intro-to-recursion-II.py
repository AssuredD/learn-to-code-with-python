def reverse(str1):
    return str1[::-1]


print(reverse("Straw"))

print("\n")

# Alternative solution


def reverse1(str):
    start_index = 0
    last_index = len(str) - 1  # -1
    reversed_string = ""

    while last_index >= start_index:
        reversed_string += str[last_index]
        last_index -= 1
    return reversed_string


print(reverse1("Edens garden"))

# Recursion solution


def reverse2(str2):
    if len(str2) <= 1:
        return str2
    return str2[-1] + reverse2(str2[0:-1])


print(reverse2("straw"))
