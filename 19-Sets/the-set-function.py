print(set([1, 2, 3]))
print(set([1, 2, 3, 3, 2, 1]))


print(set([1, 2]))
print(set([1, 2, 1, 2, 1]))

print(set("abc"))
print(set("aabbcc"))

print(set({"key": "value"}))

# Creating a list of only unique values if the order is irrelevant

philosophers = ["Plato", "Socrates", "Aristotle",
                "Pythagoras", "Socrates", "Plato"]
philosophers_set = set(philosophers)
philosophers = list(philosophers_set)
print(philosophers)
