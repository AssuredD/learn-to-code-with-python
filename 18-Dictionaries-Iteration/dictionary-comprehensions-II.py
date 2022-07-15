capitals = {
    "New York": "Albany",
    "California": "Sacramento",
    "Texas": "Austin"
}

inverted = {value: key for key, value in capitals.items() if len(key)
            != len(value)}

print(inverted)
