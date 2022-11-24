def divers(n):
    num1 = 0
    for i in range(1, n):
        if n % i == 0:
            num1 += i
    return num1


def comper(n):
    a = divers(n)
    b = divers(a)
    if b == n and b != a:
        return n
    else:
        return None


list = []
b = 0
for j in range(1, 10001):
    if comper(j):
        list.append(comper(j))
print(sum(list))
