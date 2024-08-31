# Assignment 1
# 1. Write a Python program to sum all the items in a list.
my_list = [1, 2, 3, 4, 5]
total = 0
for item in my_list:
    total += item
print("Sum of the list:", total)


# 2. Write a Python program to get the largest and smallest number from a list without builtin functions.
my_list = [4, 7, 2, 9, 5]
if len(my_list) == 0:
    max_num = min_num = None
else:
    max_num = min_num = my_list[0]
    for num in my_list:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
print("Largest number:", max_num)
print("Smallest number:", min_num)


# 3. Write a Python program to find duplicate values from a list and display those.
my_list = [1, 2, 3, 1, 4, 5, 4]
seen = []
duplicates = []
for item in my_list:
    if item in seen and item not in duplicates:
        duplicates.append(item)
    seen.append(item)
print("Duplicate values:", duplicates)


# 4. Write a Python program to split a given list into two parts where the length of the first part of the list is given.
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_of_first_part = 3
first_part = original_list[:length_of_first_part]
second_part = original_list[length_of_first_part:]
print("Splitted the said list into two parts:")
print("First part:", first_part)
print("Second part:", second_part)


# 5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
original_list = ['red', 'green', 'white', 'black']
print("Traverse the list in reverse order:")
for index in range(len(original_list) - 1, -1, -1):
    print(original_list[index])


# Assignment 2
# 1. Write a Python program and calculate the mean of the below dictionary.
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
total = 0
count = 0
for value in test_dict.values():
    total += value
    count += 1
mean = total / count
print("Mean of the dictionary:", mean)


# 2. Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result_dict = {}
for d in (dic1, dic2, dic3):
    result_dict.update(d)
print("Concatenated dictionary:", result_dict)


# 3. Write a Python program to get the key, value and item in a dictionary.
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Key\tValue")
for key, value in dict_num.items():
    print(key, "\t", value)


# 4. Write a Python program to get the key, value and item in a dictionary.
input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}
cleaned_dict = {}
for k, v in input_dict.items():
    if v is not None:
        cleaned_dict[k] = v
print("dict with empty items Dropped:", cleaned_dict)


# Assignment 3
# 1. Write a Python program to find the number of times 4 appears in the tuple.
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)
count_4 = tuplex.count(4)
print("Number of times 4 appears:", count_4)


# 2. Write a Python program to convert a list to a tuple.
listx = [5, 10, 7, 4, 15, 3]
tuplex = tuple(listx)
print("Converted tuple:", tuplex)


# 3. Write a Python program to calculate the sum of the numbers in a given tuple.
tuples_list = [(1, 2), (3, 4), (5, 6)]
sum_of_tuple = 0
for t in tuples_list:
    for x in t:
        sum_of_tuple += x
print("Sum of tuple is:", sum_of_tuple)


# 4. Write a python program and iterate the given tuples
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)
employees = [employee1, employee2, employee3]

print("Employee Records:")
for emp in employees:
    print("Name:", emp[0])
    print("Employee ID:", emp[1])
    print("Department:", emp[2])
    print("Salary:", emp[3])
    print()


# Assignment 4
# 1. Write a Python program to Get Only unique items from two sets.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
unique_items = set1.union(set2) - set1.intersection(set2)
print("Unique items from both sets:", unique_items)


# 2. Write a Python program to Return a set of elements present in Set A or B, but not both.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
symmetric_diff = set1.symmetric_difference(set2)
print("Elements present in Set A or B, but not both:", symmetric_diff)


# 3. Write a Python program to Check if two sets have any elements in common. If yes, display the common elements.
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)


# 4. Write a Python program to Remove items from set1 that are not common to both set1 and set2.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
common_items = set1.intersection(set2)
set1 = set1.intersection(common_items)
print("Items common to both sets:", common_items)
