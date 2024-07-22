# Assignment 3 Question 5
# Write a program to count the occurrence of the word "INDIA" in a text file India.txt.
def count_occurrence_word(file_name, target_word):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            word_count = text.count(target_word)
            print(f"The word '{target_word}' occurred {word_count} times.")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

count_occurrence_word("India.txt", "INDIA")

# Assignment 3 Question 6
# Write a program to count and display the lines starting with "T" in a text file story.txt.
def count_lines_starting_with(file_name, start_char):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                if line.startswith(start_char):
                    print(line, end='')
                    count += 1
            print(f"\nTotal number of lines starting with '{start_char}': {count}")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

count_lines_starting_with("story.txt", "T")

# Assignment 3 Question 7
# Write a program to count the number of vowels and consonants in a file Myfile.txt.
def count_vowels_and_consonants(file_name):
    vowels = 'AEIOUaeiou'
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            vowel_count = sum(1 for char in text if char in vowels)
            consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
            print(f"Number of vowels: {vowel_count}")
            print(f"Number of consonants: {consonant_count}")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

count_vowels_and_consonants("Myfile.txt")

# Assignment 3 Question 8
# Write a program to count and display the number of words starting with "i" in a file Word.txt.
def count_words_starting_with(file_name, start_char):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            count = 0
            for word in words:
                if word.lower().startswith(start_char.lower()):
                    print(word)
                    count += 1
            print(f"Total number of words starting with '{start_char}': {count}")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

count_words_starting_with("Word.txt", "i")

# Assignment 3 Question 9
# Write a program to count and display number of words in a text file Notes.txt.
def count_words_in_notes(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            print(f"Total number of words: {len(words)}")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

count_words_in_notes("Notes.txt")

# Assignment 3 Question 10
# Write a program to display the lines having more than five words in a text file Notes.txt.
def display_lines_with_more_than_five_words(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                words = line.split()
                if len(words) > 5:
                    print(line, end='')
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

display_lines_with_more_than_five_words("Notes.txt")

# Assignment 3 Question 11
# Write a program to create a binary file "Stu.dat" and Enter students rollno, Name and Marks till the user wants.
import pickle

def create_student_binary_file(file_name):
    try:
        with open(file_name, 'wb') as file:
            while True:
                rollno = input("Enter roll number: ")
                name = input("Enter name: ")
                marks = float(input("Enter marks: "))
                student = {'rollno': rollno, 'name': name, 'marks': marks}
                pickle.dump(student, file)
                more = input("Do you want to enter more records? (yes/no): ")
                if more.lower() != 'yes':
                    break
    except Exception as e:
        print(f"An error occurred: {e}")

create_student_binary_file("Stu.dat")

# Assignment 3 Question 12
# Write a program to read a binary file "Stu.dat" and display the record of students having marks greater than 81.
def read_student_binary_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            while True:
                try:
                    student = pickle.load(file)
                    if student['marks'] > 81:
                        print(student)
                except EOFError:
                    break
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

read_student_binary_file("Stu.dat")
