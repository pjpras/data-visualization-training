# 1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd
num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print("The number is " + result + ".")

# 2. Using input function take two numbers and then swap the numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
temp = num1
num1 = num2
num2 = temp
print("After swapping: First number is " + str(num1) +
      " and Second number is " + str(num2) + ".")

# 3. Write a Program to Convert Kilometers to Miles
km = float(input("Enter distance in kilometers: "))
miles = km * 0.621371
print(str(km) + " kilometers is equal to " + str(miles) + " miles.")

# 4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year
principal = 200
rate = 5
time = 5
simple_interest = (principal * rate * time) / 100
print("The Simple Interest is Rs "+str(simple_interest))
