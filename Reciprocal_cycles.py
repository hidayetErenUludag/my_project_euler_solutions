import matplotlib.pyplot as plt


def reciprocal(n):
    for i in range(2, n):
        if 1 == (10**i % n):
            return i
    return 0


a = []
for j in range(2,1001):
    a.append(reciprocal(j))
plt.plot(a)


long = [max(reciprocal(i) for i in range(2, 1001))]
print([i for i in range(2, 1001) if reciprocal(i) == long[0]])

plt.show()
