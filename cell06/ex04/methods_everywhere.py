def shrink(x):
    print(x[:8])

def enlarge(x):
    while len(x) < 8:
        x = x + "Z"
    print(x)

word = input().split()

i = 0

if len(word) > 0:
    while i < len(word):
        x = word[i].strip("'\"")
        if len(x) > 8:
            shrink(x)

        elif len(x) < 8:
            enlarge(x)

        else:
            print(x)

        i += 1

else:
    print("none")
