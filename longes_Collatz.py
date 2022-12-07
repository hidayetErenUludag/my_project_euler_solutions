import matplotlib as plt

def collatz(i):
    count = 0
    while i > 1:
        if i % 2 == 0:
            i = i/2
            count += 1
        else:
            i = 3*i + 1
            count += 1
    return count


lists = []
for j in range(1, 10001):
    list.append([collatz(j), j])

print(sorted(list))

