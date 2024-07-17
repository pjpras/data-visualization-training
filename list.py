stdid = ['std101','std102','std103','std104','std105','std106','std107','std108','std109','std110']
stdname = ['Ashish Kumar','Abhishek Kumar','Aman','Rahul','Ruby','Suman','Saurabh','Sumit','Kamlesh','Rohan']
standard = [10,10,10,10,10,10,10,10,10,10]
Age = [15,14,15,14,13,13,15,14,15,15]
Hindi = [67,85,23,45,89,90,45,23,45,34]
English = [89,45,56,67,67,46,23,45,56,12]
Maths = [87,48,78,45,89,67,34,67,78,24]
Science = [89,90,78,45,93,67,45,78,99,45]
Computer = [90,45,67,56,65,67,34,90,67,56]
Total = [422,313,302,258,403,337,181,303,345,171]


# Print header
header = "StdId   | StdName         | Standard | Age | Hindi | English | Maths | Science | Computer | Total"
print(header)
print("-" * len(header))

students = []
for i in range(len(stdid)):
	students.append([stdid[i], stdname[i], standard[i], Age[i], Hindi[i], English[i], Maths[i], Science[i], Computer[i], Total[i]])

for student in students:
    print(f"{student[0]:<7} | {student[1]:<15} | {student[2]:<8} | {student[3]:<3} | {student[4]:<5} | {student[5]:<7} | {student[6]:<5} | {student[7]:<7} | {student[8]:<8} | {student[9]}")
print()



# Index positions for each attribute in the student lists
STDID, STDNAME, STANDARD, AGE, HINDI, ENGLISH, MATHS, SCIENCE, COMPUTER, TOTAL = range(10)

# Students who scored more than 50 in English
print("Students who scored more than 50 in English:")
for student in students:
	if student[ENGLISH] > 50:
		print(student[STDNAME])
print()

# Sort the students list by Maths score in descending order and get top four
top_scorers = sorted(students, key=lambda x: x[MATHS], reverse=True)[:4]
print("Top four scorers in Maths:")
for scorer in top_scorers:
	print(f"Name: {scorer[STDNAME]}, Age: {scorer[AGE]}")
print()

# Sort the students list by Computer score in ascending order and get bottom three
bottom_scorers = sorted(students, key=lambda x: x[COMPUTER])[:3]
print("Bottom three scorers in Computer:")
for scorer in bottom_scorers:
	print(f"StdId: {scorer[STDID]}, Name: {scorer[STDNAME]}, Age: {scorer[AGE]}")      