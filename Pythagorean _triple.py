def euler():
    for c in range(2, 1000):
        for a in range(1, c):
            b = 1000 - c - a
            if a**2 + b**2 == c**2:
                print(a, b, c, a * b * c)
                return
print(euler())