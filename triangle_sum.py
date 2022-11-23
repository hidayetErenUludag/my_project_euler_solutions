import time

start = time.time()

my_list = [line.split() for line in open("triangle.txt")]
nums = my_list


def highest_finder(n):
    while len(nums) > 1:
        list = []
        for i in range(len(nums[-2])):
            a = (nums[-2][i] + max(nums[-1][i], nums[-1][i+1]))
            list.append(a)
        nums.pop(-1)
        nums.pop(-1)
        nums.append(list)
    print(nums)


highest_finder(4)
