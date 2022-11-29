def fib_1000():
    a, b = 1, 1
    count = 2
    while count < 5000:
        count += 1
        a, b = b, a + b
        if len(str(b)) >= 1000:
            print(b)
            print(count)
            return


fib_1000()