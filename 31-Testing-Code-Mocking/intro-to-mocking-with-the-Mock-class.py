from unittest.mock import Mock

pizza = Mock()
print(pizza)
print(type(pizza))

pizza.configure_mock(
    size="Large",
    price=19.99,
    toppings=["pepperoni", "Muschroom", "sausage"]
)


# pizza.size = "Large"
# pizza.price = 19.99
# pizza.toppings = ["pepperoni", "Muschroom", "sausage"]

print(pizza.size)
print(pizza.price)
print(pizza.toppings)

# print(pizza.anything)
# print(pizza.anything.we.want)

print(pizza.cover_with_cheese())
print(pizza.cover_with_cheese())