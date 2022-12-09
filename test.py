import time


start = time.time()

def fifth_power():
    digits = []
    for i in range(2, 1000000):
        a = 0
        for j in str(i):
            a += (int(j)**5)
        if a == i:
            digits.append(i)
    print(sum(digits))


fifth_power()

end = time.time()
print(end-start, "seconds")
