scd = 2
i = 1
while i < 20:
    if scd % i == 0:
        i = i+1
    else:
        i = 1
        scd = scd+1
print(scd)
