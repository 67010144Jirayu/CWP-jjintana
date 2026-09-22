age = input("Please tell me your age: ")
print("Your are currently " + str(age) + " years old.")
i = 0
y = 10
for i in range(1,4):
    print("In " + str(y) + " years, you will be " + str(int(age) + y) + " years old.")
    y = y + 10
