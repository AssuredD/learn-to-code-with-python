numbers = [4, 8, 15, 16, 23, 42]
cubes = [number ** 3 for number in numbers]
print(cubes)


def cubes(number):
    return number ** 3


print(list(map(cubes, numbers)))


animals = ["cat", "bear", "zebra", "donkey", "cheetah"]

# lengths = [len(animal) for animal in animals]
# print(lengths)


# def lengths(animal):
#     return len(animal)


# print(list(map(lengths, animals)))

print(list(map(len, animals)))
