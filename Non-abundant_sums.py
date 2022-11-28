import time

start = time.time()


def non_abundant_number():
    abundants = []
    for i in range(1, 28124):
        sum = 0
        for j in range(1, i):
            if i % j == 0:
                sum += j
        if sum > i:
            abundants.append(i)
    return abundants


def non_sum_abundant():
    a = non_abundant_number()
    nums = []
    al_nums = []
    for k in range(1, 28124):
        al_nums.append(k)
    for i in a:
        for j in a:
            if i+j <= 28123:
                nums.append(i+j)
    res = [*set(nums)]
    a = list(set(al_nums).intersection(res))
    print(sum(al_nums)-sum(a))


non_sum_abundant()
end = time.time()
print("time", end-start)