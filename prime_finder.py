import math

num = 600_851_475_143
i = 1
while i < math.sqrt(num):
    if num % i == 0:
        num = num/i
        i = i+1
    else:
        i = i+1


print(num)