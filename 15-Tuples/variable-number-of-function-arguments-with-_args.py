def accept_stuff(*args):
    print(type(args))
    print(args)


accept_stuff(1)
accept_stuff(1, 3, 5)
accept_stuff(1, 2, 3, 4, 5)
accept_stuff()


def my_max(nonsense, *numbers):
    print(nonsense)
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest


print(my_max("Ahazam", 1))
print(my_max("Hoorah", 1, 3))
print(my_max("Bonanaza", 1, 3, 9, 6, 7, 8, -14))

print("Reverse")


def my_max(*numbers, nonsense):
    print(nonsense)
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest


print(my_max(1, 2, 3, 3,  nonsense="Ahazam"))
print(my_max(1, 3, 4, nonsense="Hoorah"))
