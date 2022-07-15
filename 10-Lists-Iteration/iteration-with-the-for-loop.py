dinner = "Steak and Potatoes"

# for character in dinner:
#     print(character)

numbers = [2, 3, 5, 7, 10]

for number in numbers:
    print(number * number)

print()

novelists = ["Fitzgerald", "Hemingway", "Steinbeck"]

for author in novelists:
    print("The novolist named", author, " is ", len(author), "character long")
    # print(len(author))

total = 0

for number in numbers:
    total = total + number
print(total)
