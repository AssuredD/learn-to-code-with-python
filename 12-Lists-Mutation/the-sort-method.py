tempratures = [40, 28, 52, 66, 35]
tempratures.sort()
tempratures.reverse()
print(tempratures)

print()

coffees = ["Latte", "Espresso", "Macchiato", "Frappucino"]
coffees.sort()
coffees.reverse()
print(coffees)

coffees = ["Latte", "espresso", "macchiato", "Frappucino"]
coffees.sort()
print(coffees)


# This method does not modify the original list
coffees = ["Latte", "Espresso", "Macchiato", "Frappucino"]
print(sorted(coffees))
