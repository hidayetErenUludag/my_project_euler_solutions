def way_finder(n):
    a = int(input("first grid :"))
    b = int(input("second grid :"))
    c = 1
    d = 1
    for i in range(1, a+b+1):
        c *= i
    for j in range(1, b+1):
        d *= j
    print(c/(d*d))

way_finder(1)