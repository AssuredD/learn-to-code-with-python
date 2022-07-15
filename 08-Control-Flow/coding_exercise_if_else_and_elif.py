# Declare a negative_energy function that accepts a numeric argument and returns its absolute value.
# The absolute value is the number's distance from zero.
#
# negative_energy(5)    => 5
# negative_energy(10)   => 10
# negative_energy(-5)   => 5
# negative_energy(-8)   => 8
# negative_energy(0)    => 0


def negative_energy(value):
    return abs(value)


print(negative_energy(5))
print(negative_energy(10))
print(negative_energy(-5))
print(negative_energy(-8))
print(negative_energy(0))

print()
# Alternative programme code


def negative_energy_2(value):
    if value >= 0:
        return value
    elif value < 0:
        return -1 * value


print(negative_energy_2(-10))
print(negative_energy_2(-7))
print(negative_energy_2(0))
print(negative_energy_2(9))
print(negative_energy_2(3/4))
