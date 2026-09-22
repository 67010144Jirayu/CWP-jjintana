x = input().strip('"')
i = 0
num = 0
while i < len(x):
    if x[i] == "z":
        print("z", end="")
        num += 1
    i += 1

if num == 0:
    print("none")

else:
    print()
