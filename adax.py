num = 600851475143
i = 2
while i < num//2:
    if num % i == 0:
        num = num/i
        i = i+1
    else:
        i = i+1
print(num)

