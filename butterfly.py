n = 4
str = ""
for i in range(1, n+1):
    for j in range(i):
        str += "*"
    for j in range(2*n - 2*i):
        str += " "
    for j in range(i):
        str += "*"
    print(str)
    str = ""
for i in range(n, 0, -1):
    for j in range(i):
        str += "*"
    for j in range(2*n - 2*i):
        str += " "
    for j in range(i):
        str += "*"
    print(str)
    str = ""
