x = input().split(" ")
y =[]
i = 0
while i < len(x):
    y.append(x[i])
    i += 1

if len(y) > 1: 
    i = len(y) -1
    while i >= 0:
        print(y[i])
        i -= 1
else:
    print("none")
