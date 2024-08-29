n = 5
pattern = ""
for i in range(1, n+1):
    for j in range(n-i):
        pattern += " "
    for j in range(i, 0, -1):
        pattern += str(j)
    for j in range(2, i+1):
        pattern += str(j)
    print(pattern)
    pattern = ""
