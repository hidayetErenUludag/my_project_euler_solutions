
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


def sorter(n):
    count_global = 0
    if count_global < collatz(n):
        count_global = collatz(n)
        num_global = n
    else:
        count_global = count_global
        num_global = n
    return (count_global, num_global)


for i in range(1, 1000001):
    print(sorter(i))
