metals = ["gold", "silver", "platinum", "palladium"]

print(list(filter(lambda metal: len(metal) > 5, metals)))
print(list(filter(lambda el: len(el) > 5, metals)))
print(list(filter(lambda metal: "p" in metal, metals)))
print(list(map(lambda metal: metal.count("l"), metals)))
print(list(map(lambda metal: metal.replace("s", "$"), metals)))
