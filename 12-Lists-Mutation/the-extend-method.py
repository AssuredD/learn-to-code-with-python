# The extend method mutates the original list

mountains = ["Mount Everest", "K2"]
print(mountains)

mountains.extend(["Kilimanjaro", "Fako Mountain", "Lhotse", "Kalu"])
print(mountains)

extra_mountains = ["Cho Oyu", "Dhaulagiri"]
mountains.extend(extra_mountains)
print(mountains)

print()

# This method creates a brand new list

steaks = ["Tenderloin", "New York Strip"]
more_steaks = ["T-Bone", "Ribeye"]

my_meal = steaks + more_steaks
print(my_meal)
print(steaks)
print(more_steaks)

steaks += more_steaks
print(steaks)
