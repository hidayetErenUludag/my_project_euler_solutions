
def factorial_digit_sum(n):
    b = 1
    c = 0
    for i in range(1, n+1):
        b = i*b
    a = [int(x) for x in str(b)]
    print(sum(a))


factorial_digit_sum(100)

