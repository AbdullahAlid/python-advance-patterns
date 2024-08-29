n = 5
str = ""
for i in range(n):
    for j in range(n-i-1):
        str += " "
    for j in range(n):
        str += "*"
    print(str)
    str = ""
