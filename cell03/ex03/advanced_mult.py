table = 0
while table <= 10:
    print("table de", table, ":", end=" ")
    number = 0
    while number <= 10:
        print(table * number, end=" ")
        number = number + 1
    print()
    table = table + 1
