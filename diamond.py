n = 4
str = ""
k = 0
for i in range(1, n+1):
    for _ in range(n-i):
        str += " "
    for _ in range(i+k):
        str += "*"
    print(str)
    str = ""
    k += 1
k = n-1
for i in range(n, 0, -1):
    for _ in range(n-i):
        str += " "
    for _ in range(i+k):
        str += "*"
    print(str)
    str = ""
    k -= 1
