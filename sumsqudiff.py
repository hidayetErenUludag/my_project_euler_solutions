i = 1
num_list = [] #stores the i squared
while i < 101:
    num_list.append(i*i) # finds the spare of i
    i = i+1 # adds 1 to i


a = 1
num_lisit_2 = []

while a < 101:
    num_lisit_2.append(a)
    a = a+1


s = sum(num_lisit_2)
c = sum(num_list)

print((s**2)-c)
