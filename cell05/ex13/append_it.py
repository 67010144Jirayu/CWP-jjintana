x = input().split()
y=[]
i= 0
while i < len(x):
    y.append(x[i].strip('"'))
    i += 1
l = 0

while l < len(y):
    if y[l][-3:] == "ism":
        print(y[l])
    else:
        print(y[l]+"ism")
    l += 1

if len(y) == 0:
    print("none")
