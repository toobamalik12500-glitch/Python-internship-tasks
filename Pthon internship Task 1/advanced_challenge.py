#function to calculate total marks
def calculate_total(marks):
    total=sum(marks)
    return total
#function to calculate percentage
def calculate_percentage(total,subjects):
    total_possible_marks=subjects*100
    percentage = (total / total_possible_marks) * 100
    return percentage
#function to calculate grade
def calculate_grade(percentage):

    if percentage >= 80:
        grade="A"
    elif percentage>=70:
        grade="B"
    elif percentage>=60:
        grade="C"
    elif percentage >= 50:
        grade = "D"

    else:
        grade = "Fail"

    return grade
#ask for number of students
number_of_students=int(input("enter numbers of students"))

#store highest percentage and student name
highest_percentage=0
highest_student=""

#Take information of multiple students
for i in range(number_of_students):
      name = input("Enter student name: ")
      subjects=int(input("enter number of subjects:"))

# Create an empty list to store marks
      marks = []
      for j in range(subjects):
       mark=float(input(f"enter marks for subject{j+1}: "))
       marks.append(mark)

#calculate total marks
total=calculate_total(marks)

# Task 4 - Calculate percentage
percentage = calculate_percentage(total, subjects)

# Task 5 - Calculate grade
grade = calculate_grade(percentage)
#test wheather student pass or fail
if percentage>=50:
    result="passed"
else:
    result="failed"

# Display student result
print("\n----- Student Result -----")
print("Student Name:", name)
print("Total Marks:", subjects * 100)
print("Obtained Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)
#chek for the highest percentage
if percentage>highest_percentage:
    highest_percentage=percentage
    highest_student=name  

# Display highest percentage student
print("\n----- Highest Percentage -----")
print("Student name",highest_student)
print("Highest Percentage:", highest_percentage, "%")



        










