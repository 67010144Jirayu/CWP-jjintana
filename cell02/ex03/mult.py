first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
Multiplication = first_number * second_number
print(first_number, "x", second_number, "=", Multiplication)
if Multiplication < 0:
    print("The result is negative.")
elif Multiplication > 0:
    print("The result is positive.")
else:
    print("The result is zero.")
