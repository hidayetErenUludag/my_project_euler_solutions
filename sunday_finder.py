normal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


total_year = [normal_year] * 100


for i in range(3, len(total_year), 4):
    total_year[i] = leap_year


today = (365) % 7
sunday_count = 0
for j in total_year:
    for k in j:
        if today % 7 == 6:
            sunday_count += 1
        today += k % 7
print(sunday_count)


