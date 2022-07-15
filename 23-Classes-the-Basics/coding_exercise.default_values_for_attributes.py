# Declare a Zombie class that accepts health and brains_eaten parameters.
class Zombie():
    def __init__(self, health=100, brains_eaten=5):
        self.health = health
        self.brains_eaten = brains_eaten

# In the initialization process for a Zombie object, assign the
# two parameters to two attributes with the same name.
#
# If the instantiation does not pass a health parameter,
# it should be assigned a default value of 100.
#
# If the instantiation does not pass a brains_eaten parameter,
# it should be assigned a default value of 5.


# Instantiate a Zombie object with 80 health and 5 brains eaten.
# Assign it to a “bob” variable.
bob = Zombie(80, 5)
print(bob.health)
print(bob.brains_eaten)
#
# Instantiate a Zombie object with 120 health and 3 brains eaten.
# Assign it to a “sally” variable.
sally = Zombie(120, 3)
print(sally.health)
print(sally.brains_eaten)
#
# Instantiate a Zombie object with no custom parameters.
# Assign it to a “benjamin” variable.
benjamin = Zombie()
print(benjamin.health)
print(benjamin.brains_eaten)
#
# Practice instantiating the objects with both positional and keyword arguments.
