n = 5
msg = ""
for i in range(n):
    for j in range(n-i-1):
        msg += " "
    for j in range(i+1):
        msg += str(i+1)+" "
    print(msg)
    msg = ""
