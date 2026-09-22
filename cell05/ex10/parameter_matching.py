x = input().split()
y = []
i = 0
while i < len(x):
    y.append(x[i])
    i += 1

z = y[0].strip('"') 
l = 1
num = 0

while l < len(y):
    if z == y[l].strip('"'):
        num += 1
    l += 1

if num > 0:
    print(num)
else:
    print("none")
