# Function to check if a given number is prime

import time
start_time = time.time()


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def evaluate_quadratic(n, a, b):
    return n ** 2 + a * n + b


# Function to find the maximum number of consecutive primes for the given range of a and b
def find_max_consecutive_primes(a_range, b_range):
    max_consecutive_primes = 0
    max_a = 0
    max_b = 0

    # Try all possible values of a and b within the given ranges
    for a in a_range:
        for b in b_range:
            consecutive_primes = 0
            # Evaluate the quadratic expression for n = 0, 1, 2, ...
            # until we get a non-prime number
            n = 0
            while is_prime(evaluate_quadratic(n, a, b)):
                consecutive_primes += 1
                n += 1
            # Update the maximum number of consecutive primes and the corresponding values of a and b
            if consecutive_primes > max_consecutive_primes:
                max_consecutive_primes = consecutive_primes
                max_a = a
                max_b = b

    # Return the product of the coefficients that produce the maximum number of consecutive primes
    return max_a * max_b


# Find the product of the coefficients for the quadratic expression that produces the maximum number of primes
# for consecutive values of n, starting with n = 0
a_range = range(-1000, 1001)
b_range = range(-1000, 1001)
print(find_max_consecutive_primes(a_range, b_range))
end = time.time()

print("--- %s seconds ---" % (time.time() - start_time))