x = input().split('"')
y = []
i = 1
while i < len(x):
    y.append(x[i])
    i += 2

if len(y) > 0:
    print(y[0])
else:
    print("none")
