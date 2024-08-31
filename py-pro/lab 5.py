# Assignment 1 Question 1
# Write a function in Python to read the content from a text file "ABC.txt" line by line and display the same on screen.
def read_file_line_by_line(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print("The file " + file_name + " does not exist.")

read_file_line_by_line("ABC.txt")

# Assignment 1 Question 2
# Write a function in Python to count and display the total number of words in a text file "ABC.txt".
def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            print("Total number of words: " + str(len(words)))
    except FileNotFoundError:
        print("The file " + file_name + " does not exist.")

count_words_in_file("ABC.txt")

# Assignment 1 Question 3
# Write a function in Python to count uppercase character in a text file "ABC.txt".
def count_uppercase_characters(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            uppercase_count = sum(1 for char in text if char.isupper())
            print("Total number of uppercase characters: " + str(uppercase_count))
    except FileNotFoundError:
        print("The file " + file_name + " does not exist.")

count_uppercase_characters("ABC.txt")

# Assignment 1 Question 4
# Write a function display_words() in Python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.
def display_words(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    if len(word) < 4:
                        print(word)
    except FileNotFoundError:
        print("The file " + file_name + " does not exist.")

display_words("story.txt")

# Assignment 2 Question 1
# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def divide_numbers(a, b):
    try:
        result = a / b
        print("Result: " + str(result))
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

divide_numbers(10, 0)

# Assignment 2 Question 2
# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
def get_integer_input():
    try:
        number = int(input("Enter an integer: "))
        print("You entered: " + str(number))
    except ValueError:
        print("Error: Input is not a valid integer.")

get_integer_input()

# Assignment 2 Question 3
# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
def open_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: The file " + file_name + " does not exist.")

open_file("file.txt")

# Assignment 2 Question 4
# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
def get_two_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("First number: " + str(num1) + ", Second number: " + str(num2))
    except ValueError:
        raise TypeError("Both inputs must be numbers.")

get_two_numbers()
