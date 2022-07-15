ingredient1 = "Pasta"
ingredient2 = "Sausage"

# if ingredient1 == "Pasta":
#     if ingredient2 == "Meatballs":
#         print("I recommend making pasta and meatballs")
#     else:
#         print("I recommend making plain pasta")
# else:
#     print("I have no recommendations")


if ingredient1 == "Pasta" and ingredient2 == "Meatballs":
    print("I recommend making pasta and meatballs")
elif ingredient1 == "Pasta":
    print("I recommend making plain pasta")
else:
    print("I have no recommendations")

print("\n")

car1 = "HONDA"
car2 = "TOYOTA"

if car1 == "BMW" and car2 == "BENZ":
    print("The owner of both cars is a middle class")
elif car1 == "BMW":
    print("The owner is a working class")
else:
    print("This person is on state benefit")
