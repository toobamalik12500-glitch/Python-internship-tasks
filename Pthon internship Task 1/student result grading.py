# Function to calculate total marks
def calculate_total(marks):
    total = sum(marks)
    return total


# Function to calculate percentage
def calculate_percentage(total, subjects):
    total_possible_marks = subjects * 100
    percentage = (total / total_possible_marks) * 100
    return percentage


# Function to calculate grade
def calculate_grade(percentage):

    if percentage >= 80:
        grade = "A"

    elif percentage >= 70:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    elif percentage >= 50:
     grade = "D"

    else:
        grade = "Fail"

    return grade


#Ask for student name
name = input("Enter student name: ")


# Ask for number of subjects
subjects = int(input("Enter number of subjects: "))


# Create an empty list to store marks
marks = []


#Take marks for each subject
for i in range(subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)


#Calculate total marks
total = calculate_total(marks)


#Calculate percentage
percentage = calculate_percentage(total, subjects)


#Calculate grade
grade = calculate_grade(percentage)


# Task 6 - Check whether student passed or failed
if percentage >= 50:
    result = "Passed"
else:
    result = "Failed"


# Display final result
print("Student Result")
print("Student Name:", name)
print("Total Marks:", subjects * 100)
print("Obtained Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)







 
 





 