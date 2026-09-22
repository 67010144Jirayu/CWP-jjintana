x = [2, 8, 9, 48, 8, 22, -12, 2]
y = []
i = 0
while i < len(x):
    if x[i] > 5:
        y.append(x[i]+2)
        i += 1
    else:
        i += 1
print(x)
print(y)
