def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


def j_finder(nums, millionth):
    j = 1
    while j * factorial(nums-1) < millionth:
        j += 1
    return j-1


def lex_permutation():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    new = []
    mil = 1000000
    for i in range(10):
        c = j_finder(len(a), mil)
        mil = mil - c * factorial(len(a)-1)
        new.append(a[c])
        a.remove(a[c])
    print(new)


lex_permutation()
