num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num2>num1: 
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} both are equal")