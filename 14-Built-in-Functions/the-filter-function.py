animals = ["elephant", "horse", "cat", "giraffe", "cheetah", "dog"]

long_words_animals = [animal for animal in animals if len(animal) > 5]

print(long_words_animals)

# Using the filter function


def is_long_animal(animal):
    return len(animal) > 5


print(list(filter(is_long_animal, animals)))
