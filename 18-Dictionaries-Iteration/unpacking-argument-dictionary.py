def height_to_metres(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 0.0254


print(height_to_metres(5, 11))

stats = {
    "feet": 5,
    "inches": 11
}

print(height_to_metres(**stats))
