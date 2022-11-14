def tri_num(n):
    num = ((n+1)*n)//2
    return num


def high_div(m):
    count = 1
    a = tri_num(m)
    for j in range(1, a):
        if a % j == 0:
            count += 1
        else:
            count = count
    print(count)
    print(tri_num(m))


print(tri_num(12375))