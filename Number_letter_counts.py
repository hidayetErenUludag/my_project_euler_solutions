import inflect


p = inflect.engine()


def num_writer(n):
    list = []
    for i in range(1, n+1):
        w = p.number_to_words(i)
        list.append(w)
        print(list)
    return list


def length_finder(m):
    a = 0
    b = 0
    for j in num_writer(m):
        a += len(j)
        b += j.count(" ") + j.count("-")
    return a-b


print(length_finder(1000))
