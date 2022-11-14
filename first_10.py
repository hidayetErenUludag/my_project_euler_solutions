given_nums = []


f = open("num/ert/nums.txt", "rb")

for say in f:
    given_nums.append(int(say))
a = str(sum(given_nums))


print(a[:10])
