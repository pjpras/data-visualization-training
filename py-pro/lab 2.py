# 1. Python program to check leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# 2. Python Program to Find the Largest Among Three Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("The largest number is", largest)

# 3. Python Program to Check if a Number is Positive, Negative or 0
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 4. Toy vendor discount calculation program
product_code = int(input("Enter product code (1 for Battery, 2 for Key-based, 3 for Electrical): "))
order_amount = float(input("Enter order amount: "))
if product_code == 1 and order_amount > 1000:
    discount = 0.10
elif product_code == 2 and order_amount > 100:
    discount = 0.05
elif product_code == 3 and order_amount > 500:
    discount = 0.10
else:
    discount = 0.0
net_amount = order_amount - (order_amount * discount)
print("The net amount to be paid is", net_amount)

# 5. Transport company fare calculation program
distance = int(input("Enter distance travelled in km: "))
if distance <= 50:
    fare = distance * 8
elif distance <= 100:
    fare = (50 * 8) + ((distance - 50) * 10)
else:
    fare = (50 * 8) + (50 * 10) + ((distance - 100) * 12)
print("The total fare is", fare, "Rs.")

# 6. Python program to reverse a number using a while loop
num = int(input("Enter a number: "))
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed number is", reversed_num)

# 7. Python program to check whether a number is palindrome or not
num = int(input("Enter a number: "))
original_num = num
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
if original_num == reversed_num:
    print(original_num, "is a palindrome.")
else:
    print(original_num, "is not a palindrome.")

# 8. Python program to find the factorial of a given number using a while loop
num = int(input("Enter a number: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print("The factorial is", factorial)

# 9. Accept numbers using input() function until the user enters 0 and display the sum of all the numbers
total_sum = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total_sum += num
print("The sum of all numbers is", total_sum)

# 10. Print the first 10 natural numbers using for loop
for i in range(1, 11):
    print(i)

# 11. Python program to check if the given string is a palindrome
string = input("Enter a string: ")
if string == string[::-1]:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")

# 12. Python program to check if a given number is an Armstrong number
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

# 13. Python program to get the Fibonacci series between 0 to 50
a, b = 0, 1
while a <= 50:
    print(a)
    a, b = b, a + b

# 14. Python program to check the validity of password input by users
password = input("Enter a password: ")

is_valid = True
if len(password) < 6 or len(password) > 12:
    is_valid = False

has_lower = False
has_upper = False
has_digit = False
has_special = False

for char in password:
    if char.islower():
        has_lower = True
    if char.isupper():
        has_upper = True
    if char.isdigit():
        has_digit = True
    if char in "@#$":
        has_special = True

if not (has_lower and has_upper and has_digit and has_special):
    is_valid = False

if is_valid:
    print("Password is valid.")
else:
    print("Password is not valid.")

