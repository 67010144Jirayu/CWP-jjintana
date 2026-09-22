x = (input().upper()).split(" ")
y =[]
i = 0
while i < len(x):
    y.append(x[i])
    i += 1

if len(y) > 0:
    y[0] = y[0][1:] 
    y[-1] = y[-1][:-1] 
    i = 0
    while i < len(y):
        print(y[i], end=" ")
        i += 1
else:
    print("none")
