a, b = 1, 1
total = 0
while a <= 4000000:
    total += a
a, b = b, a+b

print(total)
