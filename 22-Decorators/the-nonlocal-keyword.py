def outer():
    bubble_tea_flavour = "Black"

    def inner():
        nonlocal bubble_tea_flavour
        bubble_tea_flavour = "Taro"

    inner()

    return bubble_tea_flavour


print(outer())
