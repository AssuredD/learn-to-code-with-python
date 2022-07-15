# count = 0

# while count <= 5:
#     print(count)
#     count += 1
# print(count)

# count = 0

# while count <= 5:
#     print(count)
#     count += 1


invalid_number = True

while invalid_number:
    user_value = int(input("Please enter a number greater than 10: "))
    if user_value > 10:
        print("Thanks, that works! {user_value} is a great choice!")
        invalid_number = False
    else:
        print("That doesn't fit! Try again")
