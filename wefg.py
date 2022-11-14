import math
import time


def tri_num(n):
    num = ((n+1)*n)//2
    return num    # finds the  number that consists of sum of number below the n


def high_div(m):
    count = 0   # keeps the count of the divisors
    a = tri_num(m)
    for j in range(1, int(math.sqrt(a)+1)):   # tries every number below square root of the number
        if a % j == 0:    # if there is no reminder increases the count by 1
            count += 1
            if j*j != a:
                count += 1
                if count >= 500:  # if the count is 500
                    print(tri_num(m))  # print the number
                    print(count)
                    break  # stop the function
                else:
                    count = count
            else:
                count = count



for k in range(12376):
    high_div(k)


st = time.time()  # run time function
time.sleep(1)
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
