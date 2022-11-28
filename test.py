
def lex_permutation():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    millionth = 1000000
    i = 1
    while i >= 1:
        new_num = []
        j = 1
        while j * factorial(len(nums)-1) < millionth:
            millionth -= factorial(len(nums)-1)
            j += 1
        print(millionth)
        print(j)
        a = (nums[j])
        new_num.append(a)
        nums.remove(nums[j])
        print(new_num)
        print(nums)


print(j_finder(6))