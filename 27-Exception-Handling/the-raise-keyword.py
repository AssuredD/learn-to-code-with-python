def add_positive_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise ValueError(
                "One or both of the values is invalid. Both numbers must be positive integers.")
        return a + b

    except ValueError as e:
        return f"Caught the ValueError: {e}"


print(add_positive_numbers(3, 4))
print(add_positive_numbers(-10, 4))
print(add_positive_numbers(6, -4))
