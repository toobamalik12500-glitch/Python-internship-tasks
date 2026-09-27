# TASK 6 – Student Performance Data Analysis

# Import pandas
import pandas as pd

# Create student data
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Zahra", "Usman"],
    "Roll Number": [1, 2, 3, 4, 5],
    "Marks": [85, 72, 39, 91, 68]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display all students
print("===== Student Performance Analysis =====")
print()
print(df)

# Calculate average marks
average_marks = df["Marks"].mean()

# Find highest marks
highest_marks = df["Marks"].max()

# Find lowest marks
lowest_marks = df["Marks"].min()

# Count passing students
passing_students = df[df["Marks"] >= 50]

# Count failing students
failing_students = df[df["Marks"] < 50]

# Find top student
top_student = df.loc[df["Marks"].idxmax(), "Name"]

# Display basic analysis
print()
print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)

print()
print("Passing Students:", len(passing_students))
print("Failing Students:", len(failing_students))

print()
print("Top Student:", top_student)


# Intermediate Level

# Add grades
def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

df["Grade"] = df["Marks"].apply(get_grade)

print()
print("Student Grades:")
print(df)


# Find Top 3 students
top_3_students = df.sort_values("Marks", ascending=False).head(3)

print()
print("Top 3 Students:")
print(top_3_students)


# Find students above 80 marks
students_above_80 = df[df["Marks"] > 80]

print()
print("Students Above 80 Marks:")
print(students_above_80)