alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v"
    , "w", "x", "y", "z"]


def spliter(n):
    f = open("words.txt","w")
    remain = len(alphabet) % n
    for i in range(len(alphabet) - remain):
        count = 0
        for j in range(n):
            f.write(alphabet[count])
            count += 1





spliter(3)