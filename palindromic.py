def ispalindrome(n):
    return str(n) == str(n)[::-1]
liste = []
for a in range(100, 1000):
    for b in range(100, 1000):
        c = a*b
        if ispalindrome(c):
            liste.append(c)
clean_liste = [*set(liste)]
clean_liste.sort(reverse=True)
print(clean_liste)
