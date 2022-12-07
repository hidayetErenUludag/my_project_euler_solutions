import math
import time


seconds = time.time()


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def quadratic(n, a, b):
    return n ** 2 + n * a + b


def quadratic_primes(rangea, rangeb):
    prime_counter = 0
    a, b = 0, 0
    for i in rangea:
        for j in rangeb:
            primes = 0
            n = 0
            while is_prime(quadratic(n, i, j)):
                n += 1
                primes += 1
            if primes > prime_counter:
                prime_counter = primes
                a, b = i, j
    return prime_counter, (a*b)


a = range(-1000, 1001)
b = range(-1000, 1001)
print(quadratic_primes(a,b))
end = time.time()
print("--- %s seconds ---" % (time.time() - seconds))
