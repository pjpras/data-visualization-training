# Assignment 1
# 1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
def div(a, b):
    return a / b

num1 = 10
num2 = 2
print("Division of", num1, "by", num2, "is:", div(num1, num2))


# 2. Declare a square() function with one parameter. Then call the function and pass one number and display the square of that number.
def square(x):
    return x * x

num = 4
print("Square of", num, "is:", square(num))


# 3. Using max() and min() functions display the maximum and minimum of 5 random numbers.
import random

numbers = [random.randint(1, 100) for _ in range(5)]
print("Random numbers:", numbers)
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))


# 4. Accept a name from the user and display that in lower case using lower() function.
name = input("Enter your name: ")
print("Name in lower case:", name.lower())


# Assignment 2
# 1. Write a Python program to count the occurrences of each word in a given sentence
string = "To change the overall look of your document. To change the look available in the gallery"
words = string.lower().split()
word_count = {}
for word in words:
    word = word.strip(".")
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Word occurrences:", word_count)


# 2. Write a Python program to remove a newline in Python
string = "\nBest \nDeeptech \nPython \nTraining\n"
print("String without newlines:", string.replace("\n", " "))


# 3. Write a Python program to reverse words in a string
string = "Deeptech Python Training"
words = string.split()
reversed_words = ' '.join(words[::-1])
print("Reversed words:", reversed_words)


# 4. Write a Python program to count and display the vowels of a given text
string = "Welcome to python Training"
vowels = 'aeiou'
vowel_count = {}
for vowel in vowels:
    vowel_count[vowel] = string.lower().count(vowel)
total_vowels = sum(vowel_count.values())
print("Vowel count:", vowel_count)
print("Total vowels are:", total_vowels)


# Assignment 3
# 1. Write a Python program to Count all letters, digits, and special symbols from the given string
input_str = "P@#yn26at^&i5ve"
chars = 0
digits = 0
symbols = 0
for c in input_str:
    if c.isalpha():
        chars += 1
    elif c.isdigit():
        digits += 1
    else:
        symbols += 1
print("Chars =", chars, "Digits =", digits, "Symbols =", symbols)


# 2. Write a Python program to remove duplicate characters of a given string.
input_str = "String and String Function"
words = input_str.split()
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
print("String without duplicates:", ' '.join(unique_words))


# 3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
input_str = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase_count = 0
lowercase_count = 0
number_count = 0
special_count = 0
for c in input_str:
    if c.isupper():
        uppercase_count += 1
    elif c.islower():
        lowercase_count += 1
    elif c.isdigit():
        number_count += 1
    else:
        special_count += 1
print("UpperCase :", uppercase_count)
print("LowerCase :", lowercase_count)
print("NumberCase :", number_count)
print("SpecialCase :", special_count)


# 4. Write a Python Count vowels in a string
input_str = "Welcome to Python Assignment"
vowels = 'aeiou'
vowel_count = 0
for c in input_str.lower():
    if c in vowels:
        vowel_count += 1
print("Total vowels are:", vowel_count)
