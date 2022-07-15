# Declare a Musical class that accepts a name parameter.
# In the initialization process for an object, assign the
# name parameter to a name attribute on the object.
class Musical():
    def __init__(self, name):
        self.name = name


#
# Instantiate a Musical object with the name “Rent”
# and assign it to an “rent" variable.
rent = Musical("Rent")
print(rent.name)
#
# Instantiate a second Musical object with the name “Book of Mormon"
# and assign it to a “mormon” variable.
mormon = Musical("Book of Mormon")
print(mormon.name)
#
# Instantiate a third object from the class with the name “Chicago"
# and assign it to a “chicago” variable.
chicago = Musical("Chicago")
print(chicago.name)

print("=================================")

# Declare a Shape class that accepts a sides parameter.
# In the initialization process for an object, assign the sides parameter to a sides attribute on the object.


class Shape():
    def __init__(self, sides):
        self.sides = sides


# Instantiate a Shape object with 3 sides and assign it to a “triangle" variable.
triangle = Shape(3)
print(triangle.sides)
# Instantiate a Shape object with 4 sides and assign it to a “square" variable.

square = Shape(4)
print(square.sides)
# Instantiate a Shape object with 10 sides and assign it to a “decagon" variable.
decagon = Shape(10)
print(decagon.sides)

print("=================================")

# Declare a Skyscraper class that accepts name and year parameters.

# In the initialization process for an object, assign the name parameter to a name attribute
# and the year parameter to a year attribute.


class Skyscraper():
    def __init__(self, name, year):
        self.name = name
        self.year = year


# Instantiate a Skyscraper object with the name “Empire State Building”  and the year 1931.
# Assign it to a “empire" variable.
empire = Skyscraper("Empire State Building", 1931)

print(empire.name)
print(empire.year)

# Instantiate a Skyscraper object with the name “One World Trade Center” and the year 2014.
# Assign it to a “wtc" variable.
wtc = Skyscraper("One World Trade Center", 2014)

print("=================================")
