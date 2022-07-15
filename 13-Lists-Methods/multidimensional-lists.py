bubble_tea_flavours = [
    ["Honeydew", "Mango", "Passion fruit"],
    ["Peach", "Plum", "Strawberry", "Taro"],
    ["Kiwi", "Chocolate"]
]

# print(len(bubble_tea_flavours))
# print(bubble_tea_flavours[0])
# print(bubble_tea_flavours[1])
# print(bubble_tea_flavours[-1])
# print(len(bubble_tea_flavours[1]))


# print(bubble_tea_flavours[1][2])
# print(bubble_tea_flavours[0][0])
# print(bubble_tea_flavours[2][1])

all_flavours = []

for flavour_pack in bubble_tea_flavours:
    for flavour in flavour_pack:
        all_flavours.append(flavour)

print(all_flavours)
