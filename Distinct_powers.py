distinct = []

for a in range(2,101):
    for b in range(2, 101):
        distinct.append(a**b)
new = [*set(distinct)]
print(len(new))


