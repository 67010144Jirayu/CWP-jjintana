x = input().split()
if len(x) > 0:
    print("parameters:" + str(len(x)))
    for i in x:
        i = i.strip('"')
        print(i + " : " + str(len(i)))
else:
    print("none")
