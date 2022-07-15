# Define a Chocolate class that accepts and assigns a cacao_content attribute.

# Define a "sweet" class method that returns a
# Chocolate object with a cacao_content value of 30.

# Define a "semisweet" class method that returns a
# Chocolate object with a cacao_content value of 50.

# Define a "bittersweet" class method that returns a
# Chocolate object with a cacao_content value of 70.

# Define a "bitter" class method that returns a
# Chocolate object with a cacao_content value of 99.

class Chocolate():
    def __init__(self, cacao_content):
        self.cacao_content = cacao_content

    @classmethod
    def sweet(cls):
        return cls(cacao_content=30)

    @classmethod
    def semisweet(cls):
        return cls(cacao_content=50)

    @classmethod
    def bittersweet(cls):
        return cls(cacao_content=70)

    @classmethod
    def bitter(cls):
        return cls(cacao_content=99)


sweet_lover = Chocolate.sweet()
print(sweet_lover.cacao_content)

semi_sweet_lover = Chocolate.semisweet()
print(semi_sweet_lover.cacao_content)

bitter_sweet_lover = Chocolate.bittersweet()
print(bitter_sweet_lover.cacao_content)

bitter_lover = Chocolate.bitter()
print(bitter_lover.cacao_content)
