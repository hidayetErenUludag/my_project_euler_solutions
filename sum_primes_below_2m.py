
def primes_upto(limit):
    limitN = limit+1
    not_prime = set()
    primes = [2]

    for i in range(3, limitN, 2):
        if i in not_prime:
            continue

        for j in range(i*3, limitN, i*2):
            not_prime.add(j)

        primes.append(i)
    return primes

print(sum(primes_upto(2000000)))






