class Guitar():
    def __init__(self, wood):  # strings, year, nickname):
        self.wood = wood
        # self.strings = strings
        # self.year = year
        # self.nickname = nickname


acoustic = Guitar("Iroko")
electric = Guitar("Mahogany")
print(acoustic.wood)
print(electric.wood)

baritone = Guitar("Iroko")

print(baritone.wood)
print(acoustic)
print(baritone)

a = [1, 2, 3]
b = [1, 2, 3]
