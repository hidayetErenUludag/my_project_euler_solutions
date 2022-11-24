def value_name(name):
    alphet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value = 0
    for i in name:
        if i in alphet:
            value += alphet.index(i) + 1
    return value

# from https://stackoverflow.com/questions/50982483/names-scores-project-euler-22

with open("/Users/hidayeterenuludag/Desktop/p022_names.txt", "r") as File:
    Data = sorted(File.readlines()[0].split(','))

    result = 0
    for position, name in enumerate(Data):
        name_score = value_name(name) * (position + 1)
        result += name_score

    print(result)