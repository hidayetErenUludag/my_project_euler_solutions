import time

start = time.time()
def calc():
    count = 1
    current_num = 1
    for square in range(1, 501):
        a = 0
        b = 0
        b += current_num + square*2
        a += (b + 3*(square*2))
        current_num = a
        count += (a+b)*2
        square += 1
    return count

a = calc()
end = time.time()
print(a, (end-start))



