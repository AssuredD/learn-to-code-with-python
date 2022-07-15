# Numbers are immutable
a = 3
b = a

a = 5

print(a)
print(b)

# Mutatble

a = [1, 2, 3]
b = a
a.append(4)
print(a)
print(b)
