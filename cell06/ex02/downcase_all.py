def downcase_it(y):
    return y.lower()
word = input().split('"')
y = []
i = 1

while i < len(word):
    y.append(word[i])
    i += 2
i = 0

if len(y) > 0:
    while i < len(y):
        print(downcase_it(y[i]))
        i += 1
else:
    print("none")
